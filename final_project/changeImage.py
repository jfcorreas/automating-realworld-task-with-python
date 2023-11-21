#!/usr/bin/env python

from PIL import Image
from pathlib import Path

images_path = Path.cwd() / 'supplier-data' / 'images'

for f in Path(images_path).iterdir():
  if f.suffix == '.tiff':
    img = Image.open(f)
    img.convert('RGB').resize((600,400)).save(images_path / f.with_suffix('.jpeg').name, "JPEG") 