from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'HTML/800.html')

def home(request):
    return render(request, 'HTML/home.html')

def seasons(request):
    return render(request, 'HTML/seasons.html')

def characters(request):
    return render(request, 'HTML/characters.html')

def about(request):
    return render(request, 'HTML/about.html')

def contact(request):
    return render(request, 'HTML/contact.html')