# User Guide

## Table of Contents

1. [Getting Started](#getting-started)
2. [Interface Overview](#interface-overview)
3. [Working with Projects](#working-with-projects)
4. [Layer Management](#layer-management)
5. [Drawing and Painting](#drawing-and-painting)
6. [Applying Filters](#applying-filters)
7. [Keyboard Shortcuts](#keyboard-shortcuts)
8. [Tips and Tricks](#tips-and-tricks)
9. [Troubleshooting](#troubleshooting)

## Getting Started

### First Launch

1. Run the application: `python main.py`
2. You'll see the main window with:
   - A blank canvas in the center
   - Layers panel on the right
   - Tools panel on the left
   - Menu bar at the top
   - Toolbar below the menu

### Creating Your First Project

1. **Option 1: Start from scratch**
   - Click `File > New` or press `Ctrl+N`
   - Enter width and height (e.g., 800x600)
   - Click OK

2. **Option 2: Open an existing image**
   - Click `File > Open Image` or press `Ctrl+O`
   - Browse and select an image
   - The image will load as the background layer

## Interface Overview

### Main Components

#### Canvas
- Central area where you view and edit your image
- **Checkerboard** background shows transparent areas
- Drawing applies to the **currently selected layer** in the Layers panel
- Click and drag to draw (brush/eraser) or click once with **Eyedropper** to pick a color
- **Ctrl + mouse wheel** over the canvas to zoom in or out
- Scroll (without Ctrl) to pan when zoomed in

#### Layers Panel (Right Side)
- Shows all layers in your project (top to bottom)
- Each layer displays a thumbnail; **double-click a layer name** to rename it
- The **selected layer** is the one you draw on; click a layer to select it
- Controls:
  - `+` button: Add new layer
  - `-` button: Remove selected layer
  - `↑` button: Move layer up in stack
  - `↓` button: Move layer down in stack
  - Opacity slider: Adjust layer transparency
  - Visible checkbox: Show/hide layer

#### Tools Panel (Left Side)
- **Tool Selection**: Brush, Eraser, or **Eyedropper** (pick color from canvas)
- **Brush Size**: 1-200 pixels
- **Brush Opacity**: 0-100%
- **Color Picker**: Click to choose a color (Eyedropper updates this on click)

#### Menu Bar
- **File**: New, Open, Save, etc.
- **Edit**: Undo, Redo, Clear Layer, Fill
- **Layer**: Layer operations, Remove last filter from layer
- **Filter**: Image filters and adjustments, Remove last filter
- **Image**: Flip, Rotate, Resize, Crop, Make color transparent
- **View**: Zoom controls, **Transparency display** (checkerboard / white / gray / black)
- **Help**: About dialog

#### Status Bar (Bottom)
- Shows **zoom percentage**, canvas **dimensions**, and **cursor position** (when over the canvas)

#### Toolbar
- Quick access to common actions
- New, Open, Save, Undo, Redo

## Working with Projects

### Unsaved Changes
- When you have unsaved changes, the app will ask **Save / Discard / Cancel** before opening a new file, opening another project, or closing the window.
- Use **Save Image** or **Save Project** to clear the unsaved state.

### Creating a New Project

1. `File > New` (Ctrl+N)
2. Enter dimensions:
   - Common sizes: 800x600, 1920x1080, 3000x2000
   - Maximum: 10000x10000 (may be slow)
3. A white background layer is created automatically

### Opening Images

**Supported formats**: PNG, JPG, JPEG, BMP, GIF

1. `File > Open Image` (Ctrl+O)
2. Select your image
3. The image becomes the background layer
4. Canvas size matches image dimensions

### Saving Your Work

#### Save as Image
- `File > Save Image` (Ctrl+S)
- Exports the final composited image
- Formats: PNG (with transparency) or JPG
- **Note**: This flattens all layers

#### Save as Project
- `File > Save Project` (Ctrl+Shift+S)
- Saves as `.iep` file (Image Editor Pro format)
- Preserves all layers, opacity, visibility
- Can be reopened later with `File > Open Project`

## Layer Management

### Understanding Layers

Layers are like transparent sheets stacked on top of each other:
- Bottom layer is shown first
- Top layers appear in front
- Transparent areas let lower layers show through

### Basic Layer Operations

#### Adding a Layer
1. Click `+` button in Layers panel
2. Or use `Layer > New Layer` (Ctrl+Shift+N)
3. Enter a name for your layer
4. New layer is created on top

#### Removing a Layer
1. Select the layer to remove
2. Click `-` button
3. **Note**: You cannot remove the last layer

#### Reordering Layers
1. Select a layer
2. Use `↑` to move it up (forward)
3. Use `↓` to move it down (backward)

### Layer Properties

#### Opacity
- Controls layer transparency
- 100% = fully opaque
- 0% = fully transparent (invisible)
- Use the slider in Layers panel

#### Visibility
- Toggle with the "Visible" checkbox
- Hidden layers don't appear in final image
- Useful for comparing changes

### Advanced Layer Operations

#### Duplicate Layer
- `Layer > Duplicate Layer` (Ctrl+J)
- Creates an exact copy of selected layer
- New layer appears on top

#### Merge Down
- `Layer > Merge Down` (Ctrl+E)
- Combines selected layer with layer below
- Cannot be undone after saving
- Reduces layer count and file size

## Drawing and Painting

### Selecting a Tool

1. In the Tools panel, click:
   - **Brush**: For drawing
   - **Eraser**: For erasing

### Brush Settings

#### Size
- Range: 1-200 pixels
- Adjust with slider or type exact value
- Larger brushes for broad strokes
- Smaller brushes for details

#### Opacity
- Range: 0-100%
- Controls brush transparency
- Lower opacity for subtle effects
- 100% for solid color

#### Color
1. Click "Choose Color" button
2. Select color from picker dialog
3. Or enter RGB values
4. Color display shows current selection

### Drawing Technique

1. **Click and drag** to draw
2. **Release** to complete stroke
3. Each stroke is a separate action (can undo individually)

**Tips:**
- Draw slowly for smooth lines
- Use lower opacity for blending
- Zoom in for precise work
- Use layers to separate elements

### Using the Eraser

1. Select Eraser tool
2. Adjust size as needed
3. Click and drag to erase
4. **Note**: Eraser makes pixels transparent (not white)

## Applying Filters

### Basic Filters (No Parameters)

#### Grayscale
- `Filter > Grayscale`
- Converts to black and white
- Preserves transparency

#### Invert
- `Filter > Invert`
- Inverts all colors
- Black becomes white, red becomes cyan, etc.

#### Edge Detect
- `Filter > Edge Detect`
- Highlights edges in the image
- Good for artistic effects

### Adjustable Filters

#### Blur
- `Filter > Blur`
- **Radius**: 1-50 (higher = more blur)
- Use for:
  - Softening images
  - Creating depth of field
  - Reducing noise

#### Sharpen
- `Filter > Sharpen`
- **Factor**: 100-500% (higher = sharper)
- Use for:
  - Enhancing details
  - Correcting soft focus
  - Emphasizing textures

#### Brightness
- `Filter > Brightness`
- **Factor**: 0-300%
  - 100% = no change
  - <100% = darker
  - >100% = brighter

#### Contrast
- `Filter > Contrast`
- **Factor**: 0-300%
  - 100% = no change
  - <100% = less contrast
  - >100% = more contrast

#### Hue/Saturation
- `Filter > Hue/Saturation`
- **Hue Shift**: -180 to +180 degrees
  - Changes colors (red to green, etc.)
- **Saturation**: 0-300%
  - 0% = grayscale
  - 100% = no change
  - >100% = more vibrant

### Filter Tips

1. **Work on a duplicate layer** (Ctrl+J) to preserve original
2. **Adjust opacity** of filtered layer to blend with original
3. **Use filters in sequence** for complex effects
4. **Undo if needed** (Ctrl+Z)

## Keyboard Shortcuts

### File Operations
- `Ctrl+N`: New project
- `Ctrl+O`: Open image
- `Ctrl+S`: Save image
- `Ctrl+Shift+O`: Open project
- `Ctrl+Shift+S`: Save project
- `Ctrl+Q`: Quit

### Edit
- `Ctrl+Z`: Undo
- `Ctrl+Y` or `Ctrl+Shift+Z`: Redo

### Layer
- `Ctrl+Shift+N`: New layer
- `Ctrl+J`: Duplicate layer
- `Ctrl+E`: Merge down

### View
- `Ctrl++`: Zoom in
- `Ctrl+-`: Zoom out
- `Ctrl+0`: Reset zoom to 100%
- `Ctrl+1`: Fit to window (zoom so the whole image fits)
- **Ctrl + mouse wheel** over canvas: zoom in/out

## Tips and Tricks

### Organization
- Name your layers descriptively
- Use layers to separate different elements
- Keep a backup of original image in bottom layer

### Workflow
1. Start with background layer
2. Add new layers for each element
3. Adjust layer order as needed
4. Use opacity for blending
5. Merge layers when satisfied
6. Apply filters last

### Performance
- Large images (>5000x5000) may be slow
- More layers = more memory usage
- Merge layers you're done with
- Save projects regularly

### Quality
- Work at higher resolution than final output
- Use PNG for images with transparency
- Use JPG for photographs (smaller file size)
- Avoid too many undo/redo operations (limited to 50)

## Troubleshooting

### Application Won't Start
- Check Python version (3.8+)
- Verify dependencies installed: `pip install -r requirements.txt`
- Try running from terminal to see error messages

### Slow Performance
- Reduce canvas size
- Merge unnecessary layers
- Close other applications
- Use smaller brush sizes

### Can't See My Edits
- Check if layer is visible (checkbox)
- Check layer opacity (should be >0%)
- Check if you're on the right layer
- Try zooming to 100% (Ctrl+0)

### Undo Not Working
- History limited to 50 operations
- Some operations can't be undone (e.g., merge)
- Save frequently to prevent data loss

### File Won't Save
- Check disk space
- Verify write permissions
- Try different file format
- Close other programs using the file

### Filters Look Wrong
- Make sure you selected the right layer
- Check layer opacity
- Try adjusting filter parameters
- Undo (Ctrl+Z) and try again

---

For more help, please visit the GitHub repository or open an issue.
