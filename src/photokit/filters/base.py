"""Base class for all filters."""

from abc import ABC, abstractmethod

from PIL import Image


class Filter(ABC):
    """Abstract base class for image filters.

    Every concrete filter must:
      - set a `name` class attribute (used by the registry / CLI)
      - implement `apply(img, **kwargs) -> Image.Image`
    """

    name: str

    @abstractmethod
    def apply(self, img: Image.Image, **kwargs) -> Image.Image:
        """Apply the filter to the given image and return a new image."""
        ...
