"""Unit tests for image filters in src/filters.py.

Validates that every filter returns a valid PIL Image, preserves or correctly
changes dimensions/mode, and does not crash on small dummy images.
"""

import pytest
from PIL import Image

from src.filters import Filters


# Small dummy image for fast tests (100x100 RGBA)
@pytest.fixture
def sample_rgba():
    """100x100 RGBA image with simple gradient-like data."""
    w, h = 100, 100
    img = Image.new("RGBA", (w, h), (128, 64, 200, 255))
    # Add some variation so filters have something to work on
    pixels = img.load()
    for x in range(w):
        for y in range(h):
            pixels[x, y] = ((x + y) % 256, (x * 2) % 256, (y * 2) % 256, 255)
    return img


@pytest.fixture
def sample_rgb():
    """100x100 RGB image."""
    w, h = 100, 100
    img = Image.new("RGB", (w, h), (100, 150, 200))
    pixels = img.load()
    for x in range(w):
        for y in range(h):
            pixels[x, y] = ((x + y) % 256, (x * 2) % 256, (y * 2) % 256)
    return img


def test_blur_returns_image(sample_rgba):
    out = Filters.blur(sample_rgba, radius=2)
    assert isinstance(out, Image.Image)
    assert out.size == sample_rgba.size
    assert out.mode == sample_rgba.mode


def test_blur_valid_radius(sample_rgba):
    out = Filters.blur(sample_rgba, radius=5)
    assert out.size == (100, 100)
    assert out.mode == "RGBA"


def test_sharpen_returns_image(sample_rgba):
    out = Filters.sharpen(sample_rgba, factor=1.5)
    assert isinstance(out, Image.Image)
    assert out.size == sample_rgba.size
    assert out.mode == sample_rgba.mode


def test_adjust_brightness_returns_image(sample_rgba):
    out = Filters.adjust_brightness(sample_rgba, factor=1.2)
    assert isinstance(out, Image.Image)
    assert out.size == sample_rgba.size
    assert out.mode == sample_rgba.mode


def test_adjust_contrast_returns_image(sample_rgba):
    out = Filters.adjust_contrast(sample_rgba, factor=1.3)
    assert isinstance(out, Image.Image)
    assert out.size == sample_rgba.size
    assert out.mode == sample_rgba.mode


def test_adjust_hue_saturation_returns_image(sample_rgba):
    out = Filters.adjust_hue_saturation(sample_rgba, hue_shift=30, saturation=1.0)
    assert isinstance(out, Image.Image)
    assert out.size == sample_rgba.size
    assert out.mode == sample_rgba.mode


def test_desaturate_returns_image(sample_rgba):
    out = Filters.desaturate(sample_rgba)
    assert isinstance(out, Image.Image)
    assert out.size == sample_rgba.size


def test_grayscale_returns_image_and_mode(sample_rgba, sample_rgb):
    # Grayscale on RGBA returns RGBA (gray channels + original alpha)
    out_rgba = Filters.grayscale(sample_rgba)
    assert isinstance(out_rgba, Image.Image)
    assert out_rgba.size == sample_rgba.size
    assert out_rgba.mode == "RGBA"
    # Grayscale on RGB returns RGB (L then converted to RGB)
    out_rgb = Filters.grayscale(sample_rgb)
    assert out_rgb.size == sample_rgb.size
    assert out_rgb.mode == "RGB"


def test_invert_returns_image_and_mode(sample_rgba, sample_rgb):
    out_rgba = Filters.invert(sample_rgba)
    assert isinstance(out_rgba, Image.Image)
    assert out_rgba.size == sample_rgba.size
    assert out_rgba.mode == "RGBA"
    out_rgb = Filters.invert(sample_rgb)
    assert out_rgb.size == sample_rgb.size
    assert out_rgb.mode == "RGB"


def test_edge_detect_returns_image(sample_rgba):
    out = Filters.edge_detect(sample_rgba)
    assert isinstance(out, Image.Image)
    assert out.size == sample_rgba.size
    assert out.mode == sample_rgba.mode


def test_sepia_returns_image(sample_rgba):
    out = Filters.sepia(sample_rgba)
    assert isinstance(out, Image.Image)
    assert out.size == sample_rgba.size
    assert out.mode == sample_rgba.mode


def test_posterize_returns_image(sample_rgba):
    out = Filters.posterize(sample_rgba, bits=4)
    assert isinstance(out, Image.Image)
    assert out.size == sample_rgba.size
    assert out.mode == sample_rgba.mode


def test_make_color_transparent_returns_rgba(sample_rgba):
    out = Filters.make_color_transparent(sample_rgba, 128, 64, 200, tolerance=30)
    assert isinstance(out, Image.Image)
    assert out.size == sample_rgba.size
    assert out.mode == "RGBA"


def test_emboss_returns_image(sample_rgba):
    out = Filters.emboss(sample_rgba)
    assert isinstance(out, Image.Image)
    assert out.size == sample_rgba.size


def test_smooth_returns_image(sample_rgba):
    out = Filters.smooth(sample_rgba)
    assert isinstance(out, Image.Image)
    assert out.size == sample_rgba.size


def test_detail_returns_image(sample_rgba):
    out = Filters.detail(sample_rgba)
    assert isinstance(out, Image.Image)
    assert out.size == sample_rgba.size


def test_filters_do_not_modify_input(sample_rgba):
    """Ensure filters do not mutate the input image in place."""
    from copy import deepcopy
    # We can't deepcopy a PIL Image easily; compare size/mode and a pixel
    w, h = sample_rgba.size
    before_pixel = sample_rgba.getpixel((0, 0))
    _ = Filters.blur(sample_rgba, radius=1)
    _ = Filters.sharpen(sample_rgba, factor=1.0)
    assert sample_rgba.size == (w, h)
    assert sample_rgba.getpixel((0, 0)) == before_pixel
