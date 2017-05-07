from PIL import Image, ExifTags
from os import rename

file2open = "mi foto.jpg"
print('File to open:' + file2open)
img = Image.open(file2open)
exif = { ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS }
img.close()
if exif.has_key("DateTimeOriginal"):
    filename = str(exif['DateTimeOriginal'])+'.jpg'
    filename = filename.replace(':' , '-')
    print('DateTimeOriginal:' + str(exif['DateTimeOriginal']))
    print('File to save:' + filename)
    rename(file2open, 'output_folder/' + filename)
else:
    print('No DateTimeOriginal key in file:' + file2open)
print('end')