from PIL import Image, ImageDraw, ImageSequence, ImageFont
import urllib.request
import os, string, random, numpy, imageio
from ast import literal_eval
from django.conf import settings

def id_generator(size=6, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size)) + ".gif"

def watermarker(url, text, font, color):
    input_gif = Image.open(urllib.request.urlopen(url))
    width, height = input_gif.size
    color = literal_eval(color)
    sequence = []
    frameNo = 0
    text = text
    font = ImageFont.truetype(font, size=int(0.2*height))
    w, h = font.getsize(text)
    while True:
        try:
            input_gif.seek(frameNo)
        except EOFError:
            break

        new_gif = Image.new("RGB", input_gif.size)
        new_gif.paste(input_gif)

        draw = ImageDraw.Draw(new_gif)        
        #draw here
        draw.text(((width-w)/2, (height-h)/2), text, font=font, fill=color)
        open_cv_image = numpy.array(new_gif)
        sequence.append(open_cv_image)
        frameNo += 1
    out_gif = os.path.join(settings.GIFS_DIR, id_generator()) #Output location
    imageio.mimsave(out_gif, sequence)
    return out_gif
    