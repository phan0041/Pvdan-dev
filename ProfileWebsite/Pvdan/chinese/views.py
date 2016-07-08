from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
import datetime


def index(request):
    return HttpResponse("Hello, world. You're at the chinese index.")


def phrase(request):
    now = datetime.datetime.now()
    return render(request, 'chinese-templates/phrase.html', {'current_date': now})


def sentence(request):
    return HttpResponse("Hello, world. You're at the chinese sentence page.")


def music(request):
    return HttpResponse("Hello, world. You're at the chinese music page.")