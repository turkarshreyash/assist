from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def logoutfunction(request):
    logout(request)
    return HttpResponseRedirect(reverse('home:homepage'))

def homepage(request):
    return render(request,'homeassist/home.html')
