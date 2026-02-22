# Photoshop-Style Features Checklist

This document lists common Adobe Photoshop features and how **Image Editor Pro** compares.

## ✅ Implemented (we have it)

### File
| Feature | Our implementation |
|--------|---------------------|
| New | **File > New** – width, height, background White/Transparent |
| Open image | **File > Open Image** – PNG, JPG, BMP, GIF |
| Open project | **File > Open Project** – .iep (all layers) |
| Save image | **File > Save Image** – PNG, JPG |
| Save project | **File > Save Project** – .iep |
| Revert | **File > Revert** – reload from last saved .iep (when modified) |
| Save Project As | **File > Save Project As** – always show save dialog |
| Export As | **File > Export As** – export composite to a new file (PNG/JPEG) |
| Open Recent | **File > Open Recent** – last 8 opened files (images or .iep) |
| Quit | **File > Quit** |

### Edit
| Feature | Our implementation |
|--------|---------------------|
| Undo | **Edit > Undo** (Ctrl+Z) |
| Redo | **Edit > Redo** (Ctrl+Y) |
| Clear | **Edit > Clear Layer** – fill current layer with transparent |
| Fill | **Edit > Fill** – color + opacity for current layer |
| Copy merged | **Edit > Copy Merged** (Ctrl+Shift+C) – composited image to clipboard |
| Paste as new layer | **Edit > Paste as New Layer** (Ctrl+Shift+V) |

### Image
| Feature | Our implementation |
|--------|---------------------|
| Flip Horizontal | **Image > Flip Horizontal** |
| Flip Vertical | **Image > Flip Vertical** |
| Rotate 90° CW / CCW | **Image > Rotate 90° CW / 90° CCW** |
| Rotate 180° | **Image > Rotate 180°** |
| Image Size | **Image > Resize Image** – canvas and all layers |
| Canvas Size | **Image > Canvas Size** – expand/shrink with anchor (9 positions) |
| Crop | **Image > Crop** – dialog: Left, Top, Width, Height |
| Trim | **Image > Trim** – trim canvas to content (transparent pixels or top-left color) |
| Make color transparent | **Image > Make color transparent** – color + tolerance |
| Rotate Arbitrary | **Image > Rotate Arbitrary** – current layer by any angle (degrees) |

### Layer
| Feature | Our implementation |
|--------|---------------------|
| New layer | **Layer > New Layer** (Ctrl+Shift+N) |
| Duplicate layer | **Layer > Duplicate Layer** (Ctrl+J) |
| Delete layer | Remove via Layers panel |
| Merge down | **Layer > Merge Down** (Ctrl+E) |
| Flatten image | **Layer > Flatten Image** – merge all into one (undoable) |
| Layer opacity | Slider in Layers panel |
| Layer visibility | Checkbox in Layers panel |
| Layer rename | Double-click layer name in panel |
| Remove last filter from layer | **Layer > Remove last filter from layer** (per-layer) |
| Add text | **Layer > Add Text...** – text, font (Arial, Times, Courier, Georgia, Verdana, etc.), size, color, position (Top-left / Center / Custom X,Y) on current layer |

### Filter / Adjustments
| Feature | Our implementation |
|--------|---------------------|
| Blur | **Filter > Blur** (radius) |
| Sharpen | **Filter > Sharpen** |
| Brightness | **Filter > Brightness** |
| Contrast | **Filter > Contrast** |
| Hue/Saturation | **Filter > Hue/Saturation** |
| Grayscale | **Filter > Grayscale** |
| Invert | **Filter > Invert** |
| Edge detect | **Filter > Edge Detect** |
| Sepia | **Filter > Sepia** |
| Posterize | **Filter > Posterize** (bits) |
| Emboss | **Filter > Emboss** |
| Smooth | **Filter > Smooth** – soften/smooth layer |
| Detail | **Filter > Detail** – enhance fine details |

### View
| Feature | Our implementation |
|--------|---------------------|
| Zoom in/out | **View > Zoom In/Out** (Ctrl+/-), Ctrl+scroll |
| Reset zoom | **View > Reset Zoom** (Ctrl+0) |
| Fit to window | **View > Fit to Window** (Ctrl+1) |
| Actual Size (100%) | **View > Actual Size (100%)** (Ctrl+2) |
| Panels | **View > Panels** – toggle Layers, Tools, History docks |
| Transparency display | **View > Transparency display** – Checkerboard, White, Gray, Black |

### Tools
| Feature | Our implementation |
|--------|---------------------|
| Brush | Brush tool (B), size 1–200, opacity, color |
| Eraser | Eraser tool (E) |
| Eyedropper | Eyedropper (I) – pick color from canvas |
| Paint bucket | Paint bucket (G) – fill contiguous area, tolerance 0–255 |
| Color picker | Choose color in Tools panel |
| Tool shortcuts | B, E, I, G, R, U for Brush, Eraser, Eyedropper, Paint bucket, Rectangle, Ellipse |
| Rectangle / Ellipse | Shape tools: click-drag to draw filled rectangle or ellipse on current layer |

### Other
| Feature | Our implementation |
|--------|---------------------|
| Layers panel | Dockable, thumbnails, reorder, opacity, visibility |
| Tools panel | Brush size, opacity, color, tool buttons, paint bucket tolerance |
| History panel | Dockable list of undo steps (most recent at top) |
| Status bar | Zoom %, dimensions, cursor position |
| Preferences | Edit > Preferences: default new image size, brush size, background |
| Image > Mode | Grayscale (current layer) |
| Open Recent | Clear list action when list is non-empty |
| Undo/redo (global) | Up to 50 steps |
| Per-layer filter undo | Remove last filter from layer (multiple steps per layer) |
| New project background | White or Transparent |
| Help | **Help > Keyboard Shortcuts**, **Help > About** |

---

## ❌ Not implemented (possible future work)

| Photoshop feature | Notes |
|-------------------|--------|
| **Selection tools** | Rectangular, elliptical, lasso, magic wand – no selection yet |
| **Crop to selection** | Would need selection first |
| **Cut / Copy selection** | Would need selection |
| **Text tool (advanced)** | Multiple fonts, positioning, text on path (we have Layer > Add Text) |
| **Line / custom shape** | Line tool, polygon, custom shapes (we have rectangle and ellipse) |
| **Brush presets** | Saved brush size/opacity/color sets |
| **Layer groups** | Group layers in panel |
| **Blend modes** | Multiply, Screen, Overlay, etc. |
| **Layer masks** | Hide/show parts of layer with grayscale mask |
| **Adjustment layers** | Non-destructive brightness/contrast etc. |
| **Rulers & guides** | On-canvas rulers and drag guides |
| **Image > Mode (full)** | RGB, Grayscale mode for whole document (we have Grayscale for current layer) |
| **Preferences** | App-wide settings (we only save window layout) |

---

## Summary

Image Editor Pro covers core Photoshop-like workflow: layers, brush/eraser/eyedropper/paint bucket (B/E/I/G), main adjustments and filters, transforms (flip/rotate, rotate arbitrary), resize/canvas size/crop/trim, fill/clear, transparency options, copy/paste merged, flatten, revert, recent files, and export as. Selection-based editing, text, shapes, blend modes, and masks are not implemented and are the main gaps for a “full” Photoshop clone.
