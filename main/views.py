from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models
from . import TextPreProcessor
from . import NewsEngine
from . import WeatherData
import concurrent.futures
 
def home(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main:userhome'))
    location = WeatherData.getLocation(request)
    executor = concurrent.futures.ThreadPoolExecutor()
    t1 = executor.submit(WeatherData.weather,location)
    if request.method == "POST":
        search = request.POST["search"]
        t2 = executor.submit(NewsEngine.GetNews,search)
        new_query = models.Query(ip_location=str(location["city"])+","+str(location["country"]),text_searched=search)
        new_query.save()
    else:
        t2 = executor.submit(NewsEngine.GetNewsByLocation,location)
    weather = t1.result()
    (query,articles) = t2.result()
    if query:
        query["no_of_results"] = len(articles)
        new_query_properties = models.PropertiesOfSearch(query=new_query,q=query["q"])
        new_query_properties.save()
    print(f"location : {location}\nweather : {weather}\nquery : {query}")
    return render(request,'main/home.html',{'location':location,'weather':weather,'articles':articles,'query':query})


@login_required(login_url='user:login')
def userhome(request):
    location = ""
    return render(request,'main/userhome.html',{'location':location})
 