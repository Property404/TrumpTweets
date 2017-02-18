from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

main = open("/var/www/trumptweets/trumpserver/tweetgame/static/index.html").read();
def index(request):
    return HttpResponse(main);
