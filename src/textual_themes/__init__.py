"""textual-themes — Retro color themes for Textual TUI apps.

Usage:
    from textual_themes import C64_THEME, AMIGA_THEME
    app.register_theme(C64_THEME)
    app.theme = "c64"
"""
from __future__ import annotations

from .themes import (
    AMIGA_THEME,
    ATARI_ST_THEME,
    BEOS_THEME,
    C64_THEME,
    IBM_TERMINAL_THEME,
    LINUX_MINT_THEME,
    MACOS_THEME,
    MSDOS_THEME,
    NEXTSTEP_THEME,
    OPENSUSE_THEME,
    OS2_WARP_THEME,
    PLAN9_THEME,
    RETRO_THEME_NAMES,
    RETRO_THEMES,
    SOLARIS_CDE_THEME,
    THEME_DISPLAY_NAMES,
    UBUNTU_THEME,
    WINDOWS_XP_THEME,
    register_all,
)

__version__ = "0.3.0"
__author__ = "Michael Blaess"

__all__ = [
    "C64_THEME",
    "AMIGA_THEME",
    "ATARI_ST_THEME",
    "IBM_TERMINAL_THEME",
    "NEXTSTEP_THEME",
    "BEOS_THEME",
    "UBUNTU_THEME",
    "MACOS_THEME",
    "WINDOWS_XP_THEME",
    "MSDOS_THEME",
    "PLAN9_THEME",
    "SOLARIS_CDE_THEME",
    "OS2_WARP_THEME",
    "OPENSUSE_THEME",
    "LINUX_MINT_THEME",
    "RETRO_THEMES",
    "RETRO_THEME_NAMES",
    "THEME_DISPLAY_NAMES",
    "register_all",
]
