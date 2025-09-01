Instal requirements:
pip install -r requirements.txt

Execute with:
sudo .venv/bin/python3 server.py

Kill portserver:
kvothe@kvothe-ruh:~/Code/star_citicen_helper$ sudo lsof -i :5000
COMMAND  PID USER   FD   TYPE DEVICE SIZE/OFF NODE NAME
python3 5958 root    3u  IPv4  37790      0t0  TCP *:5000 (LISTEN)
kvothe@kvothe-ruh:~/Code/star_citicen_helper$ sudo kill -9 5958
