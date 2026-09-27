#!/usr/bin/env bash
# Start the preferred server independently of the caller's working directory.
set -eu

SCRIPT_DIR="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_DIR="$(dirname -- "$SCRIPT_DIR")"

# File managers do not necessarily provide a terminal for sudo or server logs.
if [[ ! -t 0 || ! -t 1 ]]; then
    exec gnome-terminal -- "$SCRIPT_DIR/start-server.sh"
fi

pause_on_error() {
    local status=$?
    if (( status != 0 )); then
        printf '\nServer startup failed (exit %s). Press Enter to close.\n' "$status"
        read -r _ || true
    fi
}
trap pause_on_error EXIT

cd -- "$PROJECT_DIR"
PYTHON="$PROJECT_DIR/.venv/bin/python3"

if [[ ! -x "$PYTHON" ]]; then
    printf 'Missing virtual environment. Run these commands in %s:\n' "$PROJECT_DIR" >&2
    printf 'python3 -m venv .venv\n.venv/bin/python3 -m pip install -r requirements.txt\n' >&2
    exit 1
fi

if ! "$PYTHON" -c 'import flask, keyboard'; then
    printf '\nInstall dependencies first: .venv/bin/python3 -m pip install -r requirements.txt\n' >&2
    exit 1
fi

printf 'Starting Star Citizen Helper: http://localhost:5000\n'
printf 'Keep this terminal open. Press Ctrl+C to stop the server.\n'
printf 'Administrator permission is required for global keyboard input.\n\n'
sudo -- "$PYTHON" "$PROJECT_DIR/sc_buttons_server.py"
