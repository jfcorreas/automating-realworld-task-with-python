#! /usr/bin/env python3

from pathlib import Path
import requests

source_path = Path.cwd() / 'supplier-data' / 'descriptions'
# web_service_url = 'http://<linux-instance-external-ip>/fruits/'

for f in Path(source_path).iterdir():
  with open(f) as fruit_file:
    description_lines = fruit_file.readlines()
    fruit_entry = {
      'name': description_lines[0].rstrip(),
      'weight': int(description_lines[1].split()[0].rstrip()),
      'description': description_lines[2].rstrip(),
      'image_name': '{}.jpeg'.format(f.stem)
    }
#    res = requests.post(web_service_url, fruit_entry)
#    res.raise_for_status()
    