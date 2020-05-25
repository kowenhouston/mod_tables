# Mod_tables POC
Create firewall rules by hitting a URL
```
apt update && apt install -y python3-pip python3-venv git
python3 -m venv /opt/mod_tables/venv/
source /opt/mod_tables/venv/bin/activate
pip install flask
git clone https://github.com/kowenhouston/mod_tables /opt/mod_tables/web/
chmod +x /opt/mod_tables/web/start.sh
/opt/mod_tables/web/start.sh
```

Then hit your URL to add your IP:
* http://YOUR_IP:5000/ip/add

Or Hit the following to add a chosen IP:
* http://YOUR_IP:5000/ip/add/IP_YOU_WANT_TO_ADD/