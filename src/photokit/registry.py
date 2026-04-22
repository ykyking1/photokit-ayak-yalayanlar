from .filters.base import Filter
from .filters.grayscale import GrayscaleFilter
from .filters.blur import BlurFilter  # <-- YENI IMPORT

FILTERS: dict[str, type[Filter]] = {
    "grayscale": GrayscaleFilter,
    "blur": BlurFilter,  # <-- YENI KAYIT
}


def get_filter(name: str) -> Filter:
    if name not in FILTERS:
        available = ", ".join(FILTERS.keys())
        raise ValueError(f"Unknown filter: {name!r}. Available: {available}")
    return FILTERS[name]()