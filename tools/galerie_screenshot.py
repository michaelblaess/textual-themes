"""Erzeugt den Galerie-Screenshot fuer EIN Theme.

    cd docs/screenshots
    uv run python ../../tools/galerie_screenshot.py goldrunner

Die Groesse 280x70 ist nicht frei gewaehlt: alle Bestandsdateien in
docs/screenshots liegen bei 3415x1707 Pixeln, und genau diese Masse kommen
bei 280 Spalten und 70 Zeilen heraus (nachgerechnet und gegengeprueft am
15.08.2026). Mit der Vorgabe 120x40 waere die Datei nur 1463x975 gross und
faellt in der Galerie aus dem Raster.

Der Weg ueber run_test() ist headless. Bei komplexen Layouts kann der
Test-Kompositor Streifenartefakte erzeugen - das Ergebnis also ansehen,
bevor es committet wird, und im Zweifel im echten Terminal mit Strg+S
nachziehen.
"""

from __future__ import annotations

import asyncio
import sys
from pathlib import Path

from textual_themes.demo import ThemeDemoApp


async def main(slug: str) -> None:
    app = ThemeDemoApp()
    async with app.run_test(size=(280, 70)) as pilot:
        app.theme = slug
        # Mehrfach durchatmen lassen: der Theme-Wechsel loest ein volles
        # Re-Layout aus, und die Seitenleiste zieht den Fokus nach.
        for _ in range(20):
            await pilot.pause()
        app.save_screenshot(str(Path.cwd() / f"{slug}.svg"))
    print(f"{slug}.svg geschrieben")


if __name__ == "__main__":
    asyncio.run(main(sys.argv[1] if len(sys.argv) > 1 else "goldrunner"))
