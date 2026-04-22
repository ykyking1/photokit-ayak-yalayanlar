"""Command-line interface for PhotoKit."""

import click
from PIL import Image
from rich.console import Console

from .registry import FILTERS, get_filter

console = Console()


@click.group()
@click.version_option()
def main() -> None:
    """PhotoKit — apply filters to images from the command line."""
    pass


@main.command("list")
def list_filters() -> None:
    """List all available filters."""
    console.print("[bold cyan]Available filters:[/]")
    for name in FILTERS:
        console.print(f"  - {name}")


@main.command()
@click.argument("name")
@click.argument("input_path", type=click.Path(exists=True, dir_okay=False))
@click.argument("output_path", type=click.Path(dir_okay=False))
@click.option("--radius", type=int, default=2, help="Blur radius (for blur filter)")
@click.option("--width", type=int, default=800, help="Target width (for resize filter)")
def apply(name: str, input_path: str, output_path: str, radius: int, width: int) -> None:
    """Apply a filter to an image."""
    try:
        img = Image.open(input_path)
        flt = get_filter(name)
        out = flt.apply(img, radius=radius, width=width)
        out.save(output_path)
        console.print(f"[green]\u2713[/] {name} applied \u2192 {output_path}")
    except ValueError as e:
        console.print(f"[red]Error:[/] {e}")
        raise SystemExit(1)
    except FileNotFoundError as e:
        console.print(f"[red]File not found:[/] {e}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
