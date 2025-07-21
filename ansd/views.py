from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, '800.html')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')