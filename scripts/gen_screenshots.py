"""Generate the docs/screenshots/<slug>.svg gallery for every retro theme.

Runs the bundled demo app headless (Textual ``run_test``) once per theme in
``RETRO_THEMES``, applies the theme and exports an SVG screenshot. This keeps
the whole gallery visually consistent — rerun the script after adding,
removing or restyling a theme.

Usage:
    python scripts/gen_screenshots.py
    poe gen-screenshots
"""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

_REPO_ROOT = Path(__file__).resolve().parent.parent
# Prefer the in-repo source over any installed copy of the package.
sys.path.insert(0, str(_REPO_ROOT / "src"))

from textual_themes.demo import ThemeDemoApp  # noqa: E402
from textual_themes.themes import RETRO_THEMES  # noqa: E402

# Terminal cell size for the gallery shots. 280x70 cells render to a
# 3434x1758 SVG via Rich's exporter — a wide, crisp gallery thumbnail.
_COLS = 280
_ROWS = 70
_OUT_DIR = _REPO_ROOT / "docs" / "screenshots"


async def _capture(slug: str) -> str:
    """Run the demo headless with the given theme and return the SVG."""
    app = ThemeDemoApp()
    async with app.run_test(size=(_COLS, _ROWS)) as pilot:
        app.theme = slug
        await pilot.pause()
        return app.export_screenshot()


async def _main() -> None:
    """Capture every theme in RETRO_THEMES into docs/screenshots/."""
    _OUT_DIR.mkdir(parents=True, exist_ok=True)
    for theme in RETRO_THEMES:
        svg = await _capture(theme.name)
        (_OUT_DIR / f"{theme.name}.svg").write_text(svg, encoding="utf-8")
        print(f"  {theme.name}.svg")
    print(f"Wrote {len(RETRO_THEMES)} screenshots to {_OUT_DIR}")


if __name__ == "__main__":
    asyncio.run(_main())
