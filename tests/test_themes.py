"""Tests for textual-themes."""
from __future__ import annotations

from textual.theme import Theme

from textual_themes import (
    AMIGA_THEME,
    ATARI_ST_THEME,
    BEOS_THEME,
    C64_THEME,
    IBM_TERMINAL_THEME,
    NEXTSTEP_THEME,
    RETRO_THEME_NAMES,
    RETRO_THEMES,
    THEME_DISPLAY_NAMES,
)


class TestThemeDefinitions:
    def test_six_themes_defined(self) -> None:
        assert len(RETRO_THEMES) == 6
        assert len(RETRO_THEME_NAMES) == 6

    def test_all_are_theme_instances(self) -> None:
        for theme in RETRO_THEMES:
            assert isinstance(theme, Theme)

    def test_theme_names_match(self) -> None:
        expected = ["c64", "amiga", "atari-st", "ibm-terminal", "nextstep", "beos"]
        assert RETRO_THEME_NAMES == expected

    def test_names_are_unique(self) -> None:
        assert len(set(RETRO_THEME_NAMES)) == len(RETRO_THEME_NAMES)

    def test_backgrounds_are_unique(self) -> None:
        backgrounds = [t.background for t in RETRO_THEMES]
        assert len(set(backgrounds)) == len(backgrounds)

    def test_display_names_for_all(self) -> None:
        for name in RETRO_THEME_NAMES:
            assert name in THEME_DISPLAY_NAMES
            assert len(THEME_DISPLAY_NAMES[name]) > 0


class TestDarkLightModes:
    def test_c64_is_dark(self) -> None:
        assert C64_THEME.dark is True

    def test_amiga_is_dark(self) -> None:
        assert AMIGA_THEME.dark is True

    def test_atari_is_light(self) -> None:
        assert ATARI_ST_THEME.dark is False

    def test_ibm_terminal_is_dark(self) -> None:
        assert IBM_TERMINAL_THEME.dark is True

    def test_nextstep_is_dark(self) -> None:
        assert NEXTSTEP_THEME.dark is True

    def test_beos_is_dark(self) -> None:
        assert BEOS_THEME.dark is True


class TestColorValues:
    """Ensure all color values are valid hex colors."""

    def test_all_colors_are_hex(self) -> None:
        color_attrs = [
            "primary", "secondary", "accent", "foreground",
            "background", "surface", "panel", "boost",
            "warning", "error", "success",
        ]
        for theme in RETRO_THEMES:
            for attr in color_attrs:
                value = getattr(theme, attr, None)
                if value is not None:
                    assert isinstance(value, str), (
                        f"{theme.name}.{attr} is not a string: {value!r}"
                    )
                    assert value.startswith("#"), (
                        f"{theme.name}.{attr} doesn't start with #: {value!r}"
                    )
                    assert len(value) == 7, (
                        f"{theme.name}.{attr} is not #RRGGBB: {value!r}"
                    )
                    # Validate hex digits
                    int(value[1:], 16)


class TestRegisterAll:
    def test_register_all_import(self) -> None:
        from textual_themes import register_all
        assert callable(register_all)
