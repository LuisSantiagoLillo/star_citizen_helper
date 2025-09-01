For the complete documentation, see README.md.

Quick start:

1) Create venv and install requirements:
   python3 -m venv .venv
   . .venv/bin/activate
   pip install -r requirements.txt

2) Run the templated server (recommended):
   sudo .venv/bin/python3 sc_buttons_server.py

   Or run the inline-HTML version:
   sudo .venv/bin/python3 server.py

3) Open http://localhost:5000 (or your host IP:5000) in a browser.

Troubleshooting port 5000:
   sudo lsof -i :5000
   sudo kill -9 <PID>
