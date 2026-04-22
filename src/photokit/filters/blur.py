from PIL import Image, ImageFilter
from .base import Filter


class BlurFilter(Filter):
    name = "blur"

    def apply(self, img: Image.Image, **kwargs) -> Image.Image:
        radius = kwargs.get("radius", 2)
        return img.filter(ImageFilter.GaussianBlur(radius=radius))