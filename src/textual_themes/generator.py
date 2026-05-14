"""Random theme generator + JSON persistence.

Internal helper used by the demo app. Not part of the public package
API — the textual-themes package exports only the 36 curated themes.

The generator builds a Textual `Theme` from a randomly picked HSL
colour-harmony strategy (analogous / complementary / triadic /
split-complementary), grounded by dark/light luminance ranges that
keep readability sane.

Saved themes round-trip via JSON to ``~/.textual-themes/saved/``.
"""

from __future__ import annotations

import colorsys
import json
import random
from pathlib import Path

from textual.theme import Theme

SAVED_DIR = Path.home() / ".textual-themes" / "saved"

_HARMONY_STRATEGIES = ("analogous", "complementary", "triadic", "split-complementary")


def _hsl_hex(hue: float, sat: float, light: float) -> str:
    """Convert HSL (hue in 0-360, sat/light in 0-1) to #rrggbb hex."""
    sat = max(0.0, min(1.0, sat))
    light = max(0.0, min(1.0, light))
    r, g, b = colorsys.hls_to_rgb((hue % 360) / 360, light, sat)
    return f"#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}"


def _relative_luminance(hex_color: str) -> float:
    """WCAG 2.x relative luminance for an #rrggbb hex color."""
    r = int(hex_color[1:3], 16) / 255
    g = int(hex_color[3:5], 16) / 255
    b = int(hex_color[5:7], 16) / 255

    def channel(c: float) -> float:
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def _contrast_ratio(a: str, b: str) -> float:
    """WCAG contrast ratio between two hex colors. Larger == higher contrast."""
    la, lb = _relative_luminance(a), _relative_luminance(b)
    light = max(la, lb)
    dark = min(la, lb)
    return (light + 0.05) / (dark + 0.05)


def _ensure_contrast(color_hex: str, fg_hex: str, min_ratio: float = 4.5) -> str:
    """Push the color's lightness away from fg until contrast >= min_ratio.

    Used to keep background / surface / panel readable against the theme's
    foreground colour. Hue and saturation are preserved; only HSL lightness
    is shifted in 0.05 steps (max 20 iterations).
    """
    if _contrast_ratio(color_hex, fg_hex) >= min_ratio:
        return color_hex
    r = int(color_hex[1:3], 16) / 255
    g = int(color_hex[3:5], 16) / 255
    b = int(color_hex[5:7], 16) / 255
    hue, light, sat = colorsys.rgb_to_hls(r, g, b)
    # If foreground is bright -> push colour darker, and vice versa.
    direction = -1 if _relative_luminance(fg_hex) > 0.5 else 1
    for _ in range(20):
        light = max(0.02, min(0.98, light + direction * 0.05))
        candidate = _hsl_hex(hue * 360, sat, light)
        if _contrast_ratio(candidate, fg_hex) >= min_ratio:
            return candidate
    return _hsl_hex(hue * 360, sat, light)


