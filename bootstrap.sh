#!/usr/bin/env bash
# bootstrap.sh - sets up the textual-themes development environment.
#
# Creates the .venv via uv, installs runtime + dev dependencies and the
# Nuitka build tool (for compile-linux.sh / compile-macos.sh). Run once
# after cloning the repo.
#
# textual-themes is primarily a library; the Nuitka build targets the
# bundled storybook demo app (textual-themes-demo).

set -euo pipefail
cd "$(dirname "$0")"

echo "=== textual-themes - dev environment ==="

echo "[1/2] venv + dependencies (uv sync)..."
uv sync --extra dev

echo "[2/2] Nuitka build tool..."
uv pip install nuitka

echo ""
echo "Done. Start with: ./run.sh"
