import base64
import tweepy
import time
import json
from secrets import*
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
import MySQLdb
db = MySQLdb.connect("localhost","root","hunter2","trump");
c = db.cursor()
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)
while True:
    q= "SELECT id from tweets";
    c.execute(q);
    l = (c.fetchall());
    sinceid = max(l)
    maxid = min(l)
    columns = ["id", "created_at","text","favorite_count","retweet_count","in_reply_to_user_id","in_reply_to_status_id"]
    def load_tweets(user_id,max_id):
        tweets = []
        markov = ""
        for status in limit_handled(tweepy.Cursor(api.user_timeline,user_id = "25073877",max_id = maxid).items()):
            parsed_json = status._json
            markov += parsed_json["text"];
            values  = [str(parsed_json[x]) if x=="id" else (base64.b64encode(str(parsed_json[x]).encode("UTF8"))).decode("UTF8") for x in columns]
            tweets += values
            query = "INSERT IGNORE INTO tweets ("+",".join(columns)+") VALUES("+values[0]+",\""+"\",\"".join(values[1::])+"\");";
            print(query);
            c.execute(query);
            db.commit();
            print(c.fetchall())
            print(values);
        a = open("markov.txt","w");
        a.write(markov);
        a.close();
    load_tweets("25073877");
    continue
"""

    twit = Tweet.objects.create(tweet_id = parsed_json['id'], created_at = parsed_json['created_at'], text = parsed_json['text'],
                          favorite_count = parsed_json['favorite_count'], retweet_count = parsed_json['retweet_count'],
                          in_reply_to_status_id= parsed_json['in_reply_to_status_id'], in_reply_to_user_id = parsed_json['in_reply_to_user_id'])
   twit.save()
for status in limit_handled(tweepy.Cursor(api.user_timeline,user_id = "25073877").items()):
    parsed_json = json.loads(status)

    twit = Tweet.objects.create(tweet_id = parsed_json['id'], created_at = parsed_json['created_at'], text = parsed_json['text'],
                          favorite_count = parsed_json['favorite_count'], retweet_count = parsed_json['retweet_count'],
                          in_reply_to_status_id= parsed_json['in_reply_to_status_id'], in_reply_to_user_id = parsed_json['in_reply_to_user_id'])
   twit.save()
   """
