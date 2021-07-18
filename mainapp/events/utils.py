import secrets
import os
from PIL import Image
from mainapp import basedir


def event_picture(upload_picture):
  randon_hex = secrets.token_hex(8)
  _, f_ext = os.path.splitext(upload_picture.filename)
  picture_fn = randon_hex + f_ext
  picture_path =os.path.join(basedir, 'static/images/event_images', picture_fn)
  picture_path_small =os.path.join(basedir, 'static/images/event_images/thumbnail', picture_fn)

  
  i = Image.open(upload_picture)
  i.resize((1280, 600))
  i.save(picture_path)



  i = Image.open(upload_picture)
  i.thumbnail((520, 200))
  i.save(picture_path_small)
  print(i.size)

  return picture_fn