"""The colour data must be readable without Textual installed.

That is the whole point of splitting `palettes.py` off `themes.py`: a
consumer that only wants the colours - a Qt application compiled with
Nuitka, a static site generator - should not end up with a TUI framework in
its dependency tree.

These tests guard the promise from both sides: the data is complete and
consistent, and it really does import on its own.
"""

from __future__ import annotations

import subprocess
import sys
from dataclasses import fields

import pytest

from textual_themes.palettes import (
    DISPLAY_NAMES,
    PALETTE_NAMES,
    PALETTES_BY_NAME,
    RETRO_PALETTES,
    Palette,
)

# Every field except `dark` holds a colour and must look like one.
COLOUR_FIELDS = tuple(f.name for f in fields(Palette) if f.name not in {"name", "dark"})


class TestPaletteData:
    def test_forty_palettes(self) -> None:
        """The count is pinned on purpose.

        Adding a theme is a deliberate act, and this line is where it gets
        confirmed - together with the display name below, which is the part
        people forget.
        """
        assert len(RETRO_PALETTES) == 40

    def test_names_are_unique(self) -> None:
        assert len(set(PALETTE_NAMES)) == len(PALETTE_NAMES)

    def test_lookup_covers_every_palette(self) -> None:
        assert set(PALETTES_BY_NAME) == set(PALETTE_NAMES)
        assert all(PALETTES_BY_NAME[p.name] is p for p in RETRO_PALETTES)

    @pytest.mark.parametrize("palette", RETRO_PALETTES, ids=lambda p: p.name)
    def test_every_colour_is_a_six_digit_hex(self, palette: Palette) -> None:
        for feld in COLOUR_FIELDS:
            wert = getattr(palette, feld)
            assert wert.startswith("#"), f"{palette.name}.{feld} = {wert!r}"
            assert len(wert) == 7, f"{palette.name}.{feld} = {wert!r}"
            int(wert[1:], 16)  # raises if it is not hex

    @pytest.mark.parametrize("palette", RETRO_PALETTES, ids=lambda p: p.name)
    def test_name_is_a_stable_identifier(self, palette: Palette) -> None:
        """Names end up in settings files, so no spaces and no capitals."""
        assert palette.name == palette.name.lower()
        assert " " not in palette.name
        assert palette.name.replace("-", "").isalnum()

    def test_every_palette_has_a_display_name(self) -> None:
        assert set(DISPLAY_NAMES) == set(PALETTE_NAMES)


class TestImportsWithoutTextual:
    def test_palettes_load_when_textual_is_missing(self) -> None:
        """The promise, checked rather than assumed.

        Runs in a child process with Textual blocked at import time. Doing it
        in-process would leave the block lying around for every later test.
        """
        skript = (
            "import sys\n"
            "class Sperre:\n"
            "    def find_spec(self, name, path=None, target=None):\n"
            "        if name == 'textual' or name.startswith('textual.'):\n"
            "            raise ImportError('textual is blocked for this test')\n"
            "        return None\n"
            "sys.meta_path.insert(0, Sperre())\n"
            "from textual_themes.palettes import RETRO_PALETTES\n"
            "assert 'textual.theme' not in sys.modules\n"
            "print(len(RETRO_PALETTES))\n"
        )
        ergebnis = subprocess.run(
            [sys.executable, "-c", skript],
            capture_output=True,
            text=True,
            check=False,
        )
        assert ergebnis.returncode == 0, ergebnis.stderr
        assert ergebnis.stdout.strip() == "40"

    def test_the_block_actually_blocks(self) -> None:
        """Counter-check: without it the test above proves nothing.

        If the import barrier were ineffective, importing Textual would
        succeed and the test above would pass for the wrong reason.
        """
        skript = (
            "import sys\n"
            "class Sperre:\n"
            "    def find_spec(self, name, path=None, target=None):\n"
            "        if name == 'textual' or name.startswith('textual.'):\n"
            "            raise ImportError('textual is blocked for this test')\n"
            "        return None\n"
            "sys.meta_path.insert(0, Sperre())\n"
            "import textual.theme\n"
        )
        ergebnis = subprocess.run(
            [sys.executable, "-c", skript],
            capture_output=True,
            text=True,
            check=False,
        )
        assert ergebnis.returncode != 0
        assert "blocked for this test" in ergebnis.stderr

    def test_a_theme_constant_still_reports_a_missing_textual(self) -> None:
        """Accessing a theme without Textual must say what is wrong.

        The lazy lookup could just as easily raise AttributeError on a name
        that plainly exists - that would send whoever hits it looking in the
        wrong place.
        """
        skript = (
            "import sys\n"
            "class Sperre:\n"
            "    def find_spec(self, name, path=None, target=None):\n"
            "        if name == 'textual' or name.startswith('textual.'):\n"
            "            raise ImportError('textual is blocked for this test')\n"
            "        return None\n"
            "sys.meta_path.insert(0, Sperre())\n"
            "import textual_themes\n"
            "try:\n"
            "    textual_themes.BROTKASTEN_THEME\n"
            "except ImportError as fehler:\n"
            "    print('ImportError:', fehler)\n"
            "else:\n"
            "    raise SystemExit('expected an ImportError')\n"
        )
        ergebnis = subprocess.run(
            [sys.executable, "-c", skript],
            capture_output=True,
            text=True,
            check=False,
        )
        assert ergebnis.returncode == 0, ergebnis.stderr
        assert "needs Textual" in ergebnis.stdout

    def test_an_unknown_name_is_still_an_attribute_error(self) -> None:
        import textual_themes

        with pytest.raises(AttributeError):
            getattr(textual_themes, "GIBT_ES_NICHT_THEME")  # noqa: B009 - genau das ist der Test
