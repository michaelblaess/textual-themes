"""Retro color themes for Textual TUI applications.

Each theme is a `textual.theme.Theme` instance that can be registered
with any Textual `App` via `app.register_theme(theme)`.

Themes:
    C64          — Commodore 64 (1982): blue/light-blue
    Amiga        — Amiga Workbench 1.3 (1987): blue/white/orange
    Atari ST     — Atari ST GEM Desktop (1985): white/black/green (light)
    IBM Terminal — IBM 3278 Terminal (1970s-80s): phosphor-green on black
    NeXTSTEP     — NeXTSTEP (1989): dark gray with purple accents
    BeOS         — BeOS (1995): blue-gray with yellow Deskbar accent
    Ubuntu       — Ubuntu Desktop: aubergine/purple with orange accents
    macOS        — macOS: clean light gray with blue accents (light)
    Windows XP   — Windows XP Luna: blue taskbar with green start button
    MS-DOS       — Norton Commander: blue/cyan/yellow
    Plan 9       — Plan 9 from Bell Labs: yellow/blue/green
    Solaris CDE  — Sun CDE Desktop: beige/teal corporate Unix
    OS/2 Warp    — IBM OS/2 Warp: dark blue/teal
    openSUSE     — openSUSE: dark green/white
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from textual.theme import Theme

if TYPE_CHECKING:
    from textual.app import App


# ────────────────────────────────────────────────────────────────────────
# C64 — Commodore 64 (1982)
# Blue on light-blue, the classic. PETSCII feeling.
# ────────────────────────────────────────────────────────────────────────
C64_THEME = Theme(
    name="c64",
    primary="#7878FF",
    secondary="#40318D",
    accent="#7878FF",
    foreground="#A0A0FF",
    background="#40318D",
    surface="#50419D",
    panel="#3A2B87",
    boost="#6868EE",
    warning="#A87832",
    error="#CC5555",
    success="#68A941",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Amiga Workbench 1.3 (1987)
# Blue/white/orange — the Workbench three-color scheme.
# ────────────────────────────────────────────────────────────────────────
AMIGA_THEME = Theme(
    name="amiga",
    primary="#FF8800",
    secondary="#0055AA",
    accent="#FF8800",
    foreground="#FFFFFF",
    background="#0055AA",
    surface="#0066BB",
    panel="#004499",
    boost="#FF9922",
    warning="#FFAA00",
    error="#FF4444",
    success="#44BB44",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Atari ST GEM Desktop (1985)
# White/black/green — the monochrome GEM Desktop look.
# ────────────────────────────────────────────────────────────────────────
ATARI_ST_THEME = Theme(
    name="atari-st",
    primary="#007700",
    secondary="#555555",
    accent="#009900",
    foreground="#111111",
    background="#E8E8E8",
    surface="#F2F2F2",
    panel="#DDDDDD",
    boost="#00AA00",
    warning="#AA8800",
    error="#CC0000",
    success="#007700",
    dark=False,
)

# ────────────────────────────────────────────────────────────────────────
# IBM Terminal (1970s-80s)
# Phosphor-green on black — the archetypal terminal.
# ────────────────────────────────────────────────────────────────────────
IBM_TERMINAL_THEME = Theme(
    name="ibm-terminal",
    primary="#33FF33",
    secondary="#1A8C1A",
    accent="#33FF33",
    foreground="#33FF33",
    background="#0A0A0A",
    surface="#111111",
    panel="#0D0D0D",
    boost="#44FF44",
    warning="#22BB22",
    error="#FF3333",
    success="#33FF33",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# NeXTSTEP (1989)
# Dark gray with subtle purple accents — Steve Jobs' "other" company.
# Elegant dark interface with 3D effects.
# ────────────────────────────────────────────────────────────────────────
NEXTSTEP_THEME = Theme(
    name="nextstep",
    primary="#9966CC",
    secondary="#555555",
    accent="#9966CC",
    foreground="#E0E0E0",
    background="#2A2A2A",
    surface="#3A3A3A",
    panel="#222222",
    boost="#AA77DD",
    warning="#CC9933",
    error="#CC4444",
    success="#44AA44",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# BeOS (1995)
# Gray with yellow accent — the Deskbar sends its regards.
# Fast, elegant, ahead of its time.
# ────────────────────────────────────────────────────────────────────────
BEOS_THEME = Theme(
    name="beos",
    primary="#FFD800",
    secondary="#5F5F5F",
    accent="#FFD800",
    foreground="#E8E8E8",
    background="#3A3A4A",
    surface="#4A4A5A",
    panel="#333344",
    boost="#FFE433",
    warning="#FF9900",
    error="#DD3333",
    success="#33BB33",
    dark=True,
)


# ────────────────────────────────────────────────────────────────────────
# Ubuntu Desktop
# Aubergine/purple with orange accents — Canonical's signature look.
# ────────────────────────────────────────────────────────────────────────
UBUNTU_THEME = Theme(
    name="ubuntu",
    primary="#E95420",
    secondary="#4A1942",
    accent="#E95420",
    foreground="#EEEEEE",
    background="#300A24",
    surface="#3B1530",
    panel="#280820",
    boost="#FF6E3A",
    warning="#F99B11",
    error="#DF382C",
    success="#38B44A",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# macOS (modern)
# Clean light gray with blue accents — Cupertino minimalism.
# ────────────────────────────────────────────────────────────────────────
MACOS_THEME = Theme(
    name="macos",
    primary="#007AFF",
    secondary="#5856D6",
    accent="#007AFF",
    foreground="#1D1D1F",
    background="#F5F5F7",
    surface="#FFFFFF",
    panel="#E8E8ED",
    boost="#0A84FF",
    warning="#FF9500",
    error="#FF3B30",
    success="#34C759",
    dark=False,
)

# ────────────────────────────────────────────────────────────────────────
# Windows XP — Luna (2001)
# Blue taskbar, green Start button — the most popular Windows ever.
# ────────────────────────────────────────────────────────────────────────
WINDOWS_XP_THEME = Theme(
    name="windows-xp",
    primary="#0054E3",
    secondary="#21A121",
    accent="#0054E3",
    foreground="#FFFFFF",
    background="#003399",
    surface="#0044AA",
    panel="#002D8A",
    boost="#2266EE",
    warning="#FFCC00",
    error="#E81123",
    success="#21A121",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# MS-DOS / Norton Commander (1986)
# Blue background, cyan panels, yellow highlights — the file manager.
# ────────────────────────────────────────────────────────────────────────
MSDOS_THEME = Theme(
    name="msdos",
    primary="#00AAAA",
    secondary="#AAAA00",
    accent="#FFFF55",
    foreground="#AAAAAA",
    background="#0000AA",
    surface="#0000BB",
    panel="#000088",
    boost="#55FFFF",
    warning="#AAAA00",
    error="#FF5555",
    success="#55FF55",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Plan 9 from Bell Labs (1992)
# Yellow/blue/green — the most distinctive OS palette ever designed.
# ────────────────────────────────────────────────────────────────────────
PLAN9_THEME = Theme(
    name="plan9",
    primary="#9EBC9F",
    secondary="#98BACE",
    accent="#9EBC9F",
    foreground="#222222",
    background="#FFFFEA",
    surface="#EAFFFF",
    panel="#EAFFDB",
    boost="#AACCAA",
    warning="#CC9933",
    error="#BB3333",
    success="#558855",
    dark=False,
)

# ────────────────────────────────────────────────────────────────────────
# Solaris CDE — Common Desktop Environment (1993)
# Slate gray with warm accents — the corporate Unix workstation.
# ────────────────────────────────────────────────────────────────────────
SOLARIS_CDE_THEME = Theme(
    name="solaris-cde",
    primary="#CC9966",
    secondary="#5F7B8A",
    accent="#CC9966",
    foreground="#D8D0C8",
    background="#3A4A5A",
    surface="#455565",
    panel="#303F4F",
    boost="#DDAA77",
    warning="#CCAA44",
    error="#CC5544",
    success="#55AA66",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# OS/2 Warp (1994)
# Dark blue with teal accents — IBM's alternative to Windows.
# ────────────────────────────────────────────────────────────────────────
OS2_WARP_THEME = Theme(
    name="os2-warp",
    primary="#00BBBB",
    secondary="#3333AA",
    accent="#00BBBB",
    foreground="#D0D0D0",
    background="#1A1A4E",
    surface="#25255E",
    panel="#141442",
    boost="#22DDDD",
    warning="#DDAA22",
    error="#DD4444",
    success="#44BB66",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# openSUSE
# Dark green with white — the Chameleon's desktop.
# ────────────────────────────────────────────────────────────────────────
OPENSUSE_THEME = Theme(
    name="opensuse",
    primary="#73BA25",
    secondary="#35B9AB",
    accent="#73BA25",
    foreground="#EEEEEE",
    background="#173F0F",
    surface="#1E4D15",
    panel="#12330B",
    boost="#85CC37",
    warning="#F0A30A",
    error="#DD3333",
    success="#73BA25",
    dark=True,
)


# ── Convenience collections ────────────────────────────────────────────

RETRO_THEMES: list[Theme] = [
    C64_THEME,
    AMIGA_THEME,
    ATARI_ST_THEME,
    IBM_TERMINAL_THEME,
    NEXTSTEP_THEME,
    BEOS_THEME,
    UBUNTU_THEME,
    MACOS_THEME,
    WINDOWS_XP_THEME,
    MSDOS_THEME,
    PLAN9_THEME,
    SOLARIS_CDE_THEME,
    OS2_WARP_THEME,
    OPENSUSE_THEME,
]

RETRO_THEME_NAMES: list[str] = [t.name for t in RETRO_THEMES]

THEME_DISPLAY_NAMES: dict[str, str] = {
    "c64": "C64 — Commodore 64",
    "amiga": "Amiga Workbench 1.3",
    "atari-st": "Atari ST GEM Desktop",
    "ibm-terminal": "IBM Terminal — Phosphor Green",
    "nextstep": "NeXTSTEP",
    "beos": "BeOS",
    "ubuntu": "Ubuntu",
    "macos": "macOS",
    "windows-xp": "Windows XP — Luna",
    "msdos": "MS-DOS — Norton Commander",
    "plan9": "Plan 9 — Bell Labs",
    "solaris-cde": "Solaris CDE",
    "os2-warp": "OS/2 Warp",
    "opensuse": "openSUSE",
}


def register_all(app: App[object]) -> None:
    """Register all retro themes with a Textual App.

    Example:
        from textual_themes import register_all

        class MyApp(App):
            def __init__(self):
                super().__init__()
                register_all(self)
                self.theme = "c64"
    """
    for theme in RETRO_THEMES:
        app.register_theme(theme)
