"""Retro color themes for Textual TUI applications.

Each theme is a `textual.theme.Theme` instance that can be registered
with any Textual `App` via `app.register_theme(theme)`.

This package contains 31 themes inspired by classic computers,
operating systems, vintage diver watches, comic-book color schemes,
80s pastel and motorsport liveries. Theme names are descriptive of
the visual style only; no trademarks are used as product names.

Themes:
    Brotkasten        — light blue on royal blue (8-bit PETSCII style)
    Boing             — three-color workbench palette: blue/white/orange
    Gemstone          — monochrome GEM Desktop look (light)
    Classic Terminal  — phosphor-green on black (CRT)
    Next              — slate gray with magenta accents
    BeBox             — blue-gray with yellow status-bar accent
    Bunty             — aubergine with warm orange accents
    Cupertino         — clean light gray with blue accents (light)
    Luna              — sky-blue task-bar with green start button
    Commandr          — blue/cyan/yellow file-manager palette
    Plan 9            — pulpy yellow/blue/green (light)
    Motif             — beige slate-gray corporate Unix toolkit
    Warp              — dark blue with teal accents
    Geeko             — dark green with white
    Minty             — warm mint-green on charcoal
    Crimson           — deep red on dark charcoal
    Razzy             — raspberry red on dark slate
    Beastie           — daemon red on dark slate
    Fifty-Eight       — black dial with aged gold lume + bezel red
    Bluesy            — royal blue with rich yellow-gold accents
    Goldfinder        — deep black with 18K gold accents
    Hulkula           — vivid green rage with steel-gray edges
    Flughund          — midnight black & moonlit blue
    Classic Navy      — deep navy with silver and muted brick-red
    Brick             — olive-green handheld LCD (light)
    Clipper           — globe blue on ivory (light)
    Synthwave         — deep purple with neon pink and electric cyan
    Miami             — pastel 80s: twilight teal, flamingo pink, sunset coral
    Racing            — charcoal with blue, red and silver stripes
    Metropolis        — bold blue, crimson red and sun yellow primary triad
    Spiderized        — red & royal-blue hero suit (high-contrast)
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from textual.theme import Theme

if TYPE_CHECKING:
    from textual.app import App


# ────────────────────────────────────────────────────────────────────────
# Brotkasten
# Light blue on royal blue, the iconic 8-bit color cast (PETSCII style).
# Pepto-inspired palette: deep blue background, vivid light-blue text,
# lifted surface so widgets pop, yellow accents for highlights.
# ────────────────────────────────────────────────────────────────────────
BROTKASTEN_THEME = Theme(
    name="brotkasten",
    primary="#7C70DA",
    secondary="#3A2B8A",
    accent="#EDF171",
    foreground="#D0CCFF",
    background="#3A2B8A",
    surface="#5446B8",
    panel="#241870",
    boost="#FFFFFF",
    warning="#EDF171",
    error="#C46C71",
    success="#A9FF9F",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Boing
# Three-color workbench palette — blue background, white foreground,
# orange accents. The bouncing-ball-demo aesthetic.
# ────────────────────────────────────────────────────────────────────────
BOING_THEME = Theme(
    name="boing",
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
# Gemstone
# White / black / green — the monochrome GEM Desktop look (light).
# ────────────────────────────────────────────────────────────────────────
GEMSTONE_THEME = Theme(
    name="gemstone",
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
# Classic Terminal
# Phosphor-green on black — the archetypal CRT terminal look.
# Subtle green-tinted surface / panel give the phosphor glow,
# so borders are visible without breaking the monochrome feel.
# ────────────────────────────────────────────────────────────────────────
CLASSIC_TERMINAL_THEME = Theme(
    name="classic-terminal",
    primary="#33FF33",
    secondary="#2A7A2A",
    accent="#88FF88",
    foreground="#33FF33",
    background="#0A0A0A",
    surface="#162616",
    panel="#0F1B0F",
    boost="#88FF88",
    warning="#FFAA00",
    error="#FF4444",
    success="#33FF33",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Next
# Dark gray with subtle magenta accents — workstation-era 3D bevels,
# elegant dark interface.
# ────────────────────────────────────────────────────────────────────────
NEXT_THEME = Theme(
    name="next",
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
# BeBox
# Gray with yellow status-bar accent — fast, elegant, ahead of its time.
# ────────────────────────────────────────────────────────────────────────
BEBOX_THEME = Theme(
    name="bebox",
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
# Bunty
# Aubergine / purple with warm orange accents — a soft signature look.
# Toned-down accent + lifted surface so the orange stops shouting.
# ────────────────────────────────────────────────────────────────────────
BUNTY_THEME = Theme(
    name="bunty",
    primary="#DD4814",
    secondary="#77216F",
    accent="#E18B5C",
    foreground="#F2EAEA",
    background="#2C001E",
    surface="#4A2540",
    panel="#1F0014",
    boost="#E18B5C",
    warning="#F99B11",
    error="#DF382C",
    success="#38B44A",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Cupertino
# Clean light gray with blue accents — minimalism (light).
# ────────────────────────────────────────────────────────────────────────
CUPERTINO_THEME = Theme(
    name="cupertino",
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
# Luna
# Blue task-bar with green start button — early-2000s sky-blue UI.
# ────────────────────────────────────────────────────────────────────────
LUNA_THEME = Theme(
    name="luna",
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
# Commandr
# Blue background, white text, bright cyan / yellow highlights — the
# classic 16-color VGA file-manager palette. Yellow is the iconic
# selection / active highlight; cyan the secondary color for column
# headers and borders.
# ────────────────────────────────────────────────────────────────────────
COMMANDR_THEME = Theme(
    name="commandr",
    primary="#FFFF55",
    secondary="#55FFFF",
    accent="#FFFF55",
    foreground="#FFFFFF",
    background="#0000AA",
    surface="#1A1ACC",
    panel="#000077",
    boost="#FFFF55",
    warning="#FFAA00",
    error="#FF5555",
    success="#55FF55",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Plan 9
# Pulpy yellow / blue / green palette — bold, distinctive (light).
# ────────────────────────────────────────────────────────────────────────
PLAN9_THEME = Theme(
    name="plan9",
    primary="#228844",
    secondary="#4488AA",
    accent="#228844",
    foreground="#111111",
    background="#FFFFEA",
    surface="#EAFFFF",
    panel="#D5E8D0",
    boost="#33AA55",
    warning="#BB8800",
    error="#CC2222",
    success="#228844",
    dark=False,
)

# ────────────────────────────────────────────────────────────────────────
# Motif
# Beige / slate-gray corporate Unix toolkit — warm accents on cool gray.
# ────────────────────────────────────────────────────────────────────────
MOTIF_THEME = Theme(
    name="motif",
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
# Warp
# Dark blue with teal accents.
# ────────────────────────────────────────────────────────────────────────
WARP_THEME = Theme(
    name="warp",
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
# Geeko
# Dark green with white — chameleon-mascot palette.
# ────────────────────────────────────────────────────────────────────────
GEEKO_THEME = Theme(
    name="geeko",
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

# ────────────────────────────────────────────────────────────────────────
# Minty
# Warm mint-green on charcoal — Cinnamon-style desktop palette.
# ────────────────────────────────────────────────────────────────────────
MINTY_THEME = Theme(
    name="minty",
    primary="#8BB158",
    secondary="#6DAB76",
    accent="#8BB158",
    foreground="#E8E8E8",
    background="#2B2B2B",
    surface="#363636",
    panel="#232323",
    boost="#9EC46A",
    warning="#E5A50A",
    error="#CC3333",
    success="#8BB158",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Crimson
# Deep red on dark charcoal — bold and corporate.
# ────────────────────────────────────────────────────────────────────────
CRIMSON_THEME = Theme(
    name="crimson",
    primary="#CC0000",
    secondary="#A30000",
    accent="#EE0000",
    foreground="#E0E0E0",
    background="#1A0A0A",
    surface="#2A1515",
    panel="#140808",
    boost="#FF2222",
    warning="#EEA500",
    error="#FF4444",
    success="#44AA44",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Razzy
# Raspberry red on dark slate — playful but high-contrast.
# ────────────────────────────────────────────────────────────────────────
RAZZY_THEME = Theme(
    name="razzy",
    primary="#C51A4A",
    secondary="#6CC24A",
    accent="#C51A4A",
    foreground="#EEEEEE",
    background="#1E1E2E",
    surface="#2A2A3A",
    panel="#181828",
    boost="#DD2A5A",
    warning="#E5A50A",
    error="#DD3333",
    success="#6CC24A",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Beastie
# Daemon red on dark slate — Unix demon mascot palette.
# ────────────────────────────────────────────────────────────────────────
BEASTIE_THEME = Theme(
    name="beastie",
    primary="#AB2B28",
    secondary="#5E8AAA",
    accent="#AB2B28",
    foreground="#D4D4D4",
    background="#1C2028",
    surface="#262A32",
    panel="#161A20",
    boost="#CC3533",
    warning="#CC9933",
    error="#DD4444",
    success="#55AA66",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Fifty-Eight
# Black dial with aged gold lume + bezel red — vintage diver style
# (the iconic 1958 dive-watch look).
# ────────────────────────────────────────────────────────────────────────
FIFTY_EIGHT_THEME = Theme(
    name="fifty-eight",
    primary="#C9A96E",
    secondary="#6A6A6A",
    accent="#9E1B25",
    foreground="#E8C985",
    background="#100C08",
    surface="#1E1914",
    panel="#080605",
    boost="#D9BC80",
    warning="#C9A048",
    error="#B8252E",
    success="#6A9A5A",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Bluesy
# Deep royal blue dial with rich yellow-gold indices, hands, and case.
# (Bluesy is a watch-collector nickname for the iconic gold/blue diver.)
# ────────────────────────────────────────────────────────────────────────
BLUESY_THEME = Theme(
    name="bluesy",
    primary="#D4AF37",
    secondary="#1E4FA0",
    accent="#F0C85A",
    foreground="#F5D76E",
    background="#081F54",
    surface="#0E2E6E",
    panel="#04133A",
    boost="#FFD960",
    warning="#E8A838",
    error="#DD3344",
    success="#48B870",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Goldfinder
# Deep black with 18K gold accents — villain-glamour palette.
# ────────────────────────────────────────────────────────────────────────
GOLDFINDER_THEME = Theme(
    name="goldfinder",
    primary="#E6B800",
    secondary="#8A6E20",
    accent="#FFD740",
    foreground="#E8DFC0",
    background="#080705",
    surface="#18140A",
    panel="#040302",
    boost="#FFE066",
    warning="#E8A838",
    error="#CC4040",
    success="#5AAA5A",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Hulkula
# Vivid green rage with steel-gray edges — gamma-strong contrast,
# secondary cool steel keeps the boldness from going neon.
# ────────────────────────────────────────────────────────────────────────
HULKULA_THEME = Theme(
    name="hulkula",
    primary="#2BA841",
    secondary="#BCC4CA",
    accent="#4DC962",
    foreground="#F0F2EE",
    background="#083C14",
    surface="#104B1B",
    panel="#042608",
    boost="#5FD974",
    warning="#D4A040",
    error="#CC2222",
    success="#4DC962",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Flughund
# Midnight black & moonlit blue — urban-night palette.
# ────────────────────────────────────────────────────────────────────────
FLUGHUND_THEME = Theme(
    name="flughund",
    primary="#244B85",
    secondary="#BCC4CA",
    accent="#3D6FB8",
    foreground="#F0F2F5",
    background="#060810",
    surface="#0E1422",
    panel="#030509",
    boost="#5282D0",
    warning="#D4A040",
    error="#CC3030",
    success="#50AA50",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Classic Navy
# Deep navy dial with silver sub-dials and muted brick-red accents —
# aviation-inspired three-register chronograph feel.
# ────────────────────────────────────────────────────────────────────────
CLASSIC_NAVY_THEME = Theme(
    name="classic-navy",
    primary="#C0C5CC",
    secondary="#1E4585",
    accent="#9E3A42",
    foreground="#EEF0F5",
    background="#0C2B5C",
    surface="#143465",
    panel="#061A3A",
    boost="#D8DCE2",
    warning="#D4A040",
    error="#B04048",
    success="#50AA50",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Brick
# Olive-green LCD handheld — beige-gray case with magenta accents (light).
# ("Brick" is the affectionate community nickname for the original
# DMG-01 form-factor handheld.)
# ────────────────────────────────────────────────────────────────────────
BRICK_THEME = Theme(
    name="brick",
    primary="#8E2A5E",
    secondary="#5A4858",
    accent="#D63B68",
    foreground="#241F28",
    background="#D4CEBC",
    surface="#E2DCCA",
    panel="#B2AC9A",
    boost="#B83470",
    warning="#C85820",
    error="#A0203A",
    success="#4A7A3A",
    dark=False,
)

# ────────────────────────────────────────────────────────────────────────
# Clipper
# Globe blue on ivory — jet-age livery palette (light).
# ────────────────────────────────────────────────────────────────────────
CLIPPER_THEME = Theme(
    name="clipper",
    primary="#1A4FA0",
    secondary="#C61F2C",
    accent="#D4222F",
    foreground="#1A1A1A",
    background="#F6F3E8",
    surface="#FCFAF0",
    panel="#EBE6D4",
    boost="#2A6BC8",
    warning="#C88A20",
    error="#C61F2C",
    success="#2E8B3D",
    dark=False,
)

# ────────────────────────────────────────────────────────────────────────
# Synthwave
# 80s retro-futurism — deep purple with neon pink and electric cyan,
# a sunset-on-a-Lamborghini aesthetic.
# ────────────────────────────────────────────────────────────────────────
SYNTHWAVE_THEME = Theme(
    name="synthwave",
    primary="#FF2E93",
    secondary="#7B2D8E",
    accent="#05D9E8",
    foreground="#F5E9FF",
    background="#1A0B3D",
    surface="#261553",
    panel="#0E0524",
    boost="#FF6EC7",
    warning="#FFD319",
    error="#FF3860",
    success="#39FF14",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Miami
# Pastel 80s — twilight teal with flamingo pink and sunset coral.
# ────────────────────────────────────────────────────────────────────────
MIAMI_THEME = Theme(
    name="miami",
    primary="#FF6FAB",
    secondary="#1FB8BC",
    accent="#FFA06A",
    foreground="#FFE8E0",
    background="#0B2F3F",
    surface="#124050",
    panel="#051825",
    boost="#FF8FC5",
    warning="#FFD76B",
    error="#E63970",
    success="#4ECDA8",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Racing
# Charcoal engine-bay background that lets the signature motorsport
# stripes pop: deep blue, cherry red, silver.
# ────────────────────────────────────────────────────────────────────────
RACING_THEME = Theme(
    name="racing",
    primary="#1A5CC8",
    secondary="#C0C6D0",
    accent="#E42030",
    foreground="#EEF0F5",
    background="#14161E",
    surface="#1F232E",
    panel="#080A10",
    boost="#2E72DC",
    warning="#E8A838",
    error="#E42030",
    success="#3AAA4A",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Metropolis
# Bold primary-color triad: deep blue, crimson red, sun yellow.
# Optimistic city-at-sunrise palette built around the three-color
# combination that classic comic panels and 60s pulp covers loved.
# ────────────────────────────────────────────────────────────────────────
METROPOLIS_THEME = Theme(
    name="metropolis",
    primary="#E02030",
    secondary="#1A5CC8",
    accent="#FFD53B",
    foreground="#F0F2F8",
    background="#0A2A5E",
    surface="#123876",
    panel="#051838",
    boost="#F83040",
    warning="#FFD53B",
    error="#C80A18",
    success="#3AAA4A",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Spiderized
# Red & royal-blue hero suit — high-contrast wallcrawler palette,
# white for the spider-eye lenses, deep night royal-blue as the canvas.
# ────────────────────────────────────────────────────────────────────────
SPIDERIZED_THEME = Theme(
    name="spiderized",
    primary="#D71920",
    secondary="#1F75FE",
    accent="#1F75FE",
    foreground="#FFFFFF",
    background="#0E1A3A",
    surface="#1A2C5F",
    panel="#070D24",
    boost="#FF3344",
    warning="#FFA830",
    error="#C80A18",
    success="#4AA85A",
    dark=True,
)


# ── Convenience collections ────────────────────────────────────────────

RETRO_THEMES: list[Theme] = [
    BROTKASTEN_THEME,
    BOING_THEME,
    GEMSTONE_THEME,
    CLASSIC_TERMINAL_THEME,
    NEXT_THEME,
    BEBOX_THEME,
    BUNTY_THEME,
    CUPERTINO_THEME,
    LUNA_THEME,
    COMMANDR_THEME,
    PLAN9_THEME,
    MOTIF_THEME,
    WARP_THEME,
    GEEKO_THEME,
    MINTY_THEME,
    CRIMSON_THEME,
    RAZZY_THEME,
    BEASTIE_THEME,
    FIFTY_EIGHT_THEME,
    BLUESY_THEME,
    GOLDFINDER_THEME,
    HULKULA_THEME,
    FLUGHUND_THEME,
    CLASSIC_NAVY_THEME,
    BRICK_THEME,
    CLIPPER_THEME,
    SYNTHWAVE_THEME,
    MIAMI_THEME,
    RACING_THEME,
    METROPOLIS_THEME,
    SPIDERIZED_THEME,
]

RETRO_THEME_NAMES: list[str] = [t.name for t in RETRO_THEMES]

THEME_DISPLAY_NAMES: dict[str, str] = {
    "brotkasten": "Brotkasten — Light Blue on Royal Blue",
    "boing": "Boing — Blue/White/Orange Workbench",
    "gemstone": "Gemstone — Monochrome GEM Desktop",
    "classic-terminal": "Classic Terminal — Phosphor Green on Black",
    "next": "Next — Slate Gray with Magenta Accents",
    "bebox": "BeBox — Blue-Gray with Yellow Accent",
    "bunty": "Bunty — Aubergine with Warm Orange Accents",
    "cupertino": "Cupertino — Clean Light Gray with Blue Accents",
    "luna": "Luna — Sky Blue with Green Start Accent",
    "commandr": "Commandr — Blue/Cyan/Yellow File Manager",
    "plan9": "Plan 9 — Pulpy Yellow/Blue/Green",
    "motif": "Motif — Beige Corporate Unix Toolkit",
    "warp": "Warp — Dark Blue with Teal Accents",
    "geeko": "Geeko — Dark Green with White",
    "minty": "Minty — Warm Mint-Green on Charcoal",
    "crimson": "Crimson — Deep Red on Dark Charcoal",
    "razzy": "Razzy — Raspberry Red on Dark Slate",
    "beastie": "Beastie — Daemon Red on Dark Slate",
    "fifty-eight": "Fifty-Eight — Black Dial, Aged Gold Lume & Bezel Red",
    "bluesy": "Bluesy — Royal Blue & Gold",
    "goldfinder": "Goldfinder — Deep Black with 18K Gold Accents",
    "hulkula": "Hulkula — Verdant Green with Steel Edges",
    "flughund": "Flughund — Midnight Black & Moonlit Blue",
    "classic-navy": "Classic Navy",
    "brick": "Brick — Olive-Green Handheld LCD",
    "clipper": "Clipper — Globe Blue on Ivory",
    "synthwave": "Synthwave — 80s Retro-Futurism",
    "miami": "Miami — Twilight Teal, Flamingo Pink & Sunset Coral",
    "racing": "Racing — Charcoal with Blue, Red & Silver Stripes",
    "metropolis": "Metropolis — Bold Blue, Crimson & Sun Yellow",
    "spiderized": "Spiderized — Red & Royal-Blue Hero Suit",
}


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
