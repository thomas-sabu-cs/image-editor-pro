#!/usr/bin/env python3
"""Basic functionality test for Image Editor Pro."""

import sys
import os
import tempfile

# Allow running from project root or from this file's directory
_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_root, 'src'))

from models import Layer, Project
from commands import CommandHistory, AddLayerCommand, DrawCommand
from filters import Filters
from PIL import Image
import numpy as np

def test_layer():
    """Test Layer class."""
    print("Testing Layer class...")
    layer = Layer("Test Layer", 100, 100)
    assert layer.name == "Test Layer"
    assert layer.get_size() == (100, 100)
    assert layer.visible == True
    assert layer.opacity == 100
    print("OK Layer class works correctly")

def test_project():
    """Test Project class."""
    print("Testing Project class...")
    project = Project(200, 150)
    assert project.width == 200
    assert project.height == 150
    assert len(project.layers) == 1  # Background layer
    
    # Add layer
    layer = project.add_layer("New Layer")
    assert len(project.layers) == 2
    assert layer.name == "New Layer"
    
    # Remove layer
    project.remove_layer(1)
    assert len(project.layers) == 1
    
    # Render
    rendered = project.render()
    assert rendered.size == (200, 150)
    print("OK Project class works correctly")

def test_filters():
    """Test filter functions."""
    print("Testing Filters...")
    # Create test image
    img = Image.new('RGBA', (100, 100), (255, 0, 0, 255))
    
    # Test blur
    blurred = Filters.blur(img, radius=2)
    assert blurred.size == img.size
    
    # Test sharpen
    sharpened = Filters.sharpen(img, factor=1.5)
    assert sharpened.size == img.size
    
    # Test brightness
    brighter = Filters.adjust_brightness(img, factor=1.5)
    assert brighter.size == img.size
    
    # Test contrast
    contrasted = Filters.adjust_contrast(img, factor=1.5)
    assert contrasted.size == img.size
    
    # Test grayscale
    gray = Filters.grayscale(img)
    assert gray.size == img.size
    
    # Test invert
    inverted = Filters.invert(img)
    assert inverted.size == img.size
    
    print("OK Filters work correctly")

def test_commands():
    """Test command pattern."""
    print("Testing Command pattern...")
    project = Project(100, 100)
    history = CommandHistory()
    
    # Test add layer command
    cmd = AddLayerCommand(project, "Test Layer")
    history.execute(cmd)
    assert len(project.layers) == 2
    
    # Test undo
    history.undo()
    assert len(project.layers) == 1
    
    # Test redo
    history.redo()
    assert len(project.layers) == 2
    
    print("OK Command pattern works correctly")

def test_save_load():
    """Test project save/load."""
    print("Testing project save/load...")
    project = Project(100, 100)
    project.add_layer("Layer 1")
    project.add_layer("Layer 2")
    
    # Use temp dir so test works on Windows and Unix
    temp_path = os.path.join(tempfile.gettempdir(), "test_project_iep.iep")
    project.save_project(temp_path)
    try:
        loaded_project = Project.load_project(temp_path)
    finally:
        try:
            os.remove(temp_path)
        except OSError:
            pass
    assert loaded_project.width == 100
    assert loaded_project.height == 100
    assert len(loaded_project.layers) == 3  # Background + 2 layers
    
    print("OK Project save/load works correctly")

def main():
    """Run all tests."""
    print("=" * 50)
    print("Image Editor Pro - Basic Functionality Tests")
    print("=" * 50)
    print()
    
    try:
        test_layer()
        test_project()
        test_filters()
        test_commands()
        test_save_load()
        
        print()
        print("=" * 50)
        print("All tests passed!")
        print("=" * 50)
        return 0
    except Exception as e:
        print()
        print("=" * 50)
        print("Tests failed!")
        print(f"Error: {e}")
        print("=" * 50)
        import traceback
        traceback.print_exc()
        return 1

if __name__ == '__main__':
    sys.exit(main())
