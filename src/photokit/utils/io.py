"""I/O helpers for loading and saving images."""

from pathlib import Path

from PIL import Image


def load_image(path: str | Path) -> Image.Image:
    """Open an image from disk."""
    return Image.open(path)


def save_image(img: Image.Image, path: str | Path) -> None:
    """Save an image to disk."""
    img.save(path)
