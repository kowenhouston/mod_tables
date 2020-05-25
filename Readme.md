# Mod_tables POC
Create firewall rules by hitting a URL
```
apt update && apt install -y python3-pip python3-venv git
python3 -m venv /opt/mod_tables/venv/
source /opt/mod_tables/venv/bin/activate
pip install flask
git clone https://github.com/kowenhouston/mod_tables /opt/mod_tables/
mv /opt/mod_tables/mod_tables/ /opt/mod_tables/web/
python3 /opt/mod_tables/web/mod_tables.py
```

Then hit your URL to add your IP:
* http://<IP>/ip/add

Or Hit the following to add a random IP:
* http://<IP>/ip/add/<IP>/