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
    Norton Commander — DOS file manager: blue/cyan/yellow
    Plan 9       — Plan 9 from Bell Labs: yellow/blue/green
    Solaris CDE  — Sun CDE Desktop: beige/teal corporate Unix
    OS/2 Warp    — IBM OS/2 Warp: dark blue/teal
    openSUSE     — openSUSE: dark green/white
    Linux Mint   — Cinnamon Desktop: warm mint-green on charcoal
    Red Hat      — Red Hat Linux: Shadowman red on dark
    Raspberry Pi — Raspberry Pi OS: raspberry red on dark
    FreeBSD      — FreeBSD: Beastie red on dark slate
    Tudor        — Tudor Black Bay 58: black dial with aged gold lume + red bezel triangle
    Bluesy       — Rolex Gold (blue dial): royal blue with rich gold accents
    Goldfinger   — James Bond (1964): black and 18K gold, the villain's signature
    Hulk         — Marvel's Incredible Hulk: vivid green rage with steel-gray edges
    Batman       — DC's Dark Knight: Gotham night sky, black and midnight blue
    Classic Navy — Deep navy dial with silver sub-dials and muted brick-red accents
    Synthwave    — 80s retro-futurism: deep purple with neon pink and electric cyan
    Miami Vice   — Pastel 80s: twilight teal with flamingo pink and sunset coral
    Gulf Racing  — Gulf Oil / Porsche 917: deep Gulf blue with dominant orange stripe
    Martini Racing — Martini livery: charcoal with deep blue, cherry red and silver stripes
    Superman     — DC's Man of Steel: hero blue, cape red and shield yellow
    Spiderman    — Marvel's web-slinger: Spidey red and suit blue on dark web-black
    Pan Am       — Pan American World Airways: the globe blue on ivory white (light)
    Game Boy     — Nintendo Game Boy DMG-01 (1989): olive LCD green (light)
