from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import NewsEngine
from django.contrib.gis.geoip2 import GeoIP2
from . import WeatherData
import threading
from . import TextPreProcessor

g = GeoIP2()



def home(request):
    articles = None
    result = None
    error = None
    weather = None
    no_of_results = 0
    if request.method == "POST":
        search = request.POST['search']
        result = TextPreProcessor.preprocessing(search)
        try:
            articles = NewsEngine.GetNews(result)
        except:
            error = "Error :-("

        
    else:
        try:
            location = g.country(NewsEngine.get_client_ip(request))["country_code"]
            print(location)
            (articles,result) = NewsEngine.GetNews(location)
        except:
            no_of_results = -1
        try:
            weather = WeatherData.weather(g.city(NewsEngine.get_client_ip(request)))
            print(weather)
        except:
            weather = None
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main:userhome'))
    if articles:
        no_of_results = len(articles)
    elif not no_of_results == -1:
        no_of_results = 0
    
    return render(request,'main/home.html',{'no_of_results':no_of_results,'articles':articles,'results':result, 'error':error})


@login_required(login_url='user:login')
def userhome(request):
    location = ""
    return render(request,'main/userhome.html',{'location':location})
