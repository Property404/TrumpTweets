from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the future. This is the past. All are welcome, but None shall pass.");
