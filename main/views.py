from django.shortcuts import render
from main.forms import User_textForm
from paralleldots import set_api_key, emotion
import giphy_client
from giphy_client.rest import ApiException
from django.conf import settings
from random import randint

# Create your views here.
set_api_key(settings.PARALLEL_API)
giphy_api_key = settings.GIPHY_API  # str | Giphy API Key.
giphy = giphy_client.DefaultApi()
# str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
lang = 'en'


def home(request):
    submit = False
    if request.method == "POST":
        form = User_textForm(request.POST)
        if form.is_valid():
            clean = form.cleaned_data
            feeling = emotion(clean['text'])
            # str | Search query term or prhase.
            query = feeling['emotion']['emotion']
            try:
                # Search Endpoint
                api_response = giphy.gifs_search_get(
                    giphy_api_key, query, lang=lang)
                gifurl = api_response.data[randint(0, 25)].images.downsized_large.url
                text = clean['text']
            except ApiException as e:
                print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)
        
        form.gif=gifurl
        form.save()
        submit=True
        return render(request, "main/home.html", {'form': form, 'url': gifurl, 'submitted': submit, 'text':text})
    else:
        form=User_textForm()
        return render(request, "main/home.html", {'form': form, 'submitted': submit})
