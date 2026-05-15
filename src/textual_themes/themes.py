"""Retro color themes for Textual TUI applications.

Each theme is a `textual.theme.Theme` instance that can be registered
with any Textual `App` via `app.register_theme(theme)`.

This package contains 38 themes inspired by classic computers,
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


# ────────────────────────────────────────────────────────────────────────
# Ascot
# Royal-meeting meets Le-Mans paddock: deep British Racing Green with
# a signal-yellow accent and silver secondary, plus a warm beige
# foreground (instead of pure white) that's much easier on the eyes
# during long sessions — the colour of weathered race-card paper.
# ────────────────────────────────────────────────────────────────────────
ASCOT_THEME = Theme(
    name="ascot",
    primary="#F2C200",
    secondary="#C0C5CC",
    accent="#F2C200",
    foreground="#F5EBD2",
    background="#173E2D",
    surface="#1F4E3A",
    panel="#0E2C1E",
    boost="#FFD835",
    warning="#F2C200",
    error="#C81E2A",
    success="#2E7D52",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Joker
# Comic-book Joker palette modelled after the Bronze-Age look —
# royal-purple suit drives the primary buttons, acid-green hair
# (and bowtie) drives the secondary, golden-yellow vest is the
# accent for modal title bars and key highlights. Cream face-
# powder foreground on a dark Gotham-night background; sidebar
# uses a subtler dark purple than the suit so it grounds the
# layout instead of shouting. No red in the title bars — only
# in semantic errors.
# ────────────────────────────────────────────────────────────────────────
JOKER_THEME = Theme(
    name="joker",
    primary="#7B3FB2",
    secondary="#2FCC2F",
    accent="#FFC72C",
    foreground="#F5F0E5",
    background="#0E0824",
    surface="#1F0F3F",
    panel="#2D1758",
    boost="#9555D4",
    warning="#FFC72C",
    error="#DC4040",
    success="#2FCC2F",
    dark=True,
)

# ────────────────────────────────────────────────────────────────────────
# Marley
# Reggae roots palette: black canvas with the green / gold / red
# tricolour. Green is the primary (lion-of-Judah dominance), gold the
# accent (highlights and warnings), red the alert color. Warm cream
# foreground keeps the vibe sun-drenched rather than sterile.
# ────────────────────────────────────────────────────────────────────────
MARLEY_THEME = Theme(
    name="marley",
    primary="#078930",
    secondary="#DA121A",
    accent="#FCDD09",
    foreground="#F5EFD8",
    # Warmes Fast-Schwarz statt neutralem #0A0A0A — passt zur
    # sun-drenched Palette und kollidiert nicht mit classic-terminal.
    background="#0C0A06",
    surface="#181818",
    panel="#050505",
    boost="#0AA63D",
    warning="#FCDD09",
    error="#DA121A",
    success="#078930",
    dark=True,
)


# ── Convenience collections ────────────────────────────────────────────

# ────────────────────────────────────────────────────────────────────────
# Lenseflare
# 80s Spielberg / Stranger-Things / Poltergeist atmospheric night —
# the iconic orange-teal lens-flare bichromatic on a deep twilight
# blue sky, with a Stranger-Things red accent for dramatic title
# bars. Warm amber drives the buttons (warm lens-flare side); cool
# teal handles success and secondary states (the cold counter-glow).
# Cream foreground keeps that tungsten-light glow on the suburban
# 80s night palette.
# ────────────────────────────────────────────────────────────────────────
LENSEFLARE_THEME = Theme(
    name="lenseflare",
    primary="#FF8C42",
    secondary="#2BD0E0",
    accent="#E5283A",
    foreground="#F0E5D2",
    background="#0A1226",
    surface="#14213D",
    panel="#060B18",
    boost="#FFA85C",
    warning="#FFB838",
    error="#E5283A",
    success="#2BD0E0",
    dark=True,
    variables={
        # Cool teal scrollbars instead of the muddy orange-brown that the
        # orange primary blends into on the dark twilight background.
        "scrollbar": "#1C4F5C",
        "scrollbar-hover": "#2BD0E0",
        "scrollbar-active": "#2BD0E0",
        # Muted teal selection highlight instead of brown (Tree/OptionList).
        "block-cursor-background": "#2E7E8A",
        "block-cursor-foreground": "#0A1226",
        "block-cursor-text-style": "bold",
        "block-cursor-blurred-background": "#1C4F5C",
        "block-cursor-blurred-foreground": "#F0E5D2",
        # Footer: lifted twilight-blue panel so the accent keys read against
        # it instead of disappearing on the near-black default panel.
        "footer-background": "#14213D",
    },
)


# ────────────────────────────────────────────────────────────────────────
# Platoon
# Muted military olive-drab palette — jungle olive primary, deep
# sepia-olive secondary and a warm khaki accent on a near-black
# canvas. Field-gear gold for warnings, a desaturated napalm red for
# errors. Born from the random theme generator, then hand-tuned away
# from neon lime toward authentic olive-drab uniform cloth.
# ────────────────────────────────────────────────────────────────────────
PLATOON_THEME = Theme(
    name="platoon",
    primary="#9AA04A",
    secondary="#6F8A3C",
    accent="#C7B06A",
    foreground="#E4E0CF",
    background="#12130B",
    surface="#22241A",
    panel="#3A3D22",
    boost="#AEB56A",
    warning="#E0B330",
    error="#BF3B2A",
    success="#6F9A4A",
    dark=True,
    variables={
        # Visible mid-olive scrollbars — the olive primary blended onto the
        # near-black background otherwise sinks completely out of sight.
        "scrollbar": "#666B38",
        "scrollbar-hover": "#8A9048",
        "scrollbar-active": "#C7B06A",
        # Footer: lifted olive bar so it reads as a distinct band.
        "footer-background": "#474C28",
    },
)


# ────────────────────────────────────────────────────────────────────────
# Corleone
# Cold mafia-noir palette — smoke-and-shadow night. A faintly bluish
# near-black canvas keeps it cold and melancholic; bronze (not yellow
# gold) drives the buttons, cold steel-grey handles secondary states,
# and an ash-cream foreground stays deliberately unglamorous. Oxblood
# red for errors, field amber for warnings. A quiet, somber theme.
# ────────────────────────────────────────────────────────────────────────
CORLEONE_THEME = Theme(
    name="corleone",
    primary="#A88B52",
    secondary="#4A4E58",
    accent="#9A8147",
    foreground="#C3C0B4",
    background="#0B0C0E",
    surface="#16181C",
    panel="#1F2228",
    boost="#C0A263",
    warning="#B89043",
    error="#8C2F2F",
    success="#5E7355",
    dark=True,
    variables={
        # Cold-grey scrollbars — the bronze primary blended onto the near-
        # black background would otherwise sink out of sight.
        "scrollbar": "#3A3D44",
        "scrollbar-hover": "#5A5E68",
        "scrollbar-active": "#A88B52",
        # Footer: lifted slate bar so it reads as a distinct band.
        "footer-background": "#22252C",
    },
)


# ────────────────────────────────────────────────────────────────────────
# Golden Brown
# Warm mafia-noir counterpart to Corleone — a tungsten-lit night
# instead of a cold one. Antique gold drives the buttons, sepia brown
# handles secondary states, and an aged-parchment foreground glows on
# a warm near-black canvas. Oxblood red for errors, amber for
# warnings. The warm, smoky, cigar-lounge half of the noir pair.
# ────────────────────────────────────────────────────────────────────────
GOLDEN_BROWN_THEME = Theme(
    name="golden-brown",
    primary="#A8843F",
    secondary="#6E4E36",
    accent="#C29A4E",
    foreground="#D5C5A4",
    background="#0F0B07",
    surface="#1C1611",
    panel="#2B2018",
    boost="#D2AC66",
    warning="#BE8F39",
    error="#9A2B2B",
    success="#5F6B42",
    dark=True,
    variables={
        # Visible gold-brown scrollbars — the gold primary blended onto the
        # warm near-black background otherwise sinks out of sight.
        "scrollbar": "#5A4A2C",
        "scrollbar-hover": "#8A7038",
        "scrollbar-active": "#C29A4E",
        # Footer: lifted sepia bar so it reads as a distinct band.
        "footer-background": "#352819",
    },
)


# Kept alphabetically sorted by theme name — new themes must be inserted
# in order, not appended.
RETRO_THEMES: list[Theme] = [
    ASCOT_THEME,
    BEASTIE_THEME,
    BEBOX_THEME,
    BLUESY_THEME,
    BOING_THEME,
    BRICK_THEME,
    BROTKASTEN_THEME,
    BUNTY_THEME,
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
    SPIDERIZED_THEME,
    SYNTHWAVE_THEME,
    WARP_THEME,
]

RETRO_THEME_NAMES: list[str] = [t.name for t in RETRO_THEMES]

# Kept alphabetically sorted by theme name — new entries go in order.
THEME_DISPLAY_NAMES: dict[str, str] = {
    "ascot": "Ascot — Racing Green with Yellow, Silver & Beige Text",
    "beastie": "Beastie — Daemon Red on Dark Slate",
    "bebox": "BeBox — Blue-Gray with Yellow Accent",
    "bluesy": "Bluesy — Royal Blue & Gold",
    "boing": "Boing — Blue/White/Orange Workbench",
    "brick": "Brick — Olive-Green Handheld LCD",
    "brotkasten": "Brotkasten — Light Blue on Royal Blue",
    "bunty": "Bunty — Aubergine with Warm Orange Accents",
    "classic-navy": "Classic Navy",
    "classic-terminal": "Classic Terminal — Phosphor Green on Black",
    "clipper": "Clipper — Globe Blue on Ivory",
    "commandr": "Commandr — Blue/Cyan/Yellow File Manager",
    "corleone": "Corleone — Cold Noir Bronze & Steel",
    "crimson": "Crimson — Deep Red on Dark Charcoal",
    "cupertino": "Cupertino — Clean Light Gray with Blue Accents",
    "fifty-eight": "Fifty-Eight — Black Dial, Aged Gold Lume & Bezel Red",
    "flughund": "Flughund — Midnight Black & Moonlit Blue",
    "geeko": "Geeko — Dark Green with White",
    "gemstone": "Gemstone — Monochrome GEM Desktop",
    "golden-brown": "Golden Brown — Warm Gold & Sepia Noir",
    "goldfinder": "Goldfinder — Deep Black with 18K Gold Accents",
    "hulkula": "Hulkula — Verdant Green with Steel Edges",
    "joker": "Joker — Royal Purple Suit, Acid Green Hair & Yellow Vest",
    "lenseflare": "Lenseflare — 80s Orange-Teal on Twilight Blue",
    "luna": "Luna — Sky Blue with Green Start Accent",
    "marley": "Marley — Reggae Black, Green, Gold & Red",
    "metropolis": "Metropolis — Bold Blue, Crimson & Sun Yellow",
    "miami": "Miami — Twilight Teal, Flamingo Pink & Sunset Coral",
    "minty": "Minty — Warm Mint-Green on Charcoal",
    "motif": "Motif — Beige Corporate Unix Toolkit",
    "next": "Next — Slate Gray with Magenta Accents",
    "plan9": "Plan 9 — Pulpy Yellow/Blue/Green",
    "platoon": "Platoon — Jungle Olive Drab & Khaki",
    "racing": "Racing — Charcoal with Blue, Red & Silver Stripes",
    "razzy": "Razzy — Raspberry Red on Dark Slate",
    "spiderized": "Spiderized — Red & Royal-Blue Hero Suit",
    "synthwave": "Synthwave — 80s Retro-Futurism",
    "warp": "Warp — Dark Blue with Teal Accents",
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
