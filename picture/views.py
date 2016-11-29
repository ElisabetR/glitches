import os
from random import randint
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
import os
import random
#from urllib.request import urlopen, urlretrieve

#from bs4 import BeautifulSoup

#url = "http://imgur.com/gallery/qO3N8"
#html = urlopen(url)
#soup = BeautifulSoup(html, 'html.parser')

#images = []
my_media_root = settings.MEDIA_ROOT
#for i in range(0, 5):
   # img = soup.findAll('img')[i].get('src')
   # img = "http://" + img[2:]
   # images.append(img)

#   urlretrieve(images[0], os.path.join(my_media_root,  ))


def index(request):
    # ...

    filename_midi = os.path.join(my_media_root, '0006.mid')
    #raise Exception(os.path.join(my_media_root, '0006.mid'))
    with open(filename_midi, 'rb') as m:
        midi_content = m.read()

    images = []
    for i in range(0, 8):
        filename_jpg = os.path.join(my_media_root, getRandomFile(my_media_root))
        images.append(filename_jpg)


    for img in images:
        with open(img, 'rb') as p:
            jpg_content = p.read()

        start = randint(300, 8000)
        finish = start + 100

        copy_midi = midi_content[3500:3600]
        delete_jpg = jpg_content[3500:3600]
        hex_string_jpg = jpg_content.replace(delete_jpg, copy_midi)

        filename_out = os.path.join(my_media_root, str(images.index(img)) + '.jpg')
        with open(filename_out, "wb") as fout:
            fout.write(hex_string_jpg)



    return render(request, 'picture/index.html')


def getRandomFile(path):

    """
    Returns a random filename, chosen among the files of the given path.
    """
    files = os.listdir(my_media_root)

    file_index = random.randrange(7, len(files))

    return files[file_index]