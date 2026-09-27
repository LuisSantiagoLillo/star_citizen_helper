# Star Citizen Helper

Simple Flask-based web interface to trigger Star Citizen keybinds from any device on your local network. Buttons in the UI send requests to the server, which uses the `keyboard` library to simulate key presses on the host machine where the game runs.

Note: Sending global keystrokes typically requires elevated privileges. On Linux, this means running the app with `sudo`.

## Features
- Core controls for doors, lights, docking/landing, and Mobiglass (`F1`–`F12`).
- Shield/Power panel with directional shield controls and energy presets.
- Battle mode: countermeasures, power distribution, and targeting helpers.
- Two server entry points:
  - `sc_buttons_server.py` (templated UI via `templates/` + `static/`).
  - `server.py` (self-contained version with inline HTML).

## Requirements
- Python 3.9+
- `pip`
- OS support:
  - Linux: `keyboard` library usually needs root to emit system-wide key events.
  - Windows/macOS: Behavior may vary; administrator privileges may be required.

Python dependencies are listed in `requirements.txt`:

```
flask
keyboard
```

## Setup
Create a virtual environment and install dependencies:

```
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Run
### Ubuntu desktop launcher

After completing Setup, use `scripts/sc-helper.desktop` to start the server
with a double click from a desktop that supports launchers. If Ubuntu asks,
right-click the shortcut and select **Allow Launching** first. Some file
managers display `.desktop` files as text; use the desktop shortcut instead.

The launcher opens a terminal, requests your sudo password when needed, and
starts `sc_buttons_server.py` with the project's virtual environment. Open
http://localhost:5000 in your browser. Keep the terminal open and press **Ctrl+C**
to stop the server. Startup errors remain visible until you press Enter.

`scripts/start-server.sh` resolves the repository location automatically and
can also be run from any working directory. It requires Bash, GNOME Terminal
when launched without a terminal, sudo, and the dependencies from Setup.
It does not install packages or change sudo permissions.

The `.desktop` file's `Exec` path is configured for this checkout at
`/home/kvothe/Code/star_citicen_helper`. If you move or clone the repository
elsewhere, update that path and any installed copies of the shortcut.

### Command line

Run with elevated privileges so key events can be sent globally:

```
sudo .venv/bin/python3 sc_buttons_server.py
```

Alternatively, the inline-HTML version:

```
sudo .venv/bin/python3 server.py
```

The server listens on `0.0.0.0:5000`. Open from the same machine or another device on your LAN:

- http://localhost:5000
- http://<your-host-ip>:5000

## Security Notes
- Do not expose this server to the internet. It has no authentication and can send keystrokes to your machine.
- Prefer running on a trusted LAN or bind to `127.0.0.1` and reverse-proxy with proper auth if needed.
- Consider creating a limited user and only elevating the minimal parts required in your environment.

## Troubleshooting
- Port already in use (5000):

  ```
  sudo lsof -i :5000
  sudo kill -9 <PID>
  ```

- Keyboard events not triggering:
  - Ensure you are running with the required privileges (`sudo` on Linux).
  - Close other overlays that may intercept input.
  - Verify your Star Citizen keybinds match the buttons you’re pressing.

## Development
- Main app files: `sc_buttons_server.py`, `server.py`.
- Templates/CSS/JS for the templated app: `templates/`, `static/`.
- Feel free to adjust the button bindings in `templates/index.html` and `static/scripts.js`.
