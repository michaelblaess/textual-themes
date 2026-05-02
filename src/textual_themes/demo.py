"""Demo app for textual-themes.

A storybook-style theme browser. Every retro theme is registered, the
current theme name is shown in the header, and `n` / `p` cycle through
the list. `Ctrl+S` saves an SVG screenshot of the current theme.

Run:
    python -m textual_themes
"""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, VerticalScroll
from textual.widgets import (
    Button,
    Checkbox,
    DataTable,
    Footer,
    Header,
    Input,
    Markdown,
    ProgressBar,
    RadioButton,
    RadioSet,
    RichLog,
    Static,
    Switch,
    TextArea,
    Tree,
)

from . import __version__
from .themes import RETRO_THEME_NAMES, THEME_DISPLAY_NAMES, register_all

_SAMPLE_MARKDOWN = """\
# Markdown

This **textual-themes** demo registers all retro themes. Each defines:

- `primary`, `secondary`, `accent`
- `foreground`, `background`
- `surface`, `panel`, `boost`
- `warning`, `error`, `success`

> Tip: press **Ctrl+P** for the theme picker, or **n** / **p** to step.

```python
from textual_themes import register_all

class MyApp(App):
    def __init__(self) -> None:
        super().__init__()
        register_all(self)
        self.theme = "c64"
```
"""

_SAMPLE_CODE = '''\
def fibonacci(n: int) -> int:
    """Classic recursive fib — pretty in any theme."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
'''


class ThemeDemoApp(App[None]):
    """Storybook-style demo to browse all retro themes."""

    TITLE = f"textual-themes v{__version__}"

    CSS = """
    Screen {
        layout: vertical;
    }
    #content {
        padding: 0 2 1 2;
    }
    .section-title {
        background: $boost;
        color: $foreground;
        text-style: bold;
        padding: 0 1;
        margin-top: 1;
    }
    .row {
        height: auto;
        margin-top: 1;
    }
    .row Button {
        margin-right: 1;
    }
    .row Checkbox {
        margin-right: 2;
    }
    .row Switch {
        margin-right: 2;
    }
    DataTable {
        height: 8;
        margin-top: 1;
    }
    Tree {
        height: 10;
        margin-top: 1;
    }
    RichLog {
        height: 8;
        margin-top: 1;
        border: solid $accent;
    }
    Markdown {
        margin-top: 1;
    }
    TextArea {
        height: 8;
        margin-top: 1;
    }
    ProgressBar {
        margin-top: 1;
    }
    RadioSet {
        margin-top: 1;
    }
    Input {
        margin-top: 1;
    }
    """

    BINDINGS = [
        Binding("n,N", "next_theme", "Next Theme", key_display="n"),
        Binding("p,P", "prev_theme", "Prev Theme", key_display="p"),
        Binding("ctrl+s", "screenshot", "Screenshot"),
        Binding("q,Q", "quit", "Quit", key_display="q"),
    ]

    def __init__(self, initial_theme: str | None = None) -> None:
        super().__init__()
        register_all(self)
        if initial_theme and initial_theme in RETRO_THEME_NAMES:
            self._initial_theme = initial_theme
        else:
            self._initial_theme = RETRO_THEME_NAMES[0]

    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        with VerticalScroll(id="content"):
            yield Static("Buttons", classes="section-title")
            with Horizontal(classes="row"):
                yield Button("Default", id="btn-default")
                yield Button("Primary", variant="primary", id="btn-primary")
                yield Button("Warning", variant="warning", id="btn-warning")
                yield Button("Error", variant="error", id="btn-error")
            with Horizontal(classes="row"):
                yield Button("Default", id="btn-default-d", disabled=True)
                yield Button(
                    "Primary", variant="primary", id="btn-primary-d", disabled=True
                )
                yield Button(
                    "Warning", variant="warning", id="btn-warning-d", disabled=True
                )
                yield Button(
                    "Error", variant="error", id="btn-error-d", disabled=True
                )

            yield Static("Inputs", classes="section-title")
            yield Input(placeholder="Type something here...", id="input-1")
            yield Input(value="Pre-filled value", id="input-2")
            yield TextArea(_SAMPLE_CODE, language="python", id="ta-1")

            yield Static("Checkboxes, Radios & Switch", classes="section-title")
            with Horizontal(classes="row"):
                yield Checkbox("Enable feature", value=True)
                yield Checkbox("Beta access")
                yield Switch(value=True)
                yield Switch()
            with RadioSet():
                yield RadioButton("Amanda", value=True)
                yield RadioButton("Connor MacLeod")
                yield RadioButton("Duncan MacLeod")

            yield Static("DataTable", classes="section-title")
            yield DataTable(id="dt-1", zebra_stripes=True)

            yield Static("ProgressBar", classes="section-title")
            yield ProgressBar(total=100, show_eta=False, id="pb-1")

            yield Static("Tree", classes="section-title")
            tree: Tree[str] = Tree("Themes", id="tree-1")
            tree.root.expand()
            for name in RETRO_THEME_NAMES:
                tree.root.add_leaf(THEME_DISPLAY_NAMES.get(name, name))
            yield tree

            yield Static("RichLog", classes="section-title")
            yield RichLog(highlight=True, markup=True, id="log-1")

            yield Static("Markdown", classes="section-title")
            yield Markdown(_SAMPLE_MARKDOWN)

        yield Footer()

    def on_mount(self) -> None:
        self.theme = self._initial_theme

        table = self.query_one("#dt-1", DataTable)
        table.add_columns("ID", "Name", "Status", "Score")
        table.add_row("1", "Alice", "Active", "92")
        table.add_row("2", "Bob", "Idle", "78")
        table.add_row("3", "Carol", "Banned", "12")
        table.add_row("4", "Dan", "Active", "65")

        progress = self.query_one("#pb-1", ProgressBar)
        progress.update(progress=42)

        log = self.query_one("#log-1", RichLog)
        log.write("[green]INFO[/green]  Demo app started.")
        log.write("[yellow]WARN[/yellow]  This is a sample warning.")
        log.write("[red]ERROR[/red] Sample error message.")
        log.write(
            "Press [b]n[/b] / [b]p[/b] to switch themes, [b]Ctrl+P[/b] for picker."
        )

    def watch_theme(self, theme_name: str) -> None:
        """Update the header subtitle whenever the theme changes."""
        display = THEME_DISPLAY_NAMES.get(theme_name, theme_name)
        if theme_name in RETRO_THEME_NAMES:
            index = RETRO_THEME_NAMES.index(theme_name) + 1
            total = len(RETRO_THEME_NAMES)
            self.sub_title = f"{display}  ({index}/{total})"
        else:
            self.sub_title = display

    def action_next_theme(self) -> None:
        self._cycle_theme(1)

    def action_prev_theme(self) -> None:
        self._cycle_theme(-1)

    def _cycle_theme(self, step: int) -> None:
        if self.theme not in RETRO_THEME_NAMES:
            self.theme = RETRO_THEME_NAMES[0]
            return
        idx = RETRO_THEME_NAMES.index(self.theme)
        self.theme = RETRO_THEME_NAMES[(idx + step) % len(RETRO_THEME_NAMES)]

    def action_screenshot(self) -> None:
        slug = (self.theme or "screenshot").replace("/", "-")
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"theme-{slug}-{timestamp}.svg"
        self.save_screenshot(str(Path.cwd() / filename))
        self.notify(f"Saved {filename}", title="Screenshot")
