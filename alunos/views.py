from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h1>João o Louco de Dubai Sport Club (Al Nassir)</h1>')

# Create your views here.