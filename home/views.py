# No arquivo views.py do aplicativo home

from django.shortcuts import render

def home(request):
    return render(request, 'home/home.html')
