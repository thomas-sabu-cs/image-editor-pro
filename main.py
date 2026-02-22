#!/usr/bin/env python3
"""Image Editor Pro - Main entry point.

A professional desktop image editing application built with PyQt6.

Usage:
    python main.py
"""

import sys
import os
import logging

# Add src directory to path
_script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_script_dir, 'src'))

# Logging: write to app.log for debugging user issues
_log_path = os.path.join(_script_dir, "app.log")
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(_log_path, encoding="utf-8"),
        logging.StreamHandler(sys.stderr),
    ],
)
logger = logging.getLogger("ImageEditorPro")


def main():
    """Main entry point for the application."""
    logger.info("Starting Image Editor Pro")
    try:
        from PyQt6.QtWidgets import QApplication
        from main_window import MainWindow
    except Exception as e:
        logger.exception("Failed to import application: %s", e)
        raise

    # Create application
    app = QApplication(sys.argv)
    app.setApplicationName("Image Editor Pro")
    app.setOrganizationName("ImageEditorPro")
    
    # Set application style
    app.setStyle("Fusion")
    
    # Optional: Set dark theme
    # Uncomment the following lines for a dark theme
    """
    palette = QPalette()
    palette.setColor(QPalette.ColorRole.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.WindowText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.ColorRole.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ToolTipBase, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.ToolTipText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Text, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ColorRole.ButtonText, Qt.GlobalColor.white)
    palette.setColor(QPalette.ColorRole.BrightText, Qt.GlobalColor.red)
    palette.setColor(QPalette.ColorRole.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.ColorRole.HighlightedText, Qt.GlobalColor.black)
    app.setPalette(palette)
    """
    
    # Create and show main window
    try:
        window = MainWindow()
        window.show()
        logger.info("Main window shown")
        exit_code = app.exec()
        logger.info("Application exiting with code %s", exit_code)
        sys.exit(exit_code)
    except Exception as e:
        logger.exception("Unhandled error: %s", e)
        raise


if __name__ == '__main__':
    main()
