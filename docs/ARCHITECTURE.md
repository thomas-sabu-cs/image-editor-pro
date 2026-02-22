# Architecture Documentation

## Overview

Image Editor Pro is built using a modular, object-oriented architecture that follows the Model-View-Controller (MVC) pattern with additional design patterns for specific features.

## Design Patterns

### 1. Model-View-Controller (MVC)

**Models:**
- `Layer`: Represents a single image layer
- `Project`: Manages multiple layers and project settings

**Views:**
- `Canvas`: Displays and allows interaction with the image
- `LayerPanel`: Displays layer list and controls
- `ToolOptionsPanel`: Displays tool settings

**Controller:**
- `MainWindow`: Coordinates between models and views
- Handles user actions from menus and toolbars
- Routes signals between components

### 2. Command Pattern

Implemented for undo/redo functionality:

```python
Command (Abstract)
├── DrawCommand
├── AddLayerCommand
├── RemoveLayerCommand
├── MoveLayerCommand
├── SetLayerOpacityCommand
├── SetLayerVisibilityCommand
└── FilterCommand
```

**Benefits:**
- Encapsulates actions as objects
- Easy to undo/redo
- History management
- Extensible for new operations

### 3. Strategy Pattern

Used for image filters:
- Each filter is a separate method in the `Filters` class
- Easy to add new filters without modifying existing code
- Filters are stateless and reusable

### 4. Observer Pattern

Implemented through Qt's signals and slots:
- Components communicate without tight coupling
- `Project` emits signals when layers change
- UI components update automatically

## Component Details

### Models (`models.py`)

#### Layer Class
```python
Layer:
- Properties: name, image, visible, opacity
- Methods: get_size(), resize(), get_thumbnail(), copy()
- Serialization: to_dict(), from_dict()
```

#### Project Class
```python
Project:
- Properties: width, height, layers, file_path
- Methods: add_layer(), remove_layer(), move_layer(), render()
- Signals: layers_changed, layer_modified
- Serialization: save_project(), load_project()
```

### Commands (`commands.py`)

#### Command Interface
```python
Command:
- execute(): Perform the action
- undo(): Reverse the action
- get_name(): Return command name for UI
```

#### CommandHistory
```python
CommandHistory:
- undo_stack: List of commands that can be undone
- redo_stack: List of commands that can be redone
- execute(): Execute and add to history
- undo(): Undo last command
- redo(): Redo last undone command
```

### Filters (`filters.py`)

All filters are static methods that:
1. Take a PIL Image as input
2. Return a new PIL Image (immutable)
3. Accept parameters for customization

### Canvas (`canvas.py`)

#### Canvas Class
```python
Canvas:
- Rendering: Displays composited image
- Interaction: Handles mouse events for drawing
- Tools: Brush, eraser
- Signals: drawing_completed
```

#### CanvasScrollArea
```python
CanvasScrollArea:
- Zoom: zoom_in(), zoom_out(), zoom_reset()
- Scrolling: Automatic scroll bars
```

### Panels (`panels.py`)

#### LayerPanel
```python
LayerPanel:
- Display: Layer list with thumbnails
- Controls: Add, remove, move, opacity, visibility
- Signals: layer_selected, add_layer_requested, etc.
```

#### ToolOptionsPanel
```python
ToolOptionsPanel:
- Tool selection: Brush, eraser
- Settings: Size, opacity, color
- Signals: tool_changed, brush_size_changed, etc.
```

### Main Window (`main_window.py`)

```python
MainWindow:
- Menu bar: File, Edit, Layer, Filter, View, Help
- Toolbar: Quick access to common actions
- Dock widgets: Panels for layers and tools
- Central widget: Canvas scroll area
- Signal routing: Connects all components
```

## Data Flow

### Opening an Image
1. User clicks File > Open
2. MainWindow opens file dialog
3. PIL loads the image
4. New Project created with image dimensions
5. Image set as background layer
6. Canvas and panels updated
7. Signals reconnected

### Drawing
1. User selects brush tool and settings
2. User clicks and drags on canvas
3. Canvas captures mouse events
4. Canvas draws on active layer's image
5. On mouse release, drawing_completed signal emitted
6. MainWindow creates DrawCommand
7. Command executed and added to history
8. Canvas updates to show changes

### Applying a Filter
1. User selects layer
2. User chooses filter from menu
3. Filter dialog shown (if parameters needed)
4. MainWindow applies filter to layer's image
5. FilterCommand created with old and new images
6. Command executed and added to history
7. Layer updated and canvas refreshes

### Undo/Redo
1. User presses Ctrl+Z (undo) or Ctrl+Y (redo)
2. CommandHistory pops command from appropriate stack
3. Command's undo() or execute() method called
4. Model updated
5. Signals emitted
6. UI refreshes

## Extension Points

### Adding a New Tool
1. Add tool to ToolOptionsPanel
2. Extend Canvas mouse event handlers
3. Create command for tool's actions
4. Update MainWindow to handle new tool

### Adding a New Filter
1. Add filter method to Filters class
2. Add menu action in MainWindow
3. Create FilterDialog for parameters (if needed)
4. Filter automatically works with undo/redo

### Adding a New Panel
1. Create panel widget (inherit from QWidget)
2. Add signals for user actions
3. Create dock widget in MainWindow
4. Connect signals to MainWindow handlers

## Performance Considerations

1. **Image Copying**: Commands store copies of images for undo/redo
   - Tradeoff: Memory vs functionality
   - Limited by history size (default 50)

2. **Rendering**: Project renders all visible layers on each update
   - Optimizations: Only re-render when needed
   - Future: Cache rendered image

3. **Drawing**: Direct drawing on PIL images
   - Fast for most use cases
   - May be slow for very large brushes

4. **Filters**: NumPy used for efficient array operations
   - Most filters are fast
   - Complex filters (hue/saturation) may be slower

## Dependencies

- **PyQt6**: GUI framework, widgets, signals/slots
- **Pillow (PIL)**: Image loading, saving, basic operations
- **NumPy**: Efficient array operations for filters

## Future Improvements

1. **Performance**:
   - Cache rendered image
   - Lazy layer updates
   - Multi-threading for filters

2. **Architecture**:
   - Plugin system for filters and tools
   - Separate rendering engine
   - Layer effects pipeline

3. **Features**:
   - Selection system
   - Layer masks
   - Adjustment layers
   - Non-destructive editing
