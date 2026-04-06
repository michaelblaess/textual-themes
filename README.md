# textual-themes

Retro color themes for [Textual](https://textual.textualize.io/) TUI applications.

14 carefully crafted themes inspired by classic computers and operating systems.

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

### Light Themes

| Theme | Inspiration | Style |
|-------|-------------|-------|
| **Atari ST** | GEM Desktop (1985) | White/black/green, monochrome feel |
| **macOS** | macOS (modern) | Clean light gray with blue accents |
| **Plan 9** | Plan 9 from Bell Labs (1992) | Pale yellow/blue with green accents |

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
        register_all(self)       # registers all 14 themes
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

    # Collections
    RETRO_THEMES,          # list[Theme] — all 14 themes
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

## Requirements

- Python >= 3.12
- Textual >= 0.85

## License

Apache License 2.0 — see [LICENSE](LICENSE).
