from PIL import Image
from pathlib import Path

images_path = Path.cwd() / 'images'
dest_path = Path.cwd() / 'icons'

for f in Path(images_path).iterdir():
  img = Image.open(f)
  img.rotate(90).resize((128,128)).save(dest_path / f.with_suffix('.jpeg').name) 