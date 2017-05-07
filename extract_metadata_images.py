from PIL import Image, ExifTags
from os import rename

from os import listdir
from os.path import isfile, join
import os

path = 'D:/Users/Eric Salas/Documents/Google Drive/Google Fotos/2013'


onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

for fileitem in onlyfiles:

    file2open = fileitem
    extension = file2open.split('.')[-1]
    print('File to open:' + file2open)
    try:
        img = Image.open(path +'/'+ file2open)
        exif = {ExifTags.TAGS[k]: v for k, v in img._getexif().items() if k in ExifTags.TAGS}
        img.close()
    except:
        print('Failed to open file:' + file2open)
        continue


    if exif.has_key("DateTimeOriginal"):
        filename = str(exif['DateTimeOriginal'])+ '.' + extension
        filename = filename.replace(':' , '-')
        print('DateTimeOriginal:' + str(exif['DateTimeOriginal']))
        print('File to save:' + filename)
        try:
            rename(path +'/'+ file2open, path +'/'+ 'output_folder/' + filename)
        except:
            print('Failed to save file:' + file2open)
    else:
        print('No DateTimeOriginal key in file:' + file2open)
print('end')