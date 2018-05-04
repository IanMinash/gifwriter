from PIL import Image, ImageDraw, ImageSequence, ImageFont
import urllib.request
import os

def watermarker(url, text, font, size=50):
    input_gif = Image.open(urllib.request.urlopen(url))
    width, height = input_gif.size
    frames = [frame.copy() for frame in ImageSequence.Iterator(input_gif)]
    text = text
    font = ImageFont.truetype(os.path.join(settings.FONTS_DIR, font), size=(0.1*height))
    for frame in frames:
        writer = ImageDraw.Draw(frame)
        w, h = font.getsize(text)
        writer.text(((width-w)/2, (height-h)/2), text, font=font)
    output_gif = frames[0]
    output_gif.save(fp=os.path.join(settings.STATIC_DIR, (text+".gif")),
                    format='gif', save_all=True, append_images=frames[1:])
