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
c.execute("""SELECT id, text from tweets WHERE user_id='realDonaldTrump' or user_id='POTUS';""");
real_tweets = [[m[0], b64decode(m[1].encode("UTF-8"))] for m in c.fetchall()]
corpus = open("/var/www/trumptweets/trumpserver/tweetgame/static/markov.txt", "r").read();
tm = markovify.Text(corpus);


main = open("/var/www/trumptweets/trumpserver/tweetgame/static/index.html").read();
page_realorfake = open("/var/www/trumptweets/trumpserver/tweetgame/static/realorfake.html").read();

page_compare = open("/var/www/trumptweets/trumpserver/tweetgame/static/compare.html").read();

def getRandom(real):
    juice = randint(0,len(real_tweets)-1);
    sentence = real_tweets[juice][1] if real else tm.make_sentence().encode("UTF8")
    sentence = sentence.decode("UTF-8").replace('"',"''").replace("\n","\\n").encode("UTF-8");
    return  b"{\"real\":"+str(real).encode("UTF8")+b",\"sentence\":\""+sentence+b"\", \"id\":\""+str(real_tweets[juice][0]).encode("UTF-8")+b"\"}"
def getScore(tweet):
    tokens = tweet.split();
    score = 0;
    for i in range(0, len(tokens)):
        for j in range(0, len(tokens[i::])):
            if " ".join(tokens[i:i+j+1]) in corpus:
                score += j+1
    return score;
def scoretweet(request):
    return HttpResponse(getScore(request.GET["tweet"]));

def compare(request):
    return HttpResponse(page_compare);

def index(request):
    return HttpResponse(main);
def realorfake(request):
    return HttpResponse(page_realorfake);
    
def test(request):
    return HttpResponse("Ugh");
def random(request):
    return HttpResponse(getRandom(randint(0,1)));
def morerandom(request):
    return HttpResponse(getRandom(false));
