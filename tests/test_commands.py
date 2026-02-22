"""Unit tests for command pattern and undo/redo in src/commands.py.

Ensures that execute -> undo -> redo leaves project state consistent.
"""

import pytest
from PIL import Image

from src.models import Project
from src.commands import (
    CommandHistory,
    AddLayerCommand,
    RemoveLayerCommand,
    FilterCommand,
    DrawCommand,
    SetLayerOpacityCommand,
    ClearLayerCommand,
    ResizeProjectCommand,
)
from src.filters import Filters


@pytest.fixture
def project():
    """Fresh project 80x60 with one default layer."""
    return Project(80, 60)


@pytest.fixture
def history():
    return CommandHistory(max_history=50)


def test_command_history_undo_redo_add_layer(project, history):
    """Add layer -> undo -> redo leaves same layer count and state."""
    initial_count = len(project.layers)
    cmd = AddLayerCommand(project, "Test Layer")
    history.execute(cmd)
    assert len(project.layers) == initial_count + 1
    assert project.get_layer(initial_count).name == "Test Layer"

    history.undo()
    assert len(project.layers) == initial_count

    history.redo()
    assert len(project.layers) == initial_count + 1
    assert project.get_layer(initial_count).name == "Test Layer"


def test_command_history_undo_redo_remove_layer(project, history):
    """Remove layer -> undo -> redo leaves state consistent."""
    # Add a second layer so we can remove it
    AddLayerCommand(project, "To Remove").execute()
    assert len(project.layers) == 2
    removed_name = project.get_layer(1).name

    cmd = RemoveLayerCommand(project, 1)
    history.execute(cmd)
    assert len(project.layers) == 1

    history.undo()
    assert len(project.layers) == 2
    assert project.get_layer(1).name == removed_name

    history.redo()
    assert len(project.layers) == 1


def test_command_history_undo_redo_filter(project, history):
    """Apply filter -> undo -> redo leaves layer image consistent."""
    layer = project.get_layer(0)
    old_image = layer.image.copy()
    new_image = Filters.blur(layer.image, radius=1)
    assert new_image.size == old_image.size

    cmd = FilterCommand(project, 0, "Blur", old_image, new_image)
    history.execute(cmd)
    assert layer.image.size == old_image.size

    history.undo()
    # After undo, layer should match original
    assert layer.image.size == old_image.size

    history.redo()
    assert layer.image.size == old_image.size


def test_command_history_undo_redo_draw(project, history):
    """Draw command -> undo -> redo leaves layer image consistent."""
    layer = project.get_layer(0)
    old_image = layer.image.copy()
    new_image = old_image.copy()
    from PIL import ImageDraw
    draw = ImageDraw.Draw(new_image, "RGBA")
    draw.rectangle([10, 10, 20, 20], fill=(255, 0, 0, 255))

    cmd = DrawCommand(project, 0, old_image, new_image)
    history.execute(cmd)
    assert layer.image.getpixel((15, 15))[:3] == (255, 0, 0)

    history.undo()
    assert layer.image.getpixel((15, 15)) != (255, 0, 0, 255)

    history.redo()
    assert layer.image.getpixel((15, 15))[:3] == (255, 0, 0)


def test_command_history_undo_redo_opacity(project, history):
    """Set opacity -> undo -> redo leaves opacity consistent."""
    layer = project.get_layer(0)
    cmd = SetLayerOpacityCommand(project, 0, 100, 50)
    history.execute(cmd)
    assert project.get_layer(0).opacity == 50

    history.undo()
    assert project.get_layer(0).opacity == 100

    history.redo()
    assert project.get_layer(0).opacity == 50


def test_command_history_undo_redo_clear_layer(project, history):
    """Clear layer -> undo -> redo leaves layer content consistent."""
    layer = project.get_layer(0)
    old_image = layer.image.copy()
    cmd = ClearLayerCommand(project, 0, old_image)
    history.execute(cmd)
    assert layer.image.getpixel((0, 0))[3] == 0

    history.undo()
    assert layer.image.size == old_image.size

    history.redo()
    assert layer.image.getpixel((0, 0))[3] == 0


def test_command_history_undo_redo_resize(project, history):
    """Resize project -> undo -> redo leaves dimensions consistent."""
    w, h = project.width, project.height
    cmd = ResizeProjectCommand(project, 100, 80)
    history.execute(cmd)
    assert project.width == 100 and project.height == 80
    assert project.get_layer(0).image.size == (100, 80)

    history.undo()
    assert project.width == w and project.height == h
    assert project.get_layer(0).image.size == (w, h)

    history.redo()
    assert project.width == 100 and project.height == 80


def test_command_history_can_undo_can_redo(history, project):
    assert not history.can_undo()
    assert not history.can_redo()
    history.execute(AddLayerCommand(project, "A"))
    assert history.can_undo()
    assert not history.can_redo()
    history.undo()
    assert not history.can_undo()
    assert history.can_redo()
    history.redo()
    assert history.can_undo()
    assert not history.can_redo()


def test_command_history_clear(history, project):
    history.execute(AddLayerCommand(project, "A"))
    history.clear()
    assert not history.can_undo()
    assert not history.can_redo()


