"""textual-themes - retro colour themes for Textual TUI apps.

Usage:
    from textual_themes import BROTKASTEN_THEME, BOING_THEME
    app.register_theme(BROTKASTEN_THEME)
    app.theme = "brotkasten"

Without Textual installed, the colour data is still available:

    from textual_themes.palettes import RETRO_PALETTES

That is the reason the theme constants below are resolved lazily. Importing
any submodule runs this file first, so an eager `from .themes import ...`
would drag Textual in even for a consumer that only wants the palettes - a
compiled Qt binary, for instance.
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Any

from .palettes import (
    DISPLAY_NAMES,
    PALETTE_NAMES,
    PALETTES_BY_NAME,
    RETRO_PALETTES,
    Palette,
)

if TYPE_CHECKING:
    # Only for type checkers - at runtime these come through __getattr__.
    from .themes import (
        ASCOT_THEME,
        BEASTIE_THEME,
        BEBOX_THEME,
        BLUESY_THEME,
        BOING_THEME,
        BRICK_THEME,
        BROTKASTEN_THEME,
        BUNTY_THEME,
        CHRISTOPHORUS_THEME,
        CLASSIC_NAVY_THEME,
        CLASSIC_TERMINAL_THEME,
        CLIPPER_THEME,
        COMMANDR_THEME,
        CORLEONE_THEME,
        CRIMSON_THEME,
        CUPERTINO_THEME,
        FIFTY_EIGHT_THEME,
        FLUGHUND_THEME,
        GEEKO_THEME,
        GEMSTONE_THEME,
        GOLDEN_BROWN_THEME,
        GOLDFINDER_THEME,
        GOLDRUNNER_THEME,
        HERCULES_THEME,
        HULKULA_THEME,
        JOKER_THEME,
        LENSEFLARE_THEME,
        LUNA_THEME,
        MARLEY_THEME,
        METROPOLIS_THEME,
        MIAMI_THEME,
        MINTY_THEME,
        MOTIF_THEME,
        NEXT_THEME,
        PLAN9_THEME,
        PLATOON_THEME,
        RACING_THEME,
        RAZZY_THEME,
        RETRO_THEME_NAMES,
        RETRO_THEMES,
        SPIDERIZED_THEME,
        SYNTHWAVE_THEME,
        THEME_DISPLAY_NAMES,
        WARP_THEME,
        register_all,
    )

__version__ = "0.15.0"
__author__ = "Michael Blaess"

# Everything that lives in themes.py and therefore needs Textual.
_LAZY: frozenset[str] = frozenset(
    {
        "ASCOT_THEME",
        "BEASTIE_THEME",
        "BEBOX_THEME",
        "BLUESY_THEME",
        "BOING_THEME",
        "BRICK_THEME",
        "BROTKASTEN_THEME",
        "BUNTY_THEME",
        "CHRISTOPHORUS_THEME",
        "CLASSIC_NAVY_THEME",
        "CLASSIC_TERMINAL_THEME",
        "CLIPPER_THEME",
        "COMMANDR_THEME",
        "CORLEONE_THEME",
        "CRIMSON_THEME",
        "CUPERTINO_THEME",
        "FIFTY_EIGHT_THEME",
        "FLUGHUND_THEME",
        "GEEKO_THEME",
        "GEMSTONE_THEME",
        "GOLDEN_BROWN_THEME",
        "GOLDFINDER_THEME",
        "GOLDRUNNER_THEME",
        "HERCULES_THEME",
        "HULKULA_THEME",
        "JOKER_THEME",
        "LENSEFLARE_THEME",
        "LUNA_THEME",
        "MARLEY_THEME",
        "METROPOLIS_THEME",
        "MIAMI_THEME",
        "MINTY_THEME",
        "MOTIF_THEME",
        "NEXT_THEME",
        "PLAN9_THEME",
        "PLATOON_THEME",
        "RACING_THEME",
        "RAZZY_THEME",
        "SPIDERIZED_THEME",
        "SYNTHWAVE_THEME",
        "WARP_THEME",
        "RETRO_THEMES",
        "RETRO_THEME_NAMES",
        "THEME_DISPLAY_NAMES",
        "register_all",
    }
)


def __getattr__(name: str) -> Any:
    """Resolves the theme constants on first access.

    Raises:
        AttributeError:
            For unknown names, as any module does.
        ImportError:
            When Textual is missing. The message says so plainly - the
            alternative is a confusing AttributeError on a name that
            obviously exists.
    """
    if name not in _LAZY:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    try:
        from . import themes
    except ImportError as fehler:  # pragma: no cover - depends on the install
        raise ImportError(
            f"{name} needs Textual. Install textual-themes[textual], or use "
            f"textual_themes.palettes for the colour data alone."
        ) from fehler
    return getattr(themes, name)


def __dir__() -> list[str]:
    return sorted(__all__)


# Theme constants kept alphabetically sorted - new entries go in order.
__all__ = [
    "ASCOT_THEME",
    "BEASTIE_THEME",
    "BEBOX_THEME",
    "BLUESY_THEME",
    "BOING_THEME",
    "BRICK_THEME",
    "BROTKASTEN_THEME",
    "BUNTY_THEME",
    "CHRISTOPHORUS_THEME",
    "CLASSIC_NAVY_THEME",
    "CLASSIC_TERMINAL_THEME",
    "CLIPPER_THEME",
    "COMMANDR_THEME",
    "CORLEONE_THEME",
    "CRIMSON_THEME",
    "CUPERTINO_THEME",
    "DISPLAY_NAMES",
    "FIFTY_EIGHT_THEME",
    "FLUGHUND_THEME",
    "GEEKO_THEME",
    "GEMSTONE_THEME",
    "GOLDEN_BROWN_THEME",
    "GOLDFINDER_THEME",
    "GOLDRUNNER_THEME",
    "HERCULES_THEME",
    "HULKULA_THEME",
    "JOKER_THEME",
    "LENSEFLARE_THEME",
    "LUNA_THEME",
    "MARLEY_THEME",
    "METROPOLIS_THEME",
    "MIAMI_THEME",
    "MINTY_THEME",
    "MOTIF_THEME",
    "NEXT_THEME",
    "PALETTES_BY_NAME",
    "PALETTE_NAMES",
    "PLAN9_THEME",
    "PLATOON_THEME",
    "Palette",
    "RACING_THEME",
    "RAZZY_THEME",
    "RETRO_PALETTES",
    "RETRO_THEMES",
    "RETRO_THEME_NAMES",
    "SPIDERIZED_THEME",
    "SYNTHWAVE_THEME",
    "THEME_DISPLAY_NAMES",
    "WARP_THEME",
    "register_all",
]
