# Evolution of the Architecture

This document captures the main lessons from building and refining Image Editor Pro in place—focusing on the path from a basic canvas to a responsive, predictable image editor.

---

## 1. The Initial Hurdle: Getting a Basic Canvas to Render and Apply a Simple Filter

**Goal:** Show an image on screen and change its pixels (e.g. one filter) without the app falling over.

**Challenges:**

- **Rendering pipeline:** The canvas is a Qt widget; image data lives as PIL `Image` in the model. The missing link was a consistent path: **PIL → NumPy array → QImage → QPixmap → `QPainter.drawPixmap()`**. Getting the format right (e.g. RGBA, `bytes_per_line`) and doing this in `paintEvent` was the first real milestone.
- **Single source of truth:** The project had to own the image (and later, layers). The canvas had to *read* from the project and redraw when the project changed, not hold its own copy of the image that could drift out of sync.
- **First filter:** Applying a filter meant: get the current image from the model, run the filter (PIL/NumPy), put the result back into the model, then refresh the canvas. That required a clear place for “current image” (e.g. one layer or a single image) and a way to trigger a redraw (e.g. a method that called `update()` on the canvas).

**Takeaway:** The initial hurdle was less about the filter math and more about establishing a simple, single-path data flow: **model (image) → render (PIL → QImage/QPixmap) → canvas `paintEvent`**, plus a clear trigger to repaint when the model changed.

---

## 2. The Refinement Phase: State Management and Optimized Updates

**Goal:** Move from “redraw everything all the time” to targeted updates and predictable state so the UI stays responsive and correct.

**What changed:**

- **Signals instead of polling:** The `Project` model emits `layers_changed` and `layer_modified(index)`. The canvas and layer panel connect to these and only then call `update()` or refresh. That way, only the parts that care about a change react—no global “refresh entire UI” on every tiny action.
- **Command pattern for undo/redo:** Every mutation (draw, add layer, filter, opacity, etc.) became a command that holds the minimal state needed to undo (e.g. `old_image` and `new_image` for draws and filters). The main window executes commands through a single `CommandHistory`, so undo/redo is consistent and the model doesn’t get partially updated.
- **Explicit copies at boundaries:** Commands and the canvas treat “before” and “after” as explicit copies (e.g. `old_image.copy()`, `new_image.copy()` in `DrawCommand` and `FilterCommand`). That avoids shared references and accidental mutation of undo data or the live layer.
- **Heavy work off the GUI thread:** Filter application runs in a `FilterWorker` (QThread). The UI passes in a *copy* of the layer image and shows a progress dialog; when the worker emits `result_ready`, the main thread applies the result and updates the model. That keeps the UI responsive on large images and avoids the “one big re-render + filter” blocking the event loop.
- **Eraser and compositing:** The eraser needed to “reveal” what’s below, not just paint white. That meant a dedicated `render_below(layer_index)` that composites only layers below the current one (e.g. on a white background) and using that as the eraser’s target color for the stroke, with a stable cache for the duration of the stroke.

**Takeaway:** Refinement was mostly about **who owns the data** (project/layers), **who reacts** (canvas and panels via signals), and **where copies happen** (commands, worker input/output). That made state predictable and updates localized instead of heavy re-renders everywhere.

---

## 3. The “Break” Point: UI Lag and Image Corruption from Data Flow

**What went wrong:**

- **Canvas lag:** Every `layer_modified` or `layers_changed` led to a full `project.render()` in `paintEvent`: composite all layers, then PIL → NumPy → QImage → QPixmap. On large or many layers, that happened too often (e.g. on every brush move or opacity slider change), so the UI felt sluggish or froze.
- **Corruption / garbage on canvas:** The canvas (and sometimes thumbnails) built a `QImage` from a NumPy array’s buffer: `QImage(img_array.data, w, h, bytes_per_line, QImage.Format.Format_RGBA8888)`. `QImage` does not take ownership of that buffer. When the NumPy array went out of scope or was reused, the buffer could be invalid or overwritten, so the canvas or thumbnails sometimes showed garbage or the wrong image.

**How it was fixed:**

- **Targeted repaints:** The canvas still does a full composite in `paintEvent`, but repaints are driven only by the signals that actually indicate a change (`layers_changed`, `layer_modified`). No extra timers or broad “refresh all” calls. For filters, the worker finishes and then one signal applies the result and triggers one repaint, instead of repainting during the filter run.
- **Stable buffer for display:** Where we need a QImage from a NumPy array, we ensure the underlying buffer is valid for the whole time it’s used. That can mean:
  - Using a **copy** of the array (e.g. `np.array(rendered_image, copy=True)` or `img_array.copy()`) so the QImage has its own memory, or
  - Building the QImage and then creating a QPixmap from it immediately so Qt’s internal copy in the pixmap holds the pixels, and not holding the QImage or the array around longer than the paint call.
- **Thumbnails:** Layer thumbnails go through a similar PIL → NumPy → QImage path; the same rule applies: either copy the buffer or keep the lifecycle of the array and QImage aligned so the buffer is never used after it’s invalid.

**Takeaway:** The “break” was a mix of **too many full re-renders** (solved by signal-driven, minimal updates) and **unsafe use of buffer ownership** (solved by copying or shortening the lifetime of buffers used for QImage). Data flow had to be both “when to update” and “how to hand data to Qt without dangling pointers.”

---

## 4. The Technical Delta: What I Know Now About Memory and Canvas Performance

**Memory:**

- **PIL and NumPy:** Layers and undo stacks hold full pixel buffers. Copying images (e.g. `layer.image.copy()`) is explicit and necessary for undo and for passing data to workers; the cost is proportional to layer size and history length. Capping history (e.g. 50 commands) and avoiding unnecessary copies in hot paths keeps memory growth under control.
- **Qt and buffers:** Constructing `QImage` from a raw buffer (e.g. `img_array.data`) does **not** copy; the QImage is only valid while that buffer is valid and unchanged. For anything that outlives the immediate call (or that might be painted asynchronously), use a copy or a QImage/QPixmap that Qt has copied internally.
- **Serialization:** Saving projects (e.g. .iep) encodes layer images (e.g. PNG in base64). That’s a separate copy and can be large; it’s on disk, not in the same hot path as rendering.

**Canvas performance:**

- **Render on demand:** The composite is done in `paintEvent` when Qt asks for it, not in a cache that has to be invalidated everywhere. That keeps the logic simple and avoids cache invalidation bugs; the cost is one full composite per paint. Keeping repaints to “when the project actually changed” (signals) is what makes this acceptable.
- **Format and scaling:** Using a single format (e.g. RGBA) end-to-end and doing zoom by scaling the final pixmap (or the canvas size) avoids repeated format conversions and keeps the pipeline understandable.
- **Worker thread:** Any heavy, synchronous work (big filters, future bulk operations) should run in a worker thread and only touch the model and canvas from the main thread when the result is ready. That prevents the UI from freezing and keeps the data flow clear (main thread owns the project and canvas).

**Design choices that stuck:**

- **One project, one canvas:** The project owns all layers and dimensions; the canvas is a view that renders `project.render()` and forwards input. No duplicate “display copy” of the image that could get out of sync.
- **Commands own before/after state:** Undo is reliable because each command stores the exact old and new state (e.g. images) it needs to undo/redo, and the main window is the only place that executes or reverts commands.
- **Signals for propagation:** Model changes emit signals; views (canvas, panels) subscribe and update. That keeps the dependency one-way (model → views) and avoids tight coupling.

---

*This project was refined in place through multiple iterations rather than by starting new versions. These learnings reflect the evolution of its architecture and data flow.*
