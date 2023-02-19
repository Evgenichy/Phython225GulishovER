from django.shortcuts import render
from .models import Mapp


def index(requests):
    planers = Mapp.objects.all()
    return render(requests, 'index.html', {'planers': planers})
