from django.shortcuts import render
import giphy_client
from giphy_client.rest import ApiException
from django.conf import settings
from random import randint
from main.watermarker import watermarker

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
            # Search Endpoint
        api_response = giphy.gifs_search_get(
            giphy_api_key, query, limit=24, lang=lang)
        # [randint(0, 25)].images.downsized_large.url
        for i in range(0, len(api_response.data)):
            gifs.append(api_response.data[i].images.downsized_medium.url)
    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
    request.session['urls'], request.session['query'] = gifs, query
    return render(request, 'main/results.html', context={'gifs':gifs})
    
def chosen(request):
    index = int(request.GET.get('gif'))
    chosen = request.session['urls'][index]
    text = request.session['query']
    return render(request, "main/chosen.html", context={'chosen':chosen, 'text':text})