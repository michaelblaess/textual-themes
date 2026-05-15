"""Demo app for textual-themes.

A storybook-style theme browser. Every retro theme is registered, the
current theme name is shown in the header, `n` / `p` cycle through
the list, and the content is organised in tabs (Overview first, then
Buttons / Inputs / Forms / Data / Text).

A built-in random theme generator (`r` / `Ctrl+R` / `Ctrl+D`) and JSON
persistence (`s` to save) let users sketch new palettes interactively.
Saved themes live in `~/.textual-themes/saved/` and are auto-loaded
on startup as a third "Saved" sidebar group.

Run:
    python -m textual_themes
"""

from __future__ import annotations

from pathlib import Path

from rich.text import Text
from textual.app import App, ComposeResult, RenderResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.screen import ModalScreen
from textual.widgets import (
    Button,
    Checkbox,
    DataTable,
    DirectoryTree,
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
    TabbedContent,
    TabPane,
    TextArea,
    Tree,
)
from textual_widgets import HorizontalSplitter, VerticalSplitter

_HANDLE_SIZE = 4
_V_HANDLE = "┊"
_V_LINE = "│"
_H_HANDLE = "┄"
_H_LINE = "─"


class BorderedVerticalSplitter(VerticalSplitter):
    """VerticalSplitter that draws a continuous border line when its
    `with-border` class is active. Handle stays centered, the rest of
    the splitter column becomes a solid │ line."""

    def render(self) -> RenderResult:
        h = max(1, self.size.height)
        handle_n = min(_HANDLE_SIZE, h)
        pad_top = (h - handle_n) // 2
        line_char = _V_LINE if self.has_class("with-border") else " "
        return "\n".join(_V_HANDLE if pad_top <= i < pad_top + handle_n else line_char for i in range(h))


class BorderedHorizontalSplitter(HorizontalSplitter):
    """HorizontalSplitter analogue — draws a continuous ─ line when
    `with-border` is active, handle stays centered."""

    def render(self) -> RenderResult:
        w = max(1, self.size.width)
        handle_n = min(_HANDLE_SIZE, w)
        pad_left = (w - handle_n) // 2
        pad_right = w - handle_n - pad_left
        line_char = _H_LINE if self.has_class("with-border") else " "
        return line_char * pad_left + _H_HANDLE * handle_n + line_char * pad_right


from . import __version__
from .generator import (
    generate_random_theme,
    load_saved_themes,
    save_theme,
)
from .themes import (
    RETRO_THEME_NAMES,
    RETRO_THEMES,
    THEME_DISPLAY_NAMES,
    register_all,
)

