"""Erzeugt das App-Icon fuer textual-themes (.ico + .png + .icns + SVG-Varianten).

Motiv: ein 2x2-Raster aus abgerundeten Farbkacheln (Teal, Amber, Violett) -
unten rechts statt einer vierten Kachel ein hervorgehobenes Terminal-Prompt
``>_`` (Chevron + Cursor). Steht fuer "Farbthemes fuer Terminal-Apps".

Der Prompt ist font-frei als Geometrie gezeichnet (Chevron = Polyline, Cursor =
Rechteck), damit das SVG ohne Schrift-Abhaengigkeit ueberall gleich rendert.

Drei Darstellungs-Varianten (gleiche Geometrie):
- "tile"  : dunkles, abgerundetes Tile (App-Icon-Look) - fuer .ico/.png/.icns.
- "dark"  : transparenter Hintergrund, helle Toene - fuer DUNKLE Untergruende.
- "light" : transparenter Hintergrund, kraeftige Toene - fuer HELLE Untergruende.

Erzeugt:
- assets/icon.ico         (16/32/48/64/128/256 px)  - --windows-icon-from-ico
- assets/icon.icns        (1024 px, nativ)           - --macos-app-icon
- assets/icon.png         (512 px)                   - og:image / Social-Card
- assets/icon.svg         (tile, skalierbar)         - branded Logo
- assets/icon-dark.svg    (transparent, dunkle Untergruende)
- assets/icon-light.svg   (transparent, helle Untergruende)

Aufruf (aus dem Repo-Root):
    uv run --no-sync python assets/make_icon.py
"""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw

# ── Geometrie (Basis-Koordinaten, viewBox 0..256) ────────────────────────────
_BASE = 256
_SS = 4  # Supersampling fuer die Rasterbilder
_TILE_RADIUS = _BASE * 0.22

_MARGIN = 44.0
_GAP = 16.0
_CELL = (_BASE - 2 * _MARGIN - _GAP) / 2  # = 76
_CELL_R = 14.0  # Eckenradius der Kacheln

# Kachel-Ankerpunkte (obere-linke Ecke). Reihenfolge: TL, TR, BL; BR = Prompt.
_TL = (_MARGIN, _MARGIN)
_TR = (_MARGIN + _CELL + _GAP, _MARGIN)
_BL = (_MARGIN, _MARGIN + _CELL + _GAP)
_BR = (_MARGIN + _CELL + _GAP, _MARGIN + _CELL + _GAP)

_PROMPT_OUTLINE_W = 4.0
_CHEVRON_W = 6.5
# Prompt-Elemente relativ zur BR-Zelle.
_brx, _bry = _BR
_pcx, _pcy = _brx + _CELL / 2, _bry + _CELL / 2  # Zellmitte
# Chevron ">" als Polyline (3 Punkte), etwas links der Mitte.
_CHEVRON = [
    (_pcx - 14, _pcy - 13),
    (_pcx + 2, _pcy),
    (_pcx - 14, _pcy + 13),
]
# Cursor "_" als abgerundeter Balken rechts unten neben dem Chevron.
_CURSOR = (_pcx + 8, _pcy + 9, _pcx + 26, _pcy + 15)  # x0,y0,x1,y1

# ── Farben ───────────────────────────────────────────────────────────────────
_BG_TOP = (16, 28, 26)
_BG_BOTTOM = (9, 13, 17)
_PROMPT_BG = (11, 14, 18)

_TEAL_BRIGHT, _AMBER_BRIGHT, _VIOLET_BRIGHT = (45, 212, 191), (251, 191, 36), (167, 139, 250)
_TEAL_DEEP, _AMBER_DEEP, _VIOLET_DEEP = (13, 148, 136), (217, 119, 6), (124, 58, 237)

_VARIANTS = {
    "tile": {
        "tile": True,
        "swatches": [_TEAL_BRIGHT, _AMBER_BRIGHT, _VIOLET_BRIGHT],
        "accent": _TEAL_BRIGHT,  # Chevron + Prompt-Rahmen
        "cursor": _AMBER_BRIGHT,
    },
    "dark": {
        "tile": False,
        "swatches": [_TEAL_BRIGHT, _AMBER_BRIGHT, _VIOLET_BRIGHT],
        "accent": _TEAL_BRIGHT,
        "cursor": _AMBER_BRIGHT,
    },
    "light": {
        "tile": False,
        "swatches": [_TEAL_DEEP, _AMBER_DEEP, _VIOLET_DEEP],
        "accent": _TEAL_DEEP,
        "cursor": _AMBER_DEEP,
    },
}


def _hex(c: tuple[int, int, int]) -> str:
    return f"#{c[0]:02x}{c[1]:02x}{c[2]:02x}"


# ── Rasterbild (Pillow) - "tile"-Variante ────────────────────────────────────
def _vertical_gradient(size: int) -> Image.Image:
    grad = Image.new("RGBA", (size, size))
    px = grad.load()
    assert px is not None
    for y in range(size):
        f = y / (size - 1)
        color = tuple(int(_BG_TOP[i] + (_BG_BOTTOM[i] - _BG_TOP[i]) * f) for i in range(3)) + (255,)
        for x in range(size):
            px[x, y] = color
    return grad


