"""Application-wide Qt style sheets (QSS) for a consistent dark theme.

VS Code / dark Photoshop-like appearance for menus, docks, toolbar, and controls.
"""

# Dark theme palette (hex)
# Backgrounds
BG_WINDOW = "#1e1e1e"
BG_DOCK = "#252526"
BG_TOOLBAR = "#2d2d2d"
BG_MENU = "#252526"
BG_MENU_HOVER = "#094771"
BG_INPUT = "#3c3c3c"
BG_BUTTON = "#0e639c"
BG_BUTTON_HOVER = "#1177bb"
BG_BUTTON_PRESSED = "#094771"
# Text
FG_PRIMARY = "#cccccc"
FG_SECONDARY = "#9d9d9d"
FG_DISABLED = "#6d6d6d"
# Borders
BORDER_SUBTLE = "#3c3c3c"
BORDER_FOCUS = "#007acc"
# Scrollbar
SCROLLBAR_BG = "#1e1e1e"
SCROLLBAR_HANDLE = "#424242"
SCROLLBAR_HANDLE_HOVER = "#4e4e4e"

DARK_THEME_QSS = f"""
/* Global */
QWidget {{
    background-color: {BG_WINDOW};
    color: {FG_PRIMARY};
}}

/* Main window and central area */
QMainWindow {{
    background-color: {BG_WINDOW};
}}

/* Menu bar */
QMenuBar {{
    background-color: {BG_DOCK};
    color: {FG_PRIMARY};
    border-bottom: 1px solid {BORDER_SUBTLE};
    padding: 2px 0;
}}
QMenuBar::item {{
    padding: 4px 12px;
    border-radius: 2px;
}}
QMenuBar::item:selected {{
    background-color: {BG_MENU_HOVER};
}}
QMenuBar::item:pressed {{
    background-color: {BG_BUTTON_PRESSED};
}}

/* Menus */
QMenu {{
    background-color: {BG_MENU};
    color: {FG_PRIMARY};
    border: 1px solid {BORDER_SUBTLE};
}}
QMenu::item {{
    padding: 6px 24px 6px 12px;
}}
QMenu::item:selected {{
    background-color: {BG_MENU_HOVER};
}}
QMenu::separator {{
    height: 1px;
    background-color: {BORDER_SUBTLE};
}}

/* Toolbar */
QToolBar {{
    background-color: {BG_TOOLBAR};
    border: none;
    border-bottom: 1px solid {BORDER_SUBTLE};
    spacing: 4px;
    padding: 4px;
}}
QToolBar::separator {{
    width: 1px;
    background-color: {BORDER_SUBTLE};
    margin: 4px 6px;
}}

/* Dock widgets */
QDockWidget {{
    background-color: {BG_DOCK};
    color: {FG_PRIMARY};
    titlebar-close-icon: none;
    titlebar-normal-icon: none;
}}
QDockWidget::title {{
    background-color: {BG_DOCK};
    color: {FG_PRIMARY};
    padding: 6px 8px;
    border: none;
    font-weight: bold;
}}
QDockWidget::close-button, QDockWidget::float-button {{
    background: transparent;
    border: none;
}}

/* Status bar */
QStatusBar {{
    background-color: {BG_DOCK};
    color: {FG_SECONDARY};
    border-top: 1px solid {BORDER_SUBTLE};
}}

/* Buttons */
QPushButton {{
    background-color: {BG_INPUT};
    color: {FG_PRIMARY};
    border: 1px solid {BORDER_SUBTLE};
    border-radius: 4px;
    padding: 6px 12px;
    min-width: 60px;
}}
QPushButton:hover {{
    background-color: {BG_MENU_HOVER};
    border-color: {BORDER_FOCUS};
}}
QPushButton:pressed {{
    background-color: {BG_BUTTON_PRESSED};
}}
QPushButton:disabled {{
    color: {FG_DISABLED};
    background-color: #2d2d2d;
}}

/* Spin boxes and combo boxes */
QSpinBox, QComboBox {{
    background-color: {BG_INPUT};
    color: {FG_PRIMARY};
    border: 1px solid {BORDER_SUBTLE};
    border-radius: 4px;
    padding: 4px 8px;
    min-height: 20px;
}}
QSpinBox:focus, QComboBox:focus {{
    border-color: {BORDER_FOCUS};
}}
QSpinBox::up-button, QSpinBox::down-button {{
    background-color: #2d2d2d;
    border: none;
}}
QComboBox::drop-down {{
    border: none;
    background: transparent;
}}
QComboBox QAbstractItemView {{
    background-color: {BG_MENU};
}}

/* Line edits */
QLineEdit {{
    background-color: {BG_INPUT};
    color: {FG_PRIMARY};
    border: 1px solid {BORDER_SUBTLE};
    border-radius: 4px;
    padding: 4px 8px;
}}
QLineEdit:focus {{
    border-color: {BORDER_FOCUS};
}}

/* Labels */
QLabel {{
    color: {FG_PRIMARY};
}}

/* Sliders */
QSlider::groove:horizontal {{
    background: {BORDER_SUBTLE};
    height: 6px;
    border-radius: 3px;
}}
QSlider::handle:horizontal {{
    background: {BORDER_FOCUS};
    width: 14px;
    margin: -4px 0;
    border-radius: 7px;
}}
QSlider::handle:horizontal:hover {{
    background: {BG_BUTTON_HOVER};
}}

/* Scroll area (for canvas, panels) */
QScrollArea {{
    background-color: {BG_WINDOW};
    border: none;
}}
QScrollBar:vertical {{
    background: {SCROLLBAR_BG};
    width: 12px;
    border-radius: 6px;
    margin: 0;
}}
QScrollBar::handle:vertical {{
    background: {SCROLLBAR_HANDLE};
    min-height: 24px;
    border-radius: 6px;
}}
QScrollBar::handle:vertical:hover {{
    background: {SCROLLBAR_HANDLE_HOVER};
}}
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
    height: 0;
}}

/* Tab widget (if used) */
QTabWidget::pane {{
    background-color: {BG_DOCK};
    border: 1px solid {BORDER_SUBTLE};
}}
QTabBar::tab {{
    background-color: {BG_TOOLBAR};
    color: {FG_PRIMARY};
    padding: 8px 16px;
}}
QTabBar::tab:selected {{
    background-color: {BG_DOCK};
}}

/* Dialog */
QDialog {{
    background-color: {BG_WINDOW};
}}
QDialogButtonBox QPushButton {{
    min-width: 80px;
}}

/* Form layout labels */
QFormLayout QLabel {{
    color: {FG_SECONDARY};
}}

/* List widget (e.g. layer list) */
QListWidget {{
    background-color: {BG_DOCK};
    color: {FG_PRIMARY};
    border: none;
}}
QListWidget::item {{
    padding: 4px 8px;
}}
QListWidget::item:selected {{
    background-color: {BG_MENU_HOVER};
}}
QListWidget::item:hover {{
    background-color: #2a2d2e;
}}

/* Group box */
QGroupBox {{
    color: {FG_PRIMARY};
    border: 1px solid {BORDER_SUBTLE};
    border-radius: 4px;
    margin-top: 8px;
}}
QGroupBox::title {{
    subcontrol-origin: margin;
    left: 8px;
    padding: 0 4px;
}}
"""
