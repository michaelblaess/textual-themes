#!/usr/bin/env bash
set -euo pipefail

REPO="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV="$REPO/.venv"
PYTHON_BIN="${PYTHON:-python3}"

if ! command -v "$PYTHON_BIN" >/dev/null 2>&1; then
    echo "Error: '$PYTHON_BIN' not found on PATH. Install Python 3.12+ or set PYTHON=..."
    exit 1
fi

if [ ! -d "$VENV" ]; then
    echo "Creating virtual environment..."
    "$PYTHON_BIN" -m venv "$VENV"
fi

VENV_PYTHON="$VENV/bin/python"
VENV_PIP="$VENV/bin/pip"

echo "Upgrading pip..."
"$VENV_PYTHON" -m pip install --upgrade pip --quiet

echo "Installing textual-themes (editable)..."
"$VENV_PIP" install -e "$REPO" --quiet

cat <<EOF

Setup complete.

Run the demo:
    $VENV_PYTHON -m textual_themes

List available themes:
    $VENV_PYTHON -m textual_themes --list
EOF
