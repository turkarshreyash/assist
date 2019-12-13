from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import NewsEngine



def home(request):
    articles = None
    if request.method == "POST":
        search = request.POST['search']
        articles = NewsEngine.GetNews(search)


    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main:userhome'))
    return render(request,'main/home.html',{'articles':articles})


@login_required(login_url='user:login')
def userhome(request):
    location = ""
    return render(request,'main/userhome.html',{'location':location})
