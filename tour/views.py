from django.shortcuts import render
import requests
import json
from . import info
# Create your views here.

def home(request):
    tourInfo = info.InfoFunc()
    return render(request, 'home.html', {'tourInfo': tourInfo})
