#!/usr/bin/env bash
# compile-macos.sh - compiles the textual-themes demo into a standalone macOS
# binary with Nuitka.
#
# textual-themes is primarily a library, but it ships a storybook demo app that
# lets you browse every retro theme. This script compiles that demo into a
# self-contained --standalone build (no Python install needed on the target
# machine). Output: dist/textual-themes-demo/textual-themes-demo plus its shared
# libraries, and dist/textual-themes-demo-vX.Y.Z-macos-<arch>.tar.gz.
#
# Build-Maschine braucht die Xcode Command Line Tools (liefern clang):
#   xcode-select --install
#
# Hinweise zu macOS:
# - Es entsteht KEIN .app-Bundle - das ist ein Terminal-/TUI-Programm.
# - Nuitka signiert die Binary auf macOS automatisch ad-hoc. Beim Download
#   setzt macOS ein Quarantaene-Attribut - der Empfaenger muss es entfernen:
#     xattr -dr com.apple.quarantine textual-themes-demo
#   Fuer Verteilung ohne Gatekeeper-Warnung braeuchte es eine Apple Developer
#   ID + Notarisierung (separater Schritt, hier nicht abgedeckt).

set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
entry="$root/src/textual_themes/__main__.py"
init_py="$root/src/textual_themes/__init__.py"
out_dir="$root/dist"
dist_dir="$out_dir/textual-themes-demo"
arch="$(uname -m)"   # arm64 (Apple Silicon) oder x86_64 (Intel)

# venv-Python bevorzugen, sonst System-Python
if [ -x "$root/.venv/bin/python" ]; then
    python="$root/.venv/bin/python"
else
    python="python3"
fi

# Build-Tools pruefen, bevor Nuitka mittendrin abbricht
if ! command -v clang >/dev/null 2>&1; then
    echo "Fehlt: clang - bitte Xcode Command Line Tools installieren: xcode-select --install" >&2
    exit 1
fi

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

echo "Compiling textual-themes-demo v$version ($arch) with Nuitka..."

# Alten Build verwerfen - das Ergebnis soll reproduzierbar sein
rm -rf "$dist_dir"

started=$(date +%s)

# --standalone        : self-contained, kein Python auf dem Zielrechner noetig
# --remove-output     : C-/Objekt-Zwischendateien nach dem Build aufraeumen
# --include-package-data=textual_themes : Paket-Datendateien mitnehmen
nuitka_args=(
    --standalone
    --assume-yes-for-downloads
    --remove-output
    --include-package=textual_themes
    --include-package-data=textual_themes
    --output-dir="$out_dir"
    --output-filename=textual-themes-demo
)

# App-Icon einbetten. Natives .icns verwenden - ein PNG braeuchte hier sonst
# das Zusatzpaket imageio (Nuitka: "Need to install 'imageio' ...").
icon_icns="$root/assets/icon.icns"
if [ -f "$icon_icns" ]; then
    nuitka_args+=(--macos-app-icon="$icon_icns")
else
    echo "Hinweis: $icon_icns fehlt - Binary wird ohne Icon gebaut."
fi

"$python" -m nuitka "${nuitka_args[@]}" "$entry"

# Nuitka benennt den dist-Ordner nach dem Hauptmodul (__main__.dist) - umbenennen
if [ -d "$out_dir/__main__.dist" ]; then
    mv "$out_dir/__main__.dist" "$dist_dir"
fi

elapsed=$(( $(date +%s) - started ))
exe="$dist_dir/textual-themes-demo"
size_mb=$(du -sm "$dist_dir" | cut -f1)

# Verteilbares Archiv: tar.gz statt zip - tar bewahrt das Ausfuehrungs-Flag
# der Binary, ein zip wuerde es verlieren.
tarball="$out_dir/textual-themes-demo-v$version-macos-$arch.tar.gz"
rm -f "$tarball"
tar -czf "$tarball" -C "$out_dir" textual-themes-demo
tar_mb=$(du -sm "$tarball" | cut -f1)

echo ""
echo "Done in ${elapsed}s"
echo "  dist folder : $dist_dir  (${size_mb} MB)"
echo "  tarball     : $tarball  (${tar_mb} MB)"
echo "  run         : $exe"
