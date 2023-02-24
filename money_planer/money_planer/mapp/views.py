from django.shortcuts import render
from .models import Mapp


def index(requests):
    planers = Mapp.objects.all()
    return render(requests, 'mapp/index.html', {'planers': planers})
