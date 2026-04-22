from PIL import Image
from .base import Filter


class SepiaFilter(Filter):
    name = "sepia"

    def apply(self, img: Image.Image, **kwargs) -> Image.Image:
        img = img.convert("RGB")
        pixels = img.load()
        width, height = img.size
        for py in range(height):
            for px in range(width):
                r, g, b = pixels[px, py]
                tr = int(0.393 * r + 0.769 * g + 0.189 * b)
                tg = int(0.349 * r + 0.686 * g + 0.168 * b)
                tb = int(0.272 * r + 0.534 * g + 0.131 * b)
                pixels[px, py] = (min(255, tr), min(255, tg), min(255, tb))
        return img