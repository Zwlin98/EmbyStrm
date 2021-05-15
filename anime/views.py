from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Bangumi


def index(request):
    latest_anime_list = Bangumi.objects.all()
    return render(request, 'index.html', {"latest_anime_list": latest_anime_list})
