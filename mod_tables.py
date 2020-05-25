from flask import Flask
from markupsafe import escape
from flask import request

import shlex, subprocess
app = Flask(__name__)

ALLOW_VNC_COMMAND = "iptables -I INPUT -p tcp -s <IP> --dport 5901 -j ACCEPT"
ALLOW_SSH_COMMAND = "iptables -I INPUT -p tcp -s <IP> --dport 22 -j ACCEPT"

def run_commands(ip):
    commands = [ALLOW_SSH_COMMAND, ALLOW_VNC_COMMAND]
    for command in commands:
        command = command.replace('<IP>', escape(ip))
        command = command.split()
        subprocess.call(command)
    return f'{ip} allowed'

@app.route('/ip/add/<ip>')
def add_ip(ip):
    return run_commands(escape(ip))

@app.route('/ip/add/', methods=['GET'])
def add_my_ip():
    return run_commands(escape(request.remote_addr))