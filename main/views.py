from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import NewsEngine
from django.contrib.gis.geoip2 import GeoIP2


g = GeoIP2()



def home(request):
    articles = None
    country = None
    category = None
    words = None
    if request.method == "POST":
        search = request.POST['search']
        (articles,country,category,words) = NewsEngine.GetNews(search)
        words = words.split()
    else:
        try:
            location = g.country(NewsEngine.get_client_ip(request))["country_code"]
            print(location)
            (articles,country,category,words) = NewsEngine.GetNews(location)
        except:
            pass
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main:userhome'))
    return render(request,'main/home.html',{'articles':articles,'country':country,'category':category,'words':words})


@login_required(login_url='user:login')
def userhome(request):
    location = ""
    return render(request,'main/userhome.html',{'location':location})
