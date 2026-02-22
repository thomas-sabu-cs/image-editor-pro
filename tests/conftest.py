"""Pytest configuration and fixtures for Image Editor Pro tests.

Ensures the project root is on sys.path and optionally initializes Qt
for tests that use PyQt6 (e.g. CommandHistory, Project with signals).
"""

import sys
from pathlib import Path

# Add project root so "from src.xxx" works when running pytest from project root
_root = Path(__file__).resolve().parent.parent
if str(_root) not in sys.path:
    sys.path.insert(0, str(_root))


def pytest_configure(config):
    """Create QApplication once for Qt-dependent tests (commands, models)."""
    try:
        from PyQt6.QtWidgets import QApplication
        app = QApplication.instance()
        if app is None:
            QApplication(sys.argv)
    except Exception:
        pass
