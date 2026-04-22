"""Grayscale filter — the reference implementation."""

from PIL import Image

from .base import Filter


class GrayscaleFilter(Filter):
    """Convert an image to grayscale (luminance-based)."""

    name = "grayscale"

    def apply(self, img: Image.Image, **kwargs) -> Image.Image:
        return img.convert("L")