_SAMPLE_MARKDOWN = """\
# Markdown

This **textual-themes** demo registers all retro themes. Each defines:

- `primary`, `secondary`, `accent`
- `foreground`, `background`
- `surface`, `panel`, `boost`
- `warning`, `error`, `success`

> Tip: press **Ctrl+P** for the theme picker, **n** / **p** to step,
> or **a** to open a sample About modal in the current theme.

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


class AboutModalScreen(ModalScreen[None]):
    """Showcases how a typical About / dialog looks in the current theme.

    Renders title bar, body text, and a button row so that surface,
    accent, border and button variants can be inspected together.
    """

    DEFAULT_CSS = """
    AboutModalScreen {
        align: center middle;
    }
    AboutModalScreen > VerticalScroll {
        width: auto;
        height: auto;
        min-width: 50;
        max-width: 80;
        max-height: 90%;
        background: $surface;
        border: thick $accent;
        padding: 1 2;
    }
    AboutModalScreen #modal-title {
        height: 3;
        content-align: center middle;
        text-style: bold;
        background: $accent;
        color: auto;
        margin-bottom: 1;
    }
    AboutModalScreen #modal-content {
        height: auto;
        padding: 1 2;
    }
    AboutModalScreen .button-row {
        height: auto;
        margin-top: 1;
        align: center middle;
    }
    AboutModalScreen Button {
        margin: 0 1;
    }
    AboutModalScreen #modal-footer {
        height: 1;
        content-align: center middle;
        color: $text-muted;
        margin-top: 1;
    }
    """

    BINDINGS = [
        Binding("escape", "close", "Close"),
        Binding("a,A", "close", "Close", key_display="a"),
    ]

    def __init__(self, theme_display: str) -> None:
        super().__init__()
        self._theme_display = theme_display

    def compose(self) -> ComposeResult:
        with VerticalScroll():
            yield Static("About textual-themes", id="modal-title")
            yield Static(self._build_content(), id="modal-content")
            with Horizontal(classes="button-row"):
                yield Button("OK", variant="primary", id="btn-modal-ok")
                yield Button("Cancel", id="btn-modal-cancel")
            yield Static("ESC or A to close", id="modal-footer")

    def _build_content(self) -> Text:
        text = Text()
        text.append(f"v{__version__}", style="bold")
        text.append(" by Michael Blaess\n\n")
        text.append("35 retro color themes for Textual TUI applications.\n\n")
        text.append("Active theme:\n", style="dim")
        text.append(f"    {self._theme_display}\n\n", style="bold")
        text.append(
            "This dialog renders in the current theme, so you can\n"
            "inspect how surface, accent border, primary button and\n"
            "default button variants combine.\n",
        )
        return text

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id in ("btn-modal-ok", "btn-modal-cancel"):
            self.dismiss(None)

    def action_close(self) -> None:
        self.dismiss(None)


class ThemeOpenScreen(ModalScreen[Path | None]):
    """File-picker modal for importing theme JSON files.

    Starts in `~/.textual-themes/saved/` (or home if missing). Clicking
    a .json file dismisses the modal with the file path; the parent app
    then imports + registers the theme.
    """

    DEFAULT_CSS = """
    ThemeOpenScreen {
        align: center middle;
    }
    ThemeOpenScreen > Vertical {
        width: 80;
        height: 30;
        background: $surface;
        border: thick $accent;
        padding: 1 2;
    }
    ThemeOpenScreen #open-title {
        height: 3;
        content-align: center middle;
        text-style: bold;
        background: $accent;
        color: auto;
        margin-bottom: 1;
    }
    ThemeOpenScreen DirectoryTree {
        height: 1fr;
        background: $surface;
    }
    ThemeOpenScreen #open-hint {
        height: 1;
        color: $text-muted;
        margin-top: 1;
    }
    ThemeOpenScreen .button-row {
        height: 3;
        margin-top: 1;
        align: center middle;
    }
    ThemeOpenScreen Button {
        margin: 0 1;
    }
    """

    BINDINGS = [
        Binding("escape", "cancel", "Cancel"),
    ]

    def __init__(self, start_dir: Path) -> None:
        super().__init__()
        self._start_dir = start_dir

    def compose(self) -> ComposeResult:
        with Vertical():
            yield Static("Open Theme JSON", id="open-title")
            yield DirectoryTree(str(self._start_dir))
            yield Static(
                "Click a .json file to import it as a theme",
                id="open-hint",
            )
            with Horizontal(classes="button-row"):
                yield Button("Cancel", id="btn-open-cancel")

    def on_directory_tree_file_selected(
        self,
        event: DirectoryTree.FileSelected,
    ) -> None:
        if event.path.suffix.lower() == ".json":
            self.dismiss(event.path)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "btn-open-cancel":
            self.dismiss(None)

    def action_cancel(self) -> None:
        self.dismiss(None)


class ThemeDemoApp(App[None]):
    """Storybook-style demo to browse all retro themes."""

    TITLE = f"textual-themes v{__version__}"

    CSS = """
    Screen {
        layout: vertical;
    }
    #main {
        height: 4fr;
        min-height: 10;
        layout: horizontal;
    }
    #sidebar {
        width: 36;
        min-width: 28;
        background: $panel;
    }
    #theme-tree {
        height: 1fr;
        padding: 1;
        background: $panel;
    }
    #content {
        width: 1fr;
    }
    #content TabPane {
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
    #tree-demo, #tree-demo-o {
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
    VerticalSplitter {
        width: 1;
        background: $panel;
        color: $accent;
    }
    VerticalSplitter:hover, VerticalSplitter.-dragging {
        background: $accent;
        color: $background;
    }
    #log-splitter {
        background: $panel;
        color: $accent;
        display: block;
    }
    #log-splitter:hover, #log-splitter.-dragging {
        background: $accent;
        color: $background;
    }
    #log-splitter.hidden {
        display: none;
    }
    #log-panel {
        height: 1fr;
        min-height: 5;
        max-height: 40;
        background: $surface;
        display: block;
    }
    #log-panel.hidden {
        display: none;
    }
    """

    BINDINGS = [
        Binding("n,N", "next_theme", "Next Theme", key_display="n"),
        Binding("p,P", "prev_theme", "Prev Theme", key_display="p"),
        Binding("a,A", "show_modal", "About / Modal", key_display="a"),
        Binding("r,R", "random_theme", "Random", key_display="r"),
        Binding("ctrl+r", "random_light", "Random Light"),
        Binding("ctrl+d", "random_dark", "Random Dark"),
        Binding("s,S", "save_theme", "Save Theme", key_display="s"),
        Binding("l,L", "toggle_log", "Toggle Log", key_display="l"),
        Binding("c,C", "copy_log", "Copy Log", key_display="c"),
        Binding("b,B", "toggle_border", "Sidebar Border", key_display="b"),
        Binding("o,O", "reload_themes", "Reload Saved", key_display="o"),
        Binding("ctrl+o", "open_theme", "Open Theme File"),
        Binding("ctrl+s", "screenshot", "Screenshot"),
        Binding("q,Q", "quit", "Quit", key_display="q"),
    ]

    def __init__(self, initial_theme: str | None = None) -> None:
        super().__init__()
        register_all(self)
        # Load any previously saved generator-themes from disk
        self._saved_themes = load_saved_themes()
        for theme in self._saved_themes:
            self.register_theme(theme)
        # Build a full list of theme names that the app knows
        self._all_theme_names: list[str] = list(RETRO_THEME_NAMES) + [t.name for t in self._saved_themes]
        if initial_theme and initial_theme in self._all_theme_names:
            self._initial_theme = initial_theme
        else:
            self._initial_theme = RETRO_THEME_NAMES[0]
        # Cache last generated theme so it can be saved without scanning
        self._last_generated_name: str | None = None
        # Plain-text mirror of the log panel for copy-to-clipboard
        self._log_history: list[str] = []

    def compose(self) -> ComposeResult:
        yield Header(show_clock=False)
        with Horizontal(id="main"):
            with VerticalScroll(id="sidebar"):
                yield self._build_theme_tree()
            yield BorderedVerticalSplitter(
                target_id="sidebar",
                min_size=20,
                id="vsplitter",
            )
            with TabbedContent(id="content", initial="tab-overview"):
                with TabPane("Overview", id="tab-overview"), VerticalScroll():
                    yield from self._compose_overview_tab()
                with TabPane("Buttons", id="tab-buttons"), VerticalScroll():
                    yield from self._compose_buttons_tab()
                with TabPane("Inputs", id="tab-inputs"), VerticalScroll():
                    yield from self._compose_inputs_tab()
                with TabPane("Forms", id="tab-forms"), VerticalScroll():
                    yield from self._compose_forms_tab()
                with TabPane("Data", id="tab-data"), VerticalScroll():
                    yield from self._compose_data_tab()
                with TabPane("Text", id="tab-text"), VerticalScroll():
                    yield from self._compose_text_tab()
        yield BorderedHorizontalSplitter(
            target_id="main",
            min_size=10,
            id="log-splitter",
            classes="hidden",
        )
        yield RichLog(
            highlight=True,
            markup=True,
            id="log-panel",
            classes="hidden",
        )
        yield Footer()

    def _compose_overview_tab(self) -> ComposeResult:
        """Full storybook in one scroll — for at-a-glance theme inspection."""
        yield Static("Buttons", classes="section-title")
        with Horizontal(classes="row"):
            yield Button("Default", id="btn-default-o")
            yield Button("Primary", variant="primary", id="btn-primary-o")
            yield Button("Warning", variant="warning", id="btn-warning-o")
            yield Button("Error", variant="error", id="btn-error-o")
        with Horizontal(classes="row"):
            yield Button("Default", id="btn-default-od", disabled=True)
            yield Button("Primary", variant="primary", id="btn-primary-od", disabled=True)
            yield Button("Warning", variant="warning", id="btn-warning-od", disabled=True)
            yield Button("Error", variant="error", id="btn-error-od", disabled=True)

        yield Static("Inputs", classes="section-title")
        yield Input(placeholder="Type something here...", id="input-1o")
        yield Input(value="Pre-filled value", id="input-2o")
        yield TextArea(_SAMPLE_CODE, language="python", id="ta-1o")

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
        yield DataTable(id="dt-1o", zebra_stripes=True)
        yield Static("ProgressBar", classes="section-title")
        yield ProgressBar(total=100, show_eta=False, id="pb-1o")

        yield Static("Tree", classes="section-title")
        demo_tree: Tree[str] = Tree("My Project", id="tree-demo-o")
        demo_tree.root.expand()
        src_node = demo_tree.root.add("src", expand=True)
        src_node.add_leaf("app.py")
        src_node.add_leaf("models.py")
        src_node.add_leaf("widgets.py")
        docs_node = demo_tree.root.add("docs")
        docs_node.add_leaf("README.md")
        docs_node.add_leaf("CHANGELOG.md")
        demo_tree.root.add_leaf("pyproject.toml")
        yield demo_tree

        yield Static("Markdown", classes="section-title")
        yield Markdown(_SAMPLE_MARKDOWN)

    def _compose_buttons_tab(self) -> ComposeResult:
        yield Static("Enabled", classes="section-title")
        with Horizontal(classes="row"):
            yield Button("Default", id="btn-default")
            yield Button("Primary", variant="primary", id="btn-primary")
            yield Button("Warning", variant="warning", id="btn-warning")
            yield Button("Error", variant="error", id="btn-error")
        yield Static("Disabled", classes="section-title")
        with Horizontal(classes="row"):
            yield Button("Default", id="btn-default-d", disabled=True)
            yield Button("Primary", variant="primary", id="btn-primary-d", disabled=True)
            yield Button("Warning", variant="warning", id="btn-warning-d", disabled=True)
            yield Button("Error", variant="error", id="btn-error-d", disabled=True)

    def _compose_inputs_tab(self) -> ComposeResult:
        yield Static("Input", classes="section-title")
        yield Input(placeholder="Type something here...", id="input-1")
        yield Static("Pre-filled", classes="section-title")
        yield Input(value="Pre-filled value", id="input-2")
        yield Static("TextArea", classes="section-title")
        yield TextArea(_SAMPLE_CODE, language="python", id="ta-1")

    def _compose_forms_tab(self) -> ComposeResult:
        yield Static("Checkboxes & Switches", classes="section-title")
        with Horizontal(classes="row"):
            yield Checkbox("Enable feature", value=True)
            yield Checkbox("Beta access")
            yield Switch(value=True)
            yield Switch()
        yield Static("Radio Set", classes="section-title")
        with RadioSet():
            yield RadioButton("Amanda", value=True)
            yield RadioButton("Connor MacLeod")
            yield RadioButton("Duncan MacLeod")

    def _compose_data_tab(self) -> ComposeResult:
        yield Static("DataTable", classes="section-title")
        yield DataTable(id="dt-1", zebra_stripes=True)
        yield Static("ProgressBar", classes="section-title")
        yield ProgressBar(total=100, show_eta=False, id="pb-1")
        yield Static("Tree", classes="section-title")
        demo_tree: Tree[str] = Tree("My Project", id="tree-demo")
        demo_tree.root.expand()
        src_node = demo_tree.root.add("src", expand=True)
        src_node.add_leaf("app.py")
        src_node.add_leaf("models.py")
        src_node.add_leaf("widgets.py")
        docs_node = demo_tree.root.add("docs")
        docs_node.add_leaf("README.md")
        docs_node.add_leaf("CHANGELOG.md")
        demo_tree.root.add_leaf("pyproject.toml")
        yield demo_tree

    def _compose_text_tab(self) -> ComposeResult:
        yield Static("RichLog", classes="section-title")
        yield RichLog(highlight=True, markup=True, id="log-1")
        yield Static("Markdown", classes="section-title")
        yield Markdown(_SAMPLE_MARKDOWN)

    def _build_theme_tree(self) -> Tree[str]:
        """Sidebar tree: themes grouped by Dark / Light / Saved."""
        tree: Tree[str] = Tree("Themes", id="theme-tree")
        tree.show_root = False
        tree.guide_depth = 2

        dark_themes = [t for t in RETRO_THEMES if t.dark]
        light_themes = [t for t in RETRO_THEMES if not t.dark]

        dark_node = tree.root.add(f"Dark  ({len(dark_themes)})", expand=True)
        for theme in dark_themes:
            dark_node.add_leaf(
                THEME_DISPLAY_NAMES.get(theme.name, theme.name),
                data=theme.name,
            )

        light_node = tree.root.add(f"Light  ({len(light_themes)})", expand=True)
        for theme in light_themes:
            light_node.add_leaf(
                THEME_DISPLAY_NAMES.get(theme.name, theme.name),
                data=theme.name,
            )

        if self._saved_themes:
            saved_node = tree.root.add(f"Saved  ({len(self._saved_themes)})", expand=True)
            for theme in self._saved_themes:
                saved_node.add_leaf(theme.name, data=theme.name)

        return tree

    def _refresh_theme_tree(self) -> None:
        """Rebuild the sidebar tree after themes are added at runtime."""
        try:
            tree = self.query_one("#theme-tree", Tree)
        except Exception:
            return
        tree.clear()
        dark_themes = [t for t in RETRO_THEMES if t.dark]
        light_themes = [t for t in RETRO_THEMES if not t.dark]
        dark_node = tree.root.add(f"Dark  ({len(dark_themes)})", expand=True)
        for theme in dark_themes:
            dark_node.add_leaf(
                THEME_DISPLAY_NAMES.get(theme.name, theme.name),
                data=theme.name,
            )
        light_node = tree.root.add(f"Light  ({len(light_themes)})", expand=True)
        for theme in light_themes:
            light_node.add_leaf(
                THEME_DISPLAY_NAMES.get(theme.name, theme.name),
                data=theme.name,
            )
        if self._saved_themes:
            saved_node = tree.root.add(f"Saved  ({len(self._saved_themes)})", expand=True)
            for theme in self._saved_themes:
                saved_node.add_leaf(theme.name, data=theme.name)

    def _log(self, message: str) -> None:
        """Append a line to the log panel (visible or not).

        Also mirrors to a plain-text history so `c` can copy the whole log.
        """
        plain = Text.from_markup(message).plain
        self._log_history.append(plain)
        try:
            panel = self.query_one("#log-panel", RichLog)
            panel.write(message)
        except Exception:
            pass

    def on_mount(self) -> None:
        self.theme = self._initial_theme

        # Populate Overview-tab widgets
        table_o = self.query_one("#dt-1o", DataTable)
        table_o.add_columns("ID", "Name", "Status", "Score")
        for row in (
            ("1", "Alice", "Active", "92"),
            ("2", "Bob", "Idle", "78"),
            ("3", "Carol", "Banned", "12"),
            ("4", "Dan", "Active", "65"),
        ):
            table_o.add_row(*row)
        self.query_one("#pb-1o", ProgressBar).update(progress=42)

        # Populate Data-tab widgets
        table = self.query_one("#dt-1", DataTable)
        table.add_columns("ID", "Name", "Status", "Score")
        table.add_row("1", "Alice", "Active", "92")
        table.add_row("2", "Bob", "Idle", "78")
        table.add_row("3", "Carol", "Banned", "12")
        table.add_row("4", "Dan", "Active", "65")
        self.query_one("#pb-1", ProgressBar).update(progress=42)

        # Populate Text-tab RichLog (separate from the toggleable log panel)
        log = self.query_one("#log-1", RichLog)
        log.write("[green]INFO[/green]  Demo app started.")
        log.write("[yellow]WARN[/yellow]  This is a sample warning.")
        log.write("[red]ERROR[/red] Sample error message.")
        log.write("Pick a theme on the left, press [b]n[/b] / [b]p[/b] to cycle, or [b]Ctrl+P[/b] for the picker.")

        # Seed the toggleable log panel
        self._log(f"[dim]textual-themes demo v{__version__} ready.[/dim]")
        if self._saved_themes:
            self._log(f"[green]Loaded {len(self._saved_themes)} saved theme(s) from disk.[/green]")

    def watch_theme(self, theme_name: str) -> None:
        """Update header subtitle and sidebar cursor when the theme changes."""
        display = THEME_DISPLAY_NAMES.get(theme_name, theme_name)
        if theme_name in self._all_theme_names:
            index = self._all_theme_names.index(theme_name) + 1
            total = len(self._all_theme_names)
            self.sub_title = f"{display}  ({index}/{total})"
        else:
            self.sub_title = display
        self._sync_sidebar_cursor(theme_name)

    def _sync_sidebar_cursor(self, theme_name: str) -> None:
        try:
            tree = self.query_one("#theme-tree", Tree)
        except Exception:
            return
        for category in tree.root.children:
            for leaf in category.children:
                if leaf.data == theme_name:
                    tree.select_node(leaf)
                    tree.scroll_to_node(leaf)
                    return

    def on_tree_node_selected(self, event: Tree.NodeSelected[str]) -> None:
        """Sidebar selection changes the active theme."""
        if event.control.id != "theme-tree":
            return
        name = event.node.data
        if name and name != self.theme and name in self._all_theme_names:
            self.theme = name

    def action_show_modal(self) -> None:
        theme_name = self.theme or ""
        display = THEME_DISPLAY_NAMES.get(theme_name, theme_name)
        self.push_screen(AboutModalScreen(theme_display=display))

    def action_next_theme(self) -> None:
        self._cycle_theme(1)

    def action_prev_theme(self) -> None:
        self._cycle_theme(-1)

    def _cycle_theme(self, step: int) -> None:
        if self.theme not in self._all_theme_names:
            self.theme = self._all_theme_names[0]
            return
        idx = self._all_theme_names.index(self.theme)
        self.theme = self._all_theme_names[(idx + step) % len(self._all_theme_names)]

    def action_random_theme(self) -> None:
        """Generate a random theme matching current dark/light mode."""
        current = self._registered_themes.get(self.theme or "")
        current_dark = current.dark if current is not None else True
        self._generate_and_apply(dark=current_dark)

    def action_random_light(self) -> None:
        self._generate_and_apply(dark=False)

    def action_random_dark(self) -> None:
        self._generate_and_apply(dark=True)

    def _generate_and_apply(self, dark: bool) -> None:
        new_theme = generate_random_theme(dark=dark)
        # Register + activate
        self.register_theme(new_theme)
        self._last_generated_name = new_theme.name
        self.theme = new_theme.name
        self._log(
            f"[cyan]GEN[/cyan]   {'dark' if dark else 'light'} "
            f"[b]{new_theme.name}[/b] "
            f"primary={new_theme.primary} accent={new_theme.accent}"
        )
        self.notify(
            f"Generated {new_theme.name}",
            title="Random theme",
            timeout=2,
        )

    def action_save_theme(self) -> None:
        """Persist the current theme to ~/.textual-themes/saved/<name>.json."""
        theme_obj = self._get_current_theme_obj()
        if theme_obj is None:
            self._log("[red]ERR[/red]   no theme object found for current theme")
            self.notify("Cannot save: no current theme", severity="error")
            return
        path = save_theme(theme_obj)
        self._log(f"[green]SAVE[/green]  wrote {path}")
        # Add to saved list if it wasn't already there
        if not any(t.name == theme_obj.name for t in self._saved_themes):
            self._saved_themes.append(theme_obj)
            if theme_obj.name not in self._all_theme_names:
                self._all_theme_names.append(theme_obj.name)
            self._refresh_theme_tree()
        self.notify(f"Saved {theme_obj.name}", title="Save", timeout=2)

    def _get_current_theme_obj(self):
        """Find the Theme instance matching the current self.theme name."""
        current = self.theme
        if not current:
            return None
        for theme in RETRO_THEMES:
            if theme.name == current:
                return theme
        for theme in self._saved_themes:
            if theme.name == current:
                return theme
        # Check if it's a freshly-generated theme registered on the app
        registered = self._registered_themes.get(current)
        return registered

    def action_toggle_log(self) -> None:
        try:
            panel = self.query_one("#log-panel", RichLog)
            splitter = self.query_one("#log-splitter", HorizontalSplitter)
        except Exception:
            return
        was_hidden = panel.has_class("hidden")
        panel.toggle_class("hidden")
        splitter.toggle_class("hidden")
        if not was_hidden:
            # Was visible, now hiding — reset main height so the freed
            # space goes back to the content area instead of staying empty.
            try:
                main = self.query_one("#main")
                main.styles.height = "4fr"
            except Exception:
                pass

    def action_screenshot(self) -> None:
        # Save as <theme-slug>.svg (no timestamp) so repeated captures
        # overwrite cleanly — run the demo from docs/screenshots/ to
        # regenerate the gallery in place.
        slug = (self.theme or "screenshot").replace("/", "-")
        filename = f"{slug}.svg"
        self.save_screenshot(str(Path.cwd() / filename))
        self.notify(f"Saved {filename}", title="Screenshot")

    def action_toggle_border(self) -> None:
        """Toggle the integrated-border look on both splitters at once."""
        for selector in ("#vsplitter", "#log-splitter"):
            try:
                widget = self.query_one(selector)
            except Exception:
                continue
            widget.toggle_class("with-border")
            widget.refresh()

    def action_copy_log(self) -> None:
        if not self._log_history:
            self.notify("Log is empty", severity="warning")
            return
        text = "\n".join(self._log_history)
        self.copy_to_clipboard(text)
        self._log(f"[cyan]COPY[/cyan]  copied {len(self._log_history)} log lines ({len(text)} chars) to clipboard")
        self.notify(
            f"Copied {len(self._log_history)} lines to clipboard",
            timeout=2,
        )

    def action_reload_themes(self) -> None:
        """Rescan ~/.textual-themes/saved/ for newly added JSON files."""
        fresh = load_saved_themes()
        added = 0
        for theme in fresh:
            if theme.name in self._registered_themes:
                continue
            self.register_theme(theme)
            self._saved_themes.append(theme)
            self._all_theme_names.append(theme.name)
            added += 1
        self._refresh_theme_tree()
        self._log(
            f"[cyan]LOAD[/cyan]  rescanned saved-dir, "
            f"added {added} new theme(s) "
            f"(total saved: {len(self._saved_themes)})"
        )
        self.notify(
            f"Reload: +{added} theme(s)" if added else "Reload: no new themes",
            timeout=2,
        )

    def action_open_theme(self) -> None:
        """Open a file-picker modal to import a theme JSON from anywhere."""
        from .generator import SAVED_DIR

        start_dir = SAVED_DIR if SAVED_DIR.is_dir() else Path.home()
        self.push_screen(
            ThemeOpenScreen(start_dir=start_dir),
            callback=self._on_theme_file_picked,
        )

    def _on_theme_file_picked(self, path: Path | None) -> None:
        if path is None:
            return
        import json

        from .generator import theme_from_dict

        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            theme_obj = theme_from_dict(data)
        except Exception as exc:
            self._log(f"[red]ERR[/red]   failed to import {path}: {exc}")
            self.notify(f"Import failed: {exc}", severity="error")
            return
        if theme_obj.name in self._registered_themes:
            self._log(f"[yellow]WARN[/yellow]  theme '{theme_obj.name}' already registered, switching to it")
        else:
            self.register_theme(theme_obj)
            self._saved_themes.append(theme_obj)
            self._all_theme_names.append(theme_obj.name)
            self._refresh_theme_tree()
            self._log(f"[green]LOAD[/green]  imported {theme_obj.name} from {path}")
        self.theme = theme_obj.name
        self.notify(f"Loaded {theme_obj.name}", timeout=2)
