"""Retro color themes for Textual TUI applications.

Each theme is a `textual.theme.Theme` instance that can be registered
with any Textual `App` via `app.register_theme(theme)`.

This package contains 41 themes inspired by classic computers,
operating systems, vintage diver watches, comic-book color schemes,
80s pastel and Spielberg-era cinema, motorsport liveries and reggae
roots. Theme names are descriptive of the visual style only; no
trademarks are used as product names.

Themes (alphabetical):
    Ascot             — Le-Mans racing green with signal yellow, silver and beige text
    Beastie           — daemon red on dark slate
    BeBox             — blue-gray with yellow status-bar accent
    Bluesy            — royal blue with rich yellow-gold accents
    Boing             — three-color workbench palette: blue/white/orange
    Brick             — olive-green handheld LCD (light)
    Brotkasten        — light blue on royal blue (8-bit PETSCII style)
    Bunty             — aubergine with warm orange accents
    Christophorus     — navy and gold from the Christophorus logo
    Classic Navy      — deep navy with silver and muted brick-red
    Classic Terminal  — phosphor-green on black (CRT)
    Clipper           — globe blue on ivory (light)
    Commandr          — blue/cyan/yellow file-manager palette
    Corleone          — cold mafia-noir: bronze, steel-grey and ash on bluish black
    Crimson           — deep red on dark charcoal
    Cupertino         — clean light gray with blue accents (light)
    Fifty-Eight       — black dial with aged gold lume + bezel red
    Flughund          — midnight black & moonlit blue
    Geeko             — dark green with white
    Gemstone          — monochrome GEM Desktop look (light)
    Golden Brown      — warm mafia-noir: antique gold, sepia and parchment on warm black
    Goldfinder        — deep black with 18K gold accents
    Goldrunner        — Atari-ST shooter gold on the violet city skyline
    Hulkula           — vivid green rage with steel-gray edges
    Joker             — Comic Gotham villain: royal purple suit, acid-green hair & yellow vest
    Lenseflare        — 80s Spielberg orange-teal bichromatic on twilight blue
    Luna              — sky-blue task-bar with green start button
    Marley            — reggae roots palette: black, green, gold, red
    Metropolis        — bold blue, crimson red and sun yellow primary triad
    Miami             — pastel 80s: twilight teal, flamingo pink, sunset coral
    Minty             — warm mint-green on charcoal
    Motif             — beige slate-gray corporate Unix toolkit
    Next              — slate gray with magenta accents
    Plan 9            — pulpy yellow/blue/green (light)
    Platoon           — muted military olive-drab with khaki accent on near-black
    Racing            — charcoal with blue, red and silver stripes
    Razzy             — raspberry red on dark slate
    Spiderized        — red & royal-blue hero suit (high-contrast)
    Synthwave         — deep purple with neon pink and electric cyan
    Warp              — dark blue with teal accents
"""

from __future__ import annotations

from dataclasses import asdict
from typing import TYPE_CHECKING

from textual.theme import Theme

from .palettes import (
    DISPLAY_NAMES,
    RETRO_PALETTES,
    Palette,
)

if TYPE_CHECKING:
    from textual.app import App


def _build(palette: Palette) -> Theme:
    """Wraps a palette into a Textual Theme.

    No translation table is needed: `Palette` uses exactly the field names
    `Theme` expects. Should Textual ever add a field, this is the single
    place that has to learn about it.

    Args:
        palette:
            The colour data.

    Returns:
        The theme, ready for `App.register_theme()`.
    """
    return Theme(**asdict(palette))


# One Theme per palette, built once and shared. The named constants below and
# RETRO_THEMES point at the same objects - code that compares by identity
# keeps working.
_BY_NAME: dict[str, Theme] = {palette.name: _build(palette) for palette in RETRO_PALETTES}

BROTKASTEN_THEME = _BY_NAME["brotkasten"]
BOING_THEME = _BY_NAME["boing"]
GEMSTONE_THEME = _BY_NAME["gemstone"]
CLASSIC_TERMINAL_THEME = _BY_NAME["classic-terminal"]
NEXT_THEME = _BY_NAME["next"]
BEBOX_THEME = _BY_NAME["bebox"]
BUNTY_THEME = _BY_NAME["bunty"]
CUPERTINO_THEME = _BY_NAME["cupertino"]
LUNA_THEME = _BY_NAME["luna"]
COMMANDR_THEME = _BY_NAME["commandr"]
PLAN9_THEME = _BY_NAME["plan9"]
MOTIF_THEME = _BY_NAME["motif"]
WARP_THEME = _BY_NAME["warp"]
GEEKO_THEME = _BY_NAME["geeko"]
MINTY_THEME = _BY_NAME["minty"]
CRIMSON_THEME = _BY_NAME["crimson"]
RAZZY_THEME = _BY_NAME["razzy"]
BEASTIE_THEME = _BY_NAME["beastie"]
FIFTY_EIGHT_THEME = _BY_NAME["fifty-eight"]
BLUESY_THEME = _BY_NAME["bluesy"]
GOLDFINDER_THEME = _BY_NAME["goldfinder"]
GOLDRUNNER_THEME = _BY_NAME["goldrunner"]
HERCULES_THEME = _BY_NAME["hercules"]
HULKULA_THEME = _BY_NAME["hulkula"]
FLUGHUND_THEME = _BY_NAME["flughund"]
CLASSIC_NAVY_THEME = _BY_NAME["classic-navy"]
BRICK_THEME = _BY_NAME["brick"]
CLIPPER_THEME = _BY_NAME["clipper"]
SYNTHWAVE_THEME = _BY_NAME["synthwave"]
MIAMI_THEME = _BY_NAME["miami"]
RACING_THEME = _BY_NAME["racing"]
METROPOLIS_THEME = _BY_NAME["metropolis"]
SPIDERIZED_THEME = _BY_NAME["spiderized"]
ASCOT_THEME = _BY_NAME["ascot"]
JOKER_THEME = _BY_NAME["joker"]
MARLEY_THEME = _BY_NAME["marley"]
LENSEFLARE_THEME = _BY_NAME["lenseflare"]
PLATOON_THEME = _BY_NAME["platoon"]
CORLEONE_THEME = _BY_NAME["corleone"]
GOLDEN_BROWN_THEME = _BY_NAME["golden-brown"]
CHRISTOPHORUS_THEME = _BY_NAME["christophorus"]

RETRO_THEMES: list[Theme] = list(_BY_NAME.values())

RETRO_THEME_NAMES: list[str] = [theme.name for theme in RETRO_THEMES]

# The display names live with the colour data - they describe the palette,
# not the Textual wrapper. Re-exported here under the established name.
THEME_DISPLAY_NAMES: dict[str, str] = DISPLAY_NAMES


def register_all(app: App[object]) -> None:
    """Register all retro themes with a Textual App.

    Example:
        from textual_themes import register_all

        class MyApp(App):
            def __init__(self):
                super().__init__()
                register_all(self)
                self.theme = "brotkasten"
    """
    for theme in RETRO_THEMES:
        app.register_theme(theme)
