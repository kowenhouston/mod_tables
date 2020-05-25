from flask import Flask
from markupsafe import escape
from flask import request
import re
import subprocess

app = Flask(__name__)

ALLOW_VNC_COMMAND = "iptables -I INPUT -p tcp -s <IP> --dport 5901 -j ACCEPT"
ALLOW_SSH_COMMAND = "iptables -I INPUT -p tcp -s <IP> --dport 22 -j ACCEPT"
#For Debugging
#ALLOW_VNC_COMMAND = "echo iptables -I INPUT -p tcp -s <IP> --dport 5901 -j ACCEPT"
#ALLOW_SSH_COMMAND = "echo iptables -I INPUT -p tcp -s<IP> --dport 22 -j ACCEPT"

IP_REGEX = re.compile("^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$")

def run_commands(ip):
    if IP_REGEX.match(ip):
        commands = [ALLOW_SSH_COMMAND, ALLOW_VNC_COMMAND]
        for command in commands:
            command = command.replace('<IP>', escape(ip))
            command = command.split()
            subprocess.call(command)
        return f'{ip} allowed'
    else:
        return 'IP Not detected'

@app.route('/ip/add/<ip>')
def add_ip(ip):
    return run_commands(escape(ip))

@app.route('/ip/add/', methods=['GET'])
def add_my_ip():
    return run_commands(escape(request.remote_addr))