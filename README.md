# textual-themes

Retro color themes for [Textual](https://textual.textualize.io/) TUI applications.

32 carefully crafted themes inspired by classic computers, operating systems, iconic wristwatches, 80s retro-futurism, motorsport liveries, and comic-book heroes.

## Themes

### Dark Themes

| Theme | Inspiration | Style |
|-------|-------------|-------|
| **C64** | Commodore 64 (1982) | Blue on light-blue, the PETSCII classic |
| **Amiga** | Workbench 1.3 (1987) | Blue/white/orange three-color scheme |
| **IBM Terminal** | IBM 3278 (1970s) | Phosphor-green on black |
| **NeXTSTEP** | NeXTSTEP (1989) | Dark gray with purple accents |
| **BeOS** | BeOS (1995) | Blue-gray with yellow Deskbar accent |
| **Ubuntu** | Ubuntu Desktop | Aubergine/purple with orange accents |
| **Windows XP** | Windows XP Luna (2001) | Blue taskbar with green Start button |
| **MS-DOS** | Norton Commander (1986) | Blue/cyan/yellow file manager |
| **OS/2 Warp** | IBM OS/2 Warp (1994) | Dark blue with teal accents |
| **openSUSE** | openSUSE Linux | Dark green with white |
| **Solaris CDE** | Sun CDE Desktop (1993) | Slate gray with warm accents |
| **Linux Mint** | Cinnamon Desktop | Warm mint-green on charcoal |
| **Red Hat** | Red Hat Linux | Shadowman red on dark |
| **Raspberry Pi** | Raspberry Pi OS | Raspberry red on dark blue-gray |
| **FreeBSD** | FreeBSD | Beastie red on dark slate |
| **Tudor** | Tudor Black Bay 58 | Aged gold lume on black with bezel-red accent |
| **Bluesy** | Rolex Submariner Yellow Gold | Rich yellow gold on deep royal blue |
| **Goldfinger** | James Bond (1964) | Deep black with 18K gold — the villain's signature |
| **Hulk** | Marvel's Incredible Hulk | Gamma-green rage with steel-gray edges |
| **Batman** | DC's Dark Knight | Gotham midnight — black with moonlit blue |
| **Superman** | DC's Man of Steel | Hero-blue suit with cape red and shield yellow |
| **Spiderman** | Marvel's Web-Slinger | Spidey red and suit blue on web-black |
| **Classic Navy** | Aviation-inspired | Deep navy with silver highlights and muted brick-red accents |
| **Synthwave** | 80s retro-futurism | Deep indigo with neon pink, electric cyan and sunset gold |
| **Miami Vice** | Pastel 80s TV | Twilight teal with flamingo pink and sunset coral |
| **Gulf Racing** | Gulf Oil / Porsche 917 | Deep Gulf blue body with dominant orange centre stripe |
| **Martini Racing** | Martini & Rossi livery | Charcoal with deep blue, cherry red and silver stripes |

### Light Themes

| Theme | Inspiration | Style |
|-------|-------------|-------|
| **Atari ST** | GEM Desktop (1985) | White/black/green, monochrome feel |
| **macOS** | macOS (modern) | Clean light gray with blue accents |
| **Plan 9** | Plan 9 from Bell Labs (1992) | Pale yellow/blue with green accents |
| **Pan Am** | Pan American World Airways | The iconic globe blue on ivory livery |
| **Game Boy** | Nintendo Game Boy DMG-01 (1989) | Beige-gray case with purple wordmark and magenta buttons |

## Installation

```bash
pip install git+https://github.com/michaelblaess/textual-themes.git
```

## Quick Start

```python
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

from textual_themes import register_all

class MyApp(App):
    BINDINGS = [("t", "next_theme", "Theme")]

    def __init__(self):
        super().__init__()
        register_all(self)
        self.theme = "c64"

    def compose(self) -> ComposeResult:
        yield Header()
        yield Static("Hello from the past!")
        yield Footer()

    def action_next_theme(self):
        from textual_themes import RETRO_THEME_NAMES
        names = RETRO_THEME_NAMES
        idx = names.index(self.theme) if self.theme in names else -1
        self.theme = names[(idx + 1) % len(names)]

MyApp().run()
```

## Usage

### Register all themes at once

```python
from textual_themes import register_all

class MyApp(App):
    def __init__(self):
        super().__init__()
        register_all(self)       # registers all 32 themes
        self.theme = "amiga"     # pick one
```

### Register individual themes

```python
from textual_themes import C64_THEME, IBM_TERMINAL_THEME

class MyApp(App):
    def __init__(self):
        super().__init__()
        self.register_theme(C64_THEME)
        self.register_theme(IBM_TERMINAL_THEME)
        self.theme = "ibm-terminal"
```

### Available constants

```python
from textual_themes import (
    # Individual Theme objects
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

    # Collections
    RETRO_THEMES,          # list[Theme] — all 32 themes
    RETRO_THEME_NAMES,     # list[str]   — ["c64", "amiga", ...]
    THEME_DISPLAY_NAMES,   # dict[str, str] — {"c64": "C64 — Commodore 64", ...}

    # Helper
    register_all,          # register_all(app) — registers all themes
)
```

### Theme names

Use these names with `app.theme = "..."`:

| Name | Theme |
|------|-------|
| `c64` | Commodore 64 |
| `amiga` | Amiga Workbench 1.3 |
| `atari-st` | Atari ST GEM Desktop |
| `ibm-terminal` | IBM Terminal |
| `nextstep` | NeXTSTEP |
| `beos` | BeOS |
| `ubuntu` | Ubuntu |
| `macos` | macOS |
| `windows-xp` | Windows XP Luna |
| `msdos` | MS-DOS / Norton Commander |
| `plan9` | Plan 9 from Bell Labs |
| `solaris-cde` | Solaris CDE |
| `os2-warp` | OS/2 Warp |
| `opensuse` | openSUSE |
| `linux-mint` | Linux Mint |
| `red-hat` | Red Hat Linux |
| `raspberry-pi` | Raspberry Pi OS |
| `freebsd` | FreeBSD |
| `tudor` | Tudor Black Bay 58 |
| `bluesy` | Rolex Submariner Yellow Gold Blue |
| `goldfinger` | Goldfinger — James Bond (1964) |
| `hulk` | Hulk — Marvel's Incredible Hulk |
| `batman` | Batman — DC's Dark Knight |
| `superman` | Superman — DC's Man of Steel |
| `spiderman` | Spiderman — Marvel's Web-Slinger |
| `classic-navy` | Classic Navy |
| `gameboy` | Nintendo Game Boy DMG-01 |
| `pan-am` | Pan American World Airways |
| `synthwave` | Synthwave — 80s Retro-Futurism |
| `miami-vice` | Miami Vice — Pastel 80s |
| `gulf-racing` | Gulf Racing — Porsche 917 |
| `martini-racing` | Martini Racing |

## Requirements

- Python >= 3.12
- Textual >= 0.85

## License

Apache License 2.0 — see [LICENSE](LICENSE).
