from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from . import models


def userlogin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('main:userhome'))
    if request.method == "POST":
        email = request.POST['email']
        username = User.objects.get(email=email)
        password = request.POST['password']
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('main:userhome'))
        else:
            return HttpResponse("Failed")
    return render(request,'userauth/login.html')



@login_required
def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:home'))



def newuser(request):
    pass