"""
from __future__ import annotations

from typing import TYPE_CHECKING

from textual.theme import Theme

if TYPE_CHECKING:
    from textual.app import App


# ────────────────────────────────────────────────────────────────────────
# C64 — Commodore 64 (1982)
# Blue on light-blue, the classic. PETSCII feeling.
# Pepto-inspired palette: deep blue background, vivid light-blue text,
# lifted surface so widgets pop, yellow accents for highlights.
# ────────────────────────────────────────────────────────────────────────
C64_THEME = Theme(
    name="c64",
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
# Subtle green-tinted surface / panel give the CRT phosphor glow,
# so borders are visible without breaking the monochrome feel.
# ────────────────────────────────────────────────────────────────────────
IBM_TERMINAL_THEME = Theme(
    name="ibm-terminal",
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
# Toned-down accent + lifted surface so the orange stops shouting.
# ────────────────────────────────────────────────────────────────────────
UBUNTU_THEME = Theme(
    name="ubuntu",
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
# Norton Commander (1986)
# Blue background, white text. Yellow is the iconic selection / active
# highlight (like the "Next" button in NC dialogs); cyan is the secondary
# color for column headers and borders. Classic 16-color VGA palette.
# ────────────────────────────────────────────────────────────────────────
MSDOS_THEME = Theme(
    name="msdos",
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
# Plan 9 from Bell Labs (1992)
# Yellow/blue/green — the most distinctive OS palette ever designed.
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


# ────────────────────────────────────────────────────────────────────────
# Linux Mint — Cinnamon Desktop
# Warm mint-green on charcoal — the friendly Linux desktop.
# ────────────────────────────────────────────────────────────────────────
LINUX_MINT_THEME = Theme(
    name="linux-mint",
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
# Red Hat Linux
# The Shadowman's red — enterprise Linux with attitude.
# ────────────────────────────────────────────────────────────────────────
RED_HAT_THEME = Theme(
    name="red-hat",
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
# Raspberry Pi OS
# Raspberry red on dark — the tiny computer's desktop.
# ────────────────────────────────────────────────────────────────────────
RASPBERRY_PI_THEME = Theme(
    name="raspberry-pi",
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
# FreeBSD
# Beastie red on dark slate — the daemon's domain.
# ────────────────────────────────────────────────────────────────────────
FREEBSD_THEME = Theme(
    name="freebsd",
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
# Tudor — Tudor Black Bay 58
# Black dial with aged cream/gold lume patina, steel case, and the
# signature red triangle on the bezel at 12 o'clock.
# ────────────────────────────────────────────────────────────────────────
TUDOR_THEME = Theme(
    name="tudor",
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
# Bluesy — Rolex Gold (blue dial)
# Deep royal blue dial with rich yellow-gold indices, hands, and case.
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
# Goldfinger — James Bond (1964)
# "No, Mr. Bond, I expect you to die." The villain's signature: deep
# black with 18K yellow gold — Auric Goldfinger's gold-obsessed empire.
# ────────────────────────────────────────────────────────────────────────
GOLDFINGER_THEME = Theme(
    name="goldfinger",
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
# Hulk — Marvel's Incredible Hulk
# "HULK SMASH!" Vivid gamma-green rage with steel-gray edges and the
# warning-red of torn fabric. Bruce Banner's unstoppable alter ego.
# ────────────────────────────────────────────────────────────────────────
HULK_THEME = Theme(
    name="hulk",
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
# Batman — DC's Dark Knight
# Gotham at midnight: deep black with the blue-black of a moonlit cape.
# Silver-gray Bat-signal reflections and a touch of utility-belt gold.
# ────────────────────────────────────────────────────────────────────────
BATMAN_THEME = Theme(
    name="batman",
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
# Deep navy background with silver/white highlights and muted brick-red
# accents. Aviation-inspired without tying to a single watch reference.
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
# Game Boy — Nintendo Game Boy DMG-01 (1989)
# The iconic console case — warm beige-gray plastic with the purple
# Nintendo wordmark and magenta A/B buttons. Light theme.
# ────────────────────────────────────────────────────────────────────────
GAMEBOY_THEME = Theme(
    name="gameboy",
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
# Pan Am — Pan American World Airways
# "The world's most experienced airline." The iconic globe-blue logo
# on ivory livery, with the red accent from vintage ticket stock and
# route maps. Light theme.
# ────────────────────────────────────────────────────────────────────────
PAN_AM_THEME = Theme(
    name="pan-am",
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
# Synthwave — 80s retro-futurism
# Deep indigo-purple "night sky" background, neon pink as the main
# signature, electric cyan as the accent, sunset gold for warnings —
# the Outrun / Miami Vice / Kavinsky aesthetic.
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
# Miami Vice — Pastel 80s
# Twilight teal ocean background with flamingo pink as the signature,
# sunset coral accents and mint success. The pastel counterpart to
# Synthwave — more Crockett & Tubbs, less Kavinsky.
# ────────────────────────────────────────────────────────────────────────
MIAMI_VICE_THEME = Theme(
    name="miami-vice",
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
# Gulf Racing — Gulf Oil / Porsche 917
# Le Mans 1970, the Steve McQueen 917 livery: Gulf powder blue is the
# dominant body color, Gulf orange the centre stripe, white the logo
# fields. Two strong colors plus white — exactly that.
# ────────────────────────────────────────────────────────────────────────
GULF_RACING_THEME = Theme(
    name="gulf-racing",
    primary="#F26A1F",
    secondary="#1E5C82",
    accent="#F26A1F",
    foreground="#0E2A40",
    background="#A4D4E8",
    surface="#FFFFFF",
    panel="#7FB8D2",
    boost="#FF8F3C",
    warning="#E58220",
    error="#C72020",
    success="#2D7A3D",
    dark=False,
)

# ────────────────────────────────────────────────────────────────────────
# Martini Racing — Martini & Rossi livery
# Charcoal engine-bay background that lets the signature stripes pop:
# deep Martini blue, cherry red, and pearl silver. Porsche 917, 935,
# Lancia Delta — the stripes of endurance-racing history.
# ────────────────────────────────────────────────────────────────────────
MARTINI_RACING_THEME = Theme(
    name="martini-racing",
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
# Superman — DC's Man of Steel
# The hero-blue suit with red cape and the iconic yellow S-shield.
# Metropolis sunrise — optimism, strength, and that classic red/blue/
# yellow primary-colour triad straight from the comic panels.
# ────────────────────────────────────────────────────────────────────────
SUPERMAN_THEME = Theme(
    name="superman",
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
# Spiderman — Marvel's Web-Slinger
# Classic Peter Parker suit: Marvel red and bright royal blue, NOT the
# black symbiote suit. White for the spider-eye lenses, deep night
# royal-blue as the canvas.
# ────────────────────────────────────────────────────────────────────────
SPIDERMAN_THEME = Theme(
    name="spiderman",
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
    LINUX_MINT_THEME,
    RED_HAT_THEME,
    RASPBERRY_PI_THEME,
    FREEBSD_THEME,
    TUDOR_THEME,
    BLUESY_THEME,
    GOLDFINGER_THEME,
    HULK_THEME,
    BATMAN_THEME,
    CLASSIC_NAVY_THEME,
    GAMEBOY_THEME,
    PAN_AM_THEME,
    SYNTHWAVE_THEME,
    MIAMI_VICE_THEME,
    GULF_RACING_THEME,
    MARTINI_RACING_THEME,
    SUPERMAN_THEME,
    SPIDERMAN_THEME,
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
    "msdos": "Norton Commander",
    "plan9": "Plan 9 — Bell Labs",
    "solaris-cde": "Solaris CDE",
    "os2-warp": "OS/2 Warp",
    "opensuse": "openSUSE",
    "linux-mint": "Linux Mint",
    "red-hat": "Red Hat Linux",
    "raspberry-pi": "Raspberry Pi OS",
    "freebsd": "FreeBSD",
    "tudor": "Tudor — Black Bay 58",
    "bluesy": "Bluesy — Rolex Gold",
    "goldfinger": "Goldfinger — James Bond (1964)",
    "hulk": "Hulk — Marvel's Incredible Hulk",
    "batman": "Batman — DC's Dark Knight",
    "classic-navy": "Classic Navy",
    "gameboy": "Game Boy — Nintendo DMG-01",
    "pan-am": "Pan Am — Pan American World Airways",
    "synthwave": "Synthwave — 80s Retro-Futurism",
    "miami-vice": "Miami Vice — Pastel 80s",
    "gulf-racing": "Gulf Racing — Porsche 917",
    "martini-racing": "Martini Racing",
    "superman": "Superman — DC's Man of Steel",
    "spiderman": "Spiderman — Marvel's Web-Slinger",
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
