"""Tests for the grayscale filter — reference test, copy this pattern for new filters."""

from PIL import Image

from photokit.filters.grayscale import GrayscaleFilter


def test_grayscale_converts_to_l_mode():
    img = Image.new("RGB", (10, 10), color="red")
    out = GrayscaleFilter().apply(img)
    assert out.mode == "L"


def test_grayscale_preserves_size():
    img = Image.new("RGB", (50, 30))
    out = GrayscaleFilter().apply(img)
    assert out.size == (50, 30)


def test_grayscale_registered():
    from photokit.registry import FILTERS

    assert "grayscale" in FILTERS
