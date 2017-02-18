from django.shortcuts import render
import markovify
from random import *
from base64 import*
import MySQLdb
import json
import logging
logger = logging.getLogger(__name__);
# Create your views here.
from django.http import HttpResponse
# Load from database
db = MySQLdb.connect("localhost","root","hunter2","trump");
c = db.cursor()
c.execute("""SELECT text from tweets;""");
real_tweets = [b64decode(m[0].encode("UTF-8")) for m in c.fetchall()]
corpus = open("/var/www/trumptweets/trumpserver/tweetgame/static/markov.txt", "r").read();
tm = markovify.Text(corpus);


main = open("/var/www/trumptweets/trumpserver/tweetgame/static/index.html").read();
def getRandom():
    real = randint(0,1);
    sentence = choice(real_tweets) if real else tm.make_sentence().encode("UTF8")
    return  b"{"+str(real).encode("UTF8")+b",\""+sentence+b"\"}"

def index(request):
    return HttpResponse(main);
    
def test(request):
    return HttpResponse("Ugh");
def random(request):
    return HttpResponse(getRandom());
