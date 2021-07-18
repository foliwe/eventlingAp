import secrets
import os
from PIL import Image
from mainapp import basedir

def save_picture(upload_picture):
  randon_hex = secrets.token_hex(8)
  _, f_ext = os.path.splitext(upload_picture.filename)
  picture_fn = randon_hex + f_ext
  picture_path =os.path.join(basedir, 'static/images', picture_fn)

  size = (125,125)
  i = Image.open(upload_picture)
  i.thumbnail(size)
  i.save(picture_path)

  return picture_fn