import base64
import tweepy
import time
import json
from secrets import *
api = tweepy.API(auth)
import MySQLdb
c = db.cursor()
count = 0
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print("hit rate limit")
            time.sleep(15 * 60)
    q= "SELECT id from tweets";
    c.execute(q);
    l = (c.fetchall());
    sinceid = l[-1][0]
    print(sinceid)
    columns = ["id", "created_at","text","favorite_count","retweet_count","in_reply_to_user_id","in_reply_to_status_id"]
    def load_tweets(user_id,since_id):
        tweets = []
        markov = ""
        print("after markov")
        for status in limit_handled(tweepy.Cursor(api.user_timeline,user_id ="25073877",since_id = sinceid).items()):
            print("in tweet loop")
            markov += status.text
            values  = [str(status.id), str(status.created_at), str(status.favorite_count), str(status.text), str(status.retweet_count), str(status.in_reply_to_user_id), str(status.in_reply_to_status_id) ]
            tweets += (base64.b64encode(str(values).encode("UTF8"))).decode("UTF8")
            query = "INSERT IGNORE INTO tweets ("+",".join(columns)+") VALUES("+values[0]+",\""+"\",\"".join(values[1::])+"\");"
            print(query);
            c.execute(query);
            db.commit();
            print(c.fetchall());
            print(values);
        a = open("markov.txt","w");
        a.write(markov);
        a.close();
    print("before load")
    load_tweets(user_id= "25073877", since_id = sinceid)
    count +=1
    if count == 899:
        print('\nhit limit going to sleep be back in 15\n')
        print(time.gmtime())
        time.sleep(15 * 60)
    #last_tweet = status_json.id
    #print[last_tweet]
