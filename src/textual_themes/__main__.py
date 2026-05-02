"""CLI entry point: ``python -m textual_themes``.

Launches the storybook demo app. Optionally pre-selects a theme.
"""
from __future__ import annotations

import argparse
import sys

from . import __version__
from .demo import ThemeDemoApp
from .themes import RETRO_THEME_NAMES, THEME_DISPLAY_NAMES


def main() -> None:
    try:
        sys.stdout.reconfigure(encoding="utf-8")  # type: ignore[attr-defined]
    except Exception:
        pass
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

    ThemeDemoApp(initial_theme=args.theme).run()


if __name__ == "__main__":
    main()
