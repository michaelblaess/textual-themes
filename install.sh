#!/usr/bin/env bash
# textual-themes storybook - one-line installer (Linux / macOS)
#
#   curl -fsSL https://raw.githubusercontent.com/michaelblaess/textual-themes/main/install.sh | bash
#
# Installs the theme storybook into an isolated venv under
# ~/.textual-themes and puts a `textual-themes-demo` launcher on PATH.
set -euo pipefail

REPO_URL="git+https://github.com/michaelblaess/textual-themes.git"
INSTALL_DIR="${TEXTUAL_THEMES_HOME:-$HOME/.textual-themes}"
VENV="$INSTALL_DIR/venv"
BIN_DIR="$HOME/.local/bin"
LAUNCHER="$BIN_DIR/textual-themes-demo"

echo "Installing the textual-themes storybook..."

# 1. Locate a Python 3.12+ interpreter.
PYTHON_BIN=""
for candidate in python3.13 python3.12 python3 python; do
    if command -v "$candidate" >/dev/null 2>&1; then
        ver="$("$candidate" -c 'import sys; print("%d.%d" % sys.version_info[:2])' 2>/dev/null || echo "0.0")"
        if [ "${ver%%.*}" -eq 3 ] && [ "${ver##*.}" -ge 12 ]; then
            PYTHON_BIN="$candidate"
            break
        fi
    fi
done
if [ -z "$PYTHON_BIN" ]; then
    echo "Error: Python 3.12+ is required but was not found on PATH." >&2
    exit 1
fi
if ! command -v git >/dev/null 2>&1; then
    echo "Error: git is required to install from GitHub." >&2
    exit 1
fi
echo "Using $($PYTHON_BIN --version)"

# 2. Create the isolated environment.
mkdir -p "$INSTALL_DIR"
[ -d "$VENV" ] || "$PYTHON_BIN" -m venv "$VENV"

# 3. Install / update the package.
"$VENV/bin/python" -m pip install --upgrade pip --quiet
"$VENV/bin/pip" install --upgrade "$REPO_URL" --quiet

# 4. Put a launcher on PATH.
mkdir -p "$BIN_DIR"
cat > "$LAUNCHER" <<EOF
#!/usr/bin/env bash
exec "$VENV/bin/textual-themes-demo" "\$@"
EOF
chmod +x "$LAUNCHER"

echo ""
echo "Done. Launch the storybook with:"
echo "    textual-themes-demo"
case ":$PATH:" in
    *":$BIN_DIR:"*) ;;
    *)
        echo ""
        echo "Note: $BIN_DIR is not on your PATH. Add this to your shell profile:"
        echo "    export PATH=\"\$HOME/.local/bin:\$PATH\""
        ;;
esac
