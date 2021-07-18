

# def event_picture(upload_picture):
#   randon_hex = secrets.token_hex(8)
#   _, f_ext = os.path.splitext(upload_picture.filename)
#   event_picture_fn = randon_hex + f_ext
#   picture_path =os.path.join(basedir, 'static/images/event_images/', event_picture_fn)

#   size = (1280,600)
#   i = Image.open(upload_picture)
#   i.thumbnail(size)
#   i.save(picture_path)

#   return event_picture_fn
