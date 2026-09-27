# Repository Guidelines

## Project Identity & Sources of Truth

Codex project: `sc-helper`. Repository: [LuisSantiagoLillo/star_citizen_helper](https://github.com/LuisSantiagoLillo/star_citizen_helper). Default branch: `main`.

GitHub/local Git is authoritative for application code. [NEXUS/Projects/sc-helper](https://drive.google.com/drive/folders/1KPF4siIiPAdmLcPgLFNyevQdjh_6KQyr) is authoritative for supporting documentation. Never duplicate application source into Drive or treat chat history as durable documentation.

Use the existing [PROJECT_OVERVIEW.md](https://drive.google.com/file/d/1pZDLBRkMIl4wTIOD7WJbYPfp650zKOa3/view) as the general technical guide. Review and update it when changes materially affect architecture, stack, structure, runtime behavior, setup, networking, security, or major features. Use `Documentation/` for detailed guides, `Architecture/` for decisions/diagrams, `Research/` for investigations, `Assets/` for non-code assets, and `Notes/` for exploratory notes. Avoid unnecessary documents.

## Project Structure & Architecture

This Python 3.9+ Flask utility serves a LAN browser panel. JavaScript posts a `key` to `/simulate_key`; `keyboard.press_and_release` emits host keyboard input. Responses contain `message`.

- `sc_buttons_server.py`: preferred development entry point.
- `server.py`: older duplicate backend; currently also renders the shared template, despite outdated inline-HTML descriptions. Preserve consistent behavior until explicitly consolidating.
- `templates/index.html`: tabs and bindings, including placeholder `a` bindings.
- `static/scripts.js`: tab switching and requests.
- `static/styles.css`, `static/neumorphism.css`: layout and theme.
- `requirements.txt`: Flask and keyboard dependencies; no asset build step.

## Build, Test, and Development Commands

From the repository root:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python sc_buttons_server.py
```

Open `http://localhost:5000`; `python server.py` runs the alternate entry point. Linux real-keyboard integration generally requires `sudo .venv/bin/python3 sc_buttons_server.py`; reserve elevation for necessary integration checks. Consider Windows and Linux behavior.

## Development & Coding Conventions

Before editing, inspect `git status`, the current branch, relevant files, and existing behavior. Prefer incremental changes, preserve working functionality unless explicitly replacing it, and avoid unnecessary dependencies.

Keep code, comments, documentation, identifiers, technical files, and commit messages in English. Use four-space Python/JavaScript/HTML indentation, Python `snake_case`, JavaScript `camelCase`, and hyphenated CSS classes. Preserve surrounding CSS formatting; no formatter or linter is configured.

## Validation & Review

For substantial work: inspect, plan, implement, test, review the diff, report results, and update affected durable documentation. Distinguish verified facts, assumptions, proposals, and future ideas.

For meaningful code changes, identify affected components, run applicable checks, verify Flask startup and relevant routes, and check JavaScript/backend interaction when modified. Report tested and untested behavior explicitly.

No automated suite or coverage threshold currently exists. Add route tests under `tests/test_*.py` using `unittest` and Flask's test client; run `python -m unittest discover -s tests`. Mock keyboard emission. Cover successful requests, missing/invalid input, and keyboard failures. Check tabs and responsive layouts for UI changes.

## Git & Pull Requests

Use focused, descriptive imperative commits; history also includes `docs:` prefixes. Describe behavior changes and validation in PRs, link relevant issues, and include screenshots for UI changes. Do not push, merge, force-push, rewrite history, or delete branches without explicit instructions.

## Security Requirements

Both apps listen on `0.0.0.0:5000` without authentication and accept keyboard input. Treat them as trusted-LAN utilities; never expose them directly to the public Internet.

When changing input handling, validate actions server-side and prefer an allowlist of supported actions/keybindings. Do not expose arbitrary commands, shell execution, or arbitrary keyboard input without explicit justification for the latter. Use least privilege and minimal network exposure; never weaken security for convenience. Never hardcode secrets or commit credentials, `.venv/`, or generated caches.
