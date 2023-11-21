#!/usr/bin/env python3

import requests
from pathlib import Path

images_path = Path.cwd() / 'supplier-data' / 'images'
url = "http://localhost/upload/"

for image_file in Path(images_path).iterdir():
  if image_file.suffix == '.jpeg':
    with open(image_file, 'rb') as opened:
      r = requests.post(url, files={'file': opened})