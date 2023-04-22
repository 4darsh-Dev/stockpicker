from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


# it gives the index page.
def index(request):
    return render(request, 'index.html')

def live(request):
    return render(request, 'livemarket.html' )

def analyze(request):
    return render(request, 'analyze.html' )