def generate_random_theme(
    dark: bool,
    seed: int | None = None,
) -> Theme:
    """Generate a random Textual `Theme`.

    Args:
        dark: True for a dark theme (light foreground on dark background),
            False for a light theme.
        seed: Optional seed for reproducibility. If None, uses the system
            random source.

    The generator picks one of four colour-harmony strategies and grounds
    luminance by the dark/light flag. Semantic colours (warning/error/
    success) are clamped to amber/red/green hue bands so error messages
    always look red etc.
    """
    rng = random.Random(seed)

    base_hue = rng.uniform(0, 360)
    strategy = rng.choice(_HARMONY_STRATEGIES)

    if strategy == "analogous":
        primary_hue = base_hue
        secondary_hue = base_hue + rng.choice([-30, -20, 20, 30])
        accent_hue = base_hue + rng.choice([-60, -45, 45, 60])
    elif strategy == "complementary":
        primary_hue = base_hue
        secondary_hue = base_hue + rng.uniform(-15, 15)
        accent_hue = base_hue + 180
    elif strategy == "triadic":
        primary_hue = base_hue
        secondary_hue = base_hue + 120
        accent_hue = base_hue + 240
    else:  # split-complementary
        primary_hue = base_hue
        secondary_hue = base_hue + 150
        accent_hue = base_hue + 210

    # Saturation/lightness ranges differ between dark and light themes:
    # dark themes pop with high saturation on a near-black canvas, while
    # light themes need softer pastel-ish colors to avoid eye-straining
    # high-saturation pops against a white background.
    if dark:
        primary_s_lo, primary_s_hi = 0.55, 0.85
        primary_l_lo, primary_l_hi = 0.45, 0.60
        secondary_s_lo, secondary_s_hi = 0.40, 0.70
        accent_s_lo, accent_s_hi = 0.65, 0.90
        accent_l_lo, accent_l_hi = 0.50, 0.65
    else:
        primary_s_lo, primary_s_hi = 0.40, 0.65
        primary_l_lo, primary_l_hi = 0.42, 0.55
        secondary_s_lo, secondary_s_hi = 0.30, 0.55
        accent_s_lo, accent_s_hi = 0.45, 0.70
        accent_l_lo, accent_l_hi = 0.48, 0.62

    primary = _hsl_hex(
        primary_hue,
        rng.uniform(primary_s_lo, primary_s_hi),
        rng.uniform(primary_l_lo, primary_l_hi),
    )
    secondary = _hsl_hex(
        secondary_hue,
        rng.uniform(secondary_s_lo, secondary_s_hi),
        rng.uniform(0.40, 0.55),
    )
    accent_sat = rng.uniform(accent_s_lo, accent_s_hi)
    accent_light = rng.uniform(accent_l_lo, accent_l_hi)
    accent = _hsl_hex(accent_hue, accent_sat, accent_light)
    boost = _hsl_hex(accent_hue, min(1.0, accent_sat + 0.1), min(0.75, accent_light + 0.10))

    # Panel gets its own hue (randomly picked) so the sidebar/header colour
    # differs between themes — without this, light themes especially all
    # look like "white with slightly different buttons".
    panel_hue = rng.choice([primary_hue, secondary_hue, accent_hue])

    if dark:
        bg_light = rng.uniform(0.04, 0.10)
        surface_light = bg_light + rng.uniform(0.03, 0.07)
        panel_light = bg_light + rng.uniform(0.08, 0.22)
        fg_light = rng.uniform(0.85, 0.95)
        bg_sat = rng.uniform(0.20, 0.45)
        surface_sat = rng.uniform(0.20, 0.40)
        panel_sat = rng.uniform(0.45, 0.80)
        fg_sat = rng.uniform(0.02, 0.10)
    else:
        # Light themes: pastel panel (lighter + less saturated) and
        # subtler surface/background tints for a calmer feel.
        bg_light = rng.uniform(0.94, 0.99)
        surface_light = max(0.88, bg_light - rng.uniform(0.02, 0.05))
        panel_light = rng.uniform(0.62, 0.82)
        fg_light = rng.uniform(0.12, 0.25)
        bg_sat = rng.uniform(0.04, 0.12)
        surface_sat = rng.uniform(0.08, 0.18)
        panel_sat = rng.uniform(0.25, 0.50)
        fg_sat = rng.uniform(0.10, 0.30)

    background = _hsl_hex(primary_hue, bg_sat, bg_light)
    surface = _hsl_hex(primary_hue, surface_sat, surface_light)
    panel = _hsl_hex(panel_hue, panel_sat, panel_light)
    foreground = _hsl_hex(primary_hue, fg_sat, fg_light)

    # WCAG contrast guard: ensure body text stays readable on every surface
    background = _ensure_contrast(background, foreground)
    surface = _ensure_contrast(surface, foreground)
    panel = _ensure_contrast(panel, foreground)

    # Semantic colours clamped to expected hue bands
    warning = _hsl_hex(rng.uniform(35, 50), rng.uniform(0.70, 0.90), 0.55)
    error = _hsl_hex(rng.uniform(0, 15), rng.uniform(0.60, 0.80), 0.50)
    success = _hsl_hex(rng.uniform(120, 150), rng.uniform(0.50, 0.70), 0.45)

    fingerprint = (primary + secondary + accent + background).replace("#", "")[:8]
    name = f"random-{'dark' if dark else 'light'}-{fingerprint}"

    return Theme(
        name=name,
        primary=primary,
        secondary=secondary,
        accent=accent,
        foreground=foreground,
        background=background,
        surface=surface,
        panel=panel,
        boost=boost,
        warning=warning,
        error=error,
        success=success,
        dark=dark,
    )


def theme_to_dict(theme: Theme) -> dict[str, object]:
    """Serialise a Theme to a plain dict suitable for JSON."""
    return {
        "name": theme.name,
        "primary": theme.primary,
        "secondary": theme.secondary,
        "accent": theme.accent,
        "foreground": theme.foreground,
        "background": theme.background,
        "surface": theme.surface,
        "panel": theme.panel,
        "boost": theme.boost,
        "warning": theme.warning,
        "error": theme.error,
        "success": theme.success,
        "is_dark": theme.dark,
    }


def theme_from_dict(data: dict[str, object]) -> Theme:
    """Deserialise a Theme from the dict produced by `theme_to_dict`."""
    return Theme(
        name=str(data["name"]),
        primary=str(data["primary"]),
        secondary=str(data["secondary"]),
        accent=str(data["accent"]),
        foreground=str(data["foreground"]),
        background=str(data["background"]),
        surface=str(data["surface"]),
        panel=str(data["panel"]),
        boost=str(data.get("boost") or data["accent"]),
        warning=str(data["warning"]),
        error=str(data["error"]),
        success=str(data["success"]),
        dark=bool(data["is_dark"]),
    )


def save_theme(theme: Theme) -> Path:
    """Write a Theme to `~/.textual-themes/saved/<name>.json`. Returns path."""
    SAVED_DIR.mkdir(parents=True, exist_ok=True)
    path = SAVED_DIR / f"{theme.name}.json"
    path.write_text(
        json.dumps(theme_to_dict(theme), indent=2),
        encoding="utf-8",
    )
    return path


def load_saved_themes() -> list[Theme]:
    """Load all themes from `~/.textual-themes/saved/`. Silently skips broken files."""
    if not SAVED_DIR.is_dir():
        return []
    themes: list[Theme] = []
    for path in sorted(SAVED_DIR.glob("*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
            themes.append(theme_from_dict(data))
        except Exception:
            continue
    return themes
