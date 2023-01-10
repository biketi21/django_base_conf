from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.


def home(request):
    return render(request, "index.html")


def logout(request):
    logout(request)
    return print("logged out")
