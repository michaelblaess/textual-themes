#!/usr/bin/env bash
# compile-linux.sh - compiles the textual-themes demo into a standalone Linux
# binary with Nuitka.
#
# textual-themes is primarily a library, but it ships a storybook demo app that
# lets you browse every retro theme. This script compiles that demo into a
# self-contained --standalone build (no Python install needed on the target
# machine). Output: dist/textual-themes-demo/textual-themes-demo plus its shared
# libraries, and dist/textual-themes-demo-vX.Y.Z-linux-x86_64.tar.gz.
#
# Build-Maschine braucht: gcc, patchelf und die Python-Header.
#   Debian/Ubuntu:  sudo apt install gcc patchelf python3-dev
#   Fedora:         sudo dnf install gcc patchelf python3-devel

set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
entry="$root/src/textual_themes/__main__.py"
init_py="$root/src/textual_themes/__init__.py"
out_dir="$root/dist"
dist_dir="$out_dir/textual-themes-demo"

# venv-Python bevorzugen, sonst System-Python
if [ -x "$root/.venv/bin/python" ]; then
    python="$root/.venv/bin/python"
else
    python="python3"
fi

# Build-Tools pruefen, bevor Nuitka mittendrin abbricht
for tool in gcc patchelf; do
    if ! command -v "$tool" >/dev/null 2>&1; then
        echo "Fehlt: $tool - bitte installieren (z.B. sudo apt install gcc patchelf python3-dev)" >&2
        exit 1
    fi
done

# venv mit dem Lockfile abgleichen, damit Nuitka keine veralteten
# (Git-)Dependencies einkompiliert. --inexact laesst Extra-Pakete wie das
# ad-hoc installierte nuitka unangetastet.
if command -v uv >/dev/null 2>&1; then
    echo "Syncing venv to lockfile (uv sync --inexact)..."
    uv sync --inexact --project "$root"
else
    echo "uv nicht gefunden - venv-Sync uebersprungen" >&2
fi

# Version aus __init__.py lesen, damit nichts driftet
# (portables sed - 'grep -oP' gibt es auf dem BSD-grep von macOS nicht)
version="$(sed -n 's/^__version__ *= *"\([^"]*\)".*/\1/p' "$init_py")"
if [ -z "$version" ]; then
    echo "Konnte __version__ nicht aus $init_py lesen" >&2
    exit 1
fi

echo "Compiling textual-themes-demo v$version with Nuitka..."

# Alten Build verwerfen - das Ergebnis soll reproduzierbar sein
rm -rf "$dist_dir"

started=$(date +%s)

# --standalone        : self-contained, kein Python auf dem Zielrechner noetig
# --remove-output     : C-/Objekt-Zwischendateien nach dem Build aufraeumen
# --include-package-data=textual_themes : Paket-Datendateien mitnehmen
#
# Kein App-Icon: ein ELF-Binary kann kein Icon einbetten (--linux-icon nur bei
# AppImage/--onefile). Auf dem Desktop kaeme das Icon ueber eine .desktop-Datei.
"$python" -m nuitka \
    --standalone \
    --assume-yes-for-downloads \
    --remove-output \
    --include-package=textual_themes \
    --include-package-data=textual_themes \
    --output-dir="$out_dir" \
    --output-filename=textual-themes-demo \
    "$entry"

# Nuitka benennt den dist-Ordner nach dem Hauptmodul (__main__.dist) - umbenennen
if [ -d "$out_dir/__main__.dist" ]; then
    mv "$out_dir/__main__.dist" "$dist_dir"
fi

elapsed=$(( $(date +%s) - started ))
exe="$dist_dir/textual-themes-demo"
size_mb=$(du -sm "$dist_dir" | cut -f1)

# Verteilbares Archiv: tar.gz statt zip - tar bewahrt das Ausfuehrungs-Flag
# der Binary, ein zip wuerde es verlieren.
tarball="$out_dir/textual-themes-demo-v$version-linux-x86_64.tar.gz"
rm -f "$tarball"
tar -czf "$tarball" -C "$out_dir" textual-themes-demo
tar_mb=$(du -sm "$tarball" | cut -f1)

echo ""
echo "Done in ${elapsed}s"
echo "  dist folder : $dist_dir  (${size_mb} MB)"
echo "  tarball     : $tarball  (${tar_mb} MB)"
echo "  run         : $exe"
