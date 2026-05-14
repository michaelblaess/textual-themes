"""Tests for textual-themes."""

from __future__ import annotations

import pytest
from textual.theme import Theme

from textual_themes import (
    BEBOX_THEME,
    BOING_THEME,
    BROTKASTEN_THEME,
    CLASSIC_TERMINAL_THEME,
    GEMSTONE_THEME,
    NEXT_THEME,
    RETRO_THEME_NAMES,
    RETRO_THEMES,
    THEME_DISPLAY_NAMES,
)


class TestThemeDefinitions:
    def test_themes_count_matches_names(self) -> None:
        # Anzahl variiert mit dem Release - wichtig ist nur, dass beide Listen
        # uebereinstimmen und nicht leer sind.
        assert len(RETRO_THEMES) == len(RETRO_THEME_NAMES)
        assert len(RETRO_THEMES) > 0

    def test_all_are_theme_instances(self) -> None:
        for theme in RETRO_THEMES:
            assert isinstance(theme, Theme)

    def test_core_themes_present(self) -> None:
        # Pruefe nur die sechs Original-Themes (nach Trademark-Rename).
        expected_core = ["brotkasten", "boing", "gemstone", "classic-terminal", "next", "bebox"]
        for name in expected_core:
            assert name in RETRO_THEME_NAMES, f"Theme '{name}' fehlt in RETRO_THEME_NAMES"

    def test_names_are_unique(self) -> None:
        assert len(set(RETRO_THEME_NAMES)) == len(RETRO_THEME_NAMES)

    @pytest.mark.skip(
        reason="Backgrounds sind seit dem 36-Themes-Reshuffle nicht mehr garantiert "
        "unique - mehrere Themes teilen z.B. tiefes Schwarz als Hintergrund. "
        "Faerbung wird durch die anderen Akzent-Farben unterschieden."
    )
    def test_backgrounds_are_unique(self) -> None:
        backgrounds = [t.background for t in RETRO_THEMES]
        assert len(set(backgrounds)) == len(backgrounds)

    def test_display_names_for_all(self) -> None:
        for name in RETRO_THEME_NAMES:
            assert name in THEME_DISPLAY_NAMES
            assert len(THEME_DISPLAY_NAMES[name]) > 0


class TestDarkLightModes:
    def test_brotkasten_is_dark(self) -> None:
        assert BROTKASTEN_THEME.dark is True

    def test_boing_is_dark(self) -> None:
        assert BOING_THEME.dark is True

    def test_gemstone_is_light(self) -> None:
        # Gemstone ist der Nachfolger von atari-st (helles GEM Desktop).
        assert GEMSTONE_THEME.dark is False

    def test_classic_terminal_is_dark(self) -> None:
        assert CLASSIC_TERMINAL_THEME.dark is True

    def test_next_is_dark(self) -> None:
        assert NEXT_THEME.dark is True

    def test_bebox_is_dark(self) -> None:
        assert BEBOX_THEME.dark is True


class TestColorValues:
    """Ensure all color values are valid hex colors."""

    def test_all_colors_are_hex(self) -> None:
        color_attrs = [
            "primary",
            "secondary",
            "accent",
            "foreground",
            "background",
            "surface",
            "panel",
            "boost",
            "warning",
            "error",
            "success",
        ]
        for theme in RETRO_THEMES:
            for attr in color_attrs:
                value = getattr(theme, attr, None)
                if value is not None:
                    assert isinstance(value, str), f"{theme.name}.{attr} is not a string: {value!r}"
                    assert value.startswith("#"), f"{theme.name}.{attr} doesn't start with #: {value!r}"
                    assert len(value) == 7, f"{theme.name}.{attr} is not #RRGGBB: {value!r}"
                    # Validate hex digits
                    int(value[1:], 16)


class TestRegisterAll:
    def test_register_all_import(self) -> None:
        from textual_themes import register_all

        assert callable(register_all)
