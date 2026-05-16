#!/usr/bin/env bash
# run.sh - starts the textual-themes storybook demo from source.
set -euo pipefail
cd "$(dirname "$0")"

if [ ! -d ".venv" ]; then
    echo "Please run ./bootstrap.sh first." >&2
    exit 1
fi

.venv/bin/python -m textual_themes "$@"
