from django.shortcuts import render
import giphy_client
from giphy_client.rest import ApiException
from django.conf import settings
from random import randint
from main.watermarker import watermarker
from django.http import HttpResponse
import os

# Create your views here.
giphy_api_key = settings.GIPHY_API  # str | Giphy API Key.
giphy = giphy_client.DefaultApi()
# str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
lang = 'en'


def home(request):
    return render(request, "main/home.html")


def result(request):
    query = request.GET.get('query')
    gifs = []
    try:
        # RPC for fetching GIFs
        api_response = giphy.gifs_search_get(
            giphy_api_key, query, limit=24, lang=lang) 
        for i in range(0, len(api_response.data)):
            gifs.append(api_response.data[i].images.downsized_medium.url)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
    request.session['urls'], request.session['query'] = gifs, query
    #Render the response and pass the GIF to the template
    return render(request, 'main/results.html', context={'gifs':gifs})

Fonts = {
    'Oleo Script':os.path.join(settings.FONTS_DIR, 'Oleo.ttf'),
    'Roboto':os.path.join(settings.FONTS_DIR, 'Roboto.ttf'),
    'Slabo 27px':os.path.join(settings.FONTS_DIR, 'Slabo.ttf'),
    'Titan One':os.path.join(settings.FONTS_DIR, 'TitanOne.ttf'),
    'Uni Sans CAPS Heavy Italic':os.path.join(settings.FONTS_DIR, 'UniSans.otf'),
}    
def chosen(request):
    index = int(request.GET.get('gif'))
    chosen = request.session['urls'][index]
    text = request.session['query']
    if request.method == 'POST':
        global Fonts
        gif_dir = watermarker(chosen, text, Fonts[request.POST.get('font')], request.POST.get('color'))
        gif = open(gif_dir, 'rb').read()
        response = HttpResponse(gif, content_type='image/gif')
        response['Content-Disposition'] = 'attachment; filename="the.gif"'
        os.remove(gif_dir)
        return response
    else:
        return render(request, "main/chosen.html", context={'chosen':chosen, 'text':text})