import requests
import re
import json
from pathlib import Path

URL = "https://www.invader-spotter.art/news.php"
DATA_FILE = Path("last_ajout.json")

html = requests.get(URL, timeout=30).text

# Extract lines containing "Ajout"
lines = re.findall(r".*Ajout.*", html)

if DATA_FILE.exists():
    old = json.loads(DATA_FILE.read_text())
else:
    old = []

new = [l for l in lines if l not in old]

if new:
    print("NEW AJOUT FOUND:")
    for n in new:
        print(n)
    DATA_FILE.write_text(json.dumps(lines))
    exit(1)  # trigger notification
else:
    print("No new Ajout")
