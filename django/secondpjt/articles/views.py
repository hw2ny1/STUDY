from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1><p>안녕하세요</p><p>모르겠어요</p></h1>")