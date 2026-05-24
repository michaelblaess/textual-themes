"""CLI entry point: ``python -m textual_themes``.

Launches the storybook demo app. Optionally pre-selects a theme.
"""

from __future__ import annotations

import argparse
import contextlib
import sys

from textual_widgets import reset_terminal_title, set_terminal_title

# Absolute Imports, damit das Nuitka-Standalone-Kompilat funktioniert:
# Nuitka kompiliert __main__.py als Top-Level (ohne Parent-Package), dort
# scheitern relative Imports mit "attempted relative import with no known
# parent package". 'python -m textual_themes' funktioniert mit absoluten
# Imports genauso, weil das Paket dann im sys.path liegt.
from textual_themes import __version__
from textual_themes.demo import ThemeDemoApp
from textual_themes.themes import RETRO_THEME_NAMES, THEME_DISPLAY_NAMES


def main() -> None:
    with contextlib.suppress(Exception):
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    parser = argparse.ArgumentParser(
        prog="python -m textual_themes",
        description=f"textual-themes v{__version__} demo — browse all retro themes.",
    )
    parser.add_argument(
        "--theme",
        default=None,
        choices=RETRO_THEME_NAMES,
        metavar="NAME",
        help="Initial theme (default: first registered theme).",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available theme names and exit.",
    )
    args = parser.parse_args()

    if args.list:
        width = max(len(name) for name in RETRO_THEME_NAMES)
        for name in RETRO_THEME_NAMES:
            display = THEME_DISPLAY_NAMES.get(name, "")
            print(f"{name:<{width}}  {display}")
        sys.exit(0)

    # Terminal-Tab-Titel setzen - Textual macht das nicht selbst.
    set_terminal_title(f"textual-themes v{__version__}")
    try:
        app = ThemeDemoApp(initial_theme=args.theme)
        app.run()
    finally:
        reset_terminal_title()


if __name__ == "__main__":
    main()