def build_master() -> Image.Image:
    """Baut das supersamplete Master-Rasterbild (tile-Variante, RGBA)."""
    v = _VARIANTS["tile"]
    s = _SS
    size = _BASE * s
    img = _vertical_gradient(size)
    draw = ImageDraw.Draw(img)

    mask = Image.new("L", (size, size), 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size - 1, size - 1), radius=int(_TILE_RADIUS * s), fill=255)

    def cell(
        anchor: tuple[float, float], fill: tuple[int, int, int], outline: tuple[int, int, int] | None = None
    ) -> None:
        x0, y0 = anchor[0] * s, anchor[1] * s
        draw.rounded_rectangle(
            (x0, y0, x0 + _CELL * s, y0 + _CELL * s),
            radius=int(_CELL_R * s),
            fill=(*fill, 255),
            outline=((*outline, 255) if outline else None),
            width=int(_PROMPT_OUTLINE_W * s) if outline else 1,
        )

    for anchor, color in zip((_TL, _TR, _BL), v["swatches"], strict=True):
        cell(anchor, color)
    cell(_BR, _PROMPT_BG, outline=v["accent"])

    draw.line([(x * s, y * s) for x, y in _CHEVRON], fill=(*v["accent"], 255), width=int(_CHEVRON_W * s), joint="curve")
    cx0, cy0, cx1, cy1 = _CURSOR
    draw.rounded_rectangle((cx0 * s, cy0 * s, cx1 * s, cy1 * s), radius=int(3 * s), fill=(*v["cursor"], 255))

    img.putalpha(mask)
    return img


# ── SVG (variantenabhaengig) ───────────────────────────────────────────────────
def build_svg(variant: str) -> str:
    """Baut das Icon als SVG-String fuer eine der Varianten."""
    v = _VARIANTS[variant]

    def rect(anchor: tuple[float, float], fill: str, outline: str | None = None) -> str:
        x, y = anchor
        stroke = f' stroke="{outline}" stroke-width="{_PROMPT_OUTLINE_W}"' if outline else ""
        return (
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{_CELL:.1f}" height="{_CELL:.1f}" '
            f'rx="{_CELL_R}" ry="{_CELL_R}" fill="{fill}"{stroke}/>'
        )

    swatches = "".join(rect(a, _hex(c)) for a, c in zip((_TL, _TR, _BL), v["swatches"], strict=True))
    prompt_cell = rect(_BR, _hex(_PROMPT_BG), outline=_hex(v["accent"]))
    chevron_pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in _CHEVRON)
    chevron = (
        f'<polyline points="{chevron_pts}" fill="none" stroke="{_hex(v["accent"])}" '
        f'stroke-width="{_CHEVRON_W}" stroke-linecap="round" stroke-linejoin="round"/>'
    )
    cx0, cy0, cx1, cy1 = _CURSOR
    cursor = (
        f'<rect x="{cx0:.1f}" y="{cy0:.1f}" width="{cx1 - cx0:.1f}" height="{cy1 - cy0:.1f}" '
        f'rx="3" ry="3" fill="{_hex(v["cursor"])}"/>'
    )

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {_BASE} {_BASE}" '
        f'width="{_BASE}" height="{_BASE}" role="img" aria-label="textual-themes">'
    ]
    if v["tile"]:
        parts.append(
            "<defs>"
            '<linearGradient id="bg" x1="0" y1="0" x2="0" y2="1">'
            f'<stop offset="0" stop-color="{_hex(_BG_TOP)}"/>'
            f'<stop offset="1" stop-color="{_hex(_BG_BOTTOM)}"/>'
            "</linearGradient>"
            f'<clipPath id="tile"><rect width="{_BASE}" height="{_BASE}" '
            f'rx="{_TILE_RADIUS:.2f}" ry="{_TILE_RADIUS:.2f}"/></clipPath>'
            "</defs>"
            '<g clip-path="url(#tile)">'
            f'<rect width="{_BASE}" height="{_BASE}" fill="url(#bg)"/>'
        )
    else:
        parts.append("<g>")
    parts.append(swatches)
    parts.append(prompt_cell)
    parts.append(chevron)
    parts.append(cursor)
    parts.append("</g></svg>\n")
    return "".join(parts)


def main() -> None:
    """Rendert das Master-Icon und schreibt .ico + .png + .icns + SVG-Varianten."""
    assets = Path(__file__).resolve().parent
    master_full = build_master()  # 1024 px
    master = master_full.resize((_BASE, _BASE), Image.Resampling.LANCZOS)

    ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
    master.save(assets / "icon.ico", sizes=ico_sizes)
    master_full.resize((512, 512), Image.Resampling.LANCZOS).save(assets / "icon.png")
    master_full.save(assets / "icon.icns")

    (assets / "icon.svg").write_text(build_svg("tile"), encoding="utf-8")
    (assets / "icon-dark.svg").write_text(build_svg("dark"), encoding="utf-8")
    (assets / "icon-light.svg").write_text(build_svg("light"), encoding="utf-8")

    print(f"icon.ico geschrieben ({', '.join(f'{w}x{h}' for w, h in ico_sizes)})")
    print("icon.png (512) / icon.icns (1024) geschrieben")
    print("icon.svg / icon-dark.svg / icon-light.svg geschrieben")


if __name__ == "__main__":
    main()
