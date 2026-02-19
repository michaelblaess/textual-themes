"""Retro color themes for Textual TUI applications.

Each theme is a `textual.theme.Theme` instance that can be registered
with any Textual `App` via `app.register_theme(theme)`.

Themes:
    C64         — Commodore 64 (1982): blue/light-blue
    Amiga       — Amiga Workbench 1.3 (1987): blue/white/orange
    Atari ST    — Atari ST GEM Desktop (1985): white/black/green (light)
    IBM Terminal — IBM 3278 Terminal (1970s-80s): phosphor-green on black
    NeXTSTEP    — NeXTSTEP (1989): dark gray with purple accents
    BeOS        — BeOS (1995): blue-gray with yellow Deskbar accent
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


# ── Convenience collections ────────────────────────────────────────────

RETRO_THEMES: list[Theme] = [
    C64_THEME,
    AMIGA_THEME,
    ATARI_ST_THEME,
    IBM_TERMINAL_THEME,
    NEXTSTEP_THEME,
    BEOS_THEME,
]

RETRO_THEME_NAMES: list[str] = [t.name for t in RETRO_THEMES]

THEME_DISPLAY_NAMES: dict[str, str] = {
    "c64": "C64 — Commodore 64",
    "amiga": "Amiga Workbench 1.3",
    "atari-st": "Atari ST GEM Desktop",
    "ibm-terminal": "IBM Terminal — Phosphor Green",
    "nextstep": "NeXTSTEP",
    "beos": "BeOS",
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
