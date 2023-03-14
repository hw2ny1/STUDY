from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>작고 소중한 나의 첫 Django PJT</h1>")