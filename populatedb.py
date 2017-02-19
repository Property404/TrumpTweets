import base64
import tweepy
import time
import json
from secrets import*
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
import MySQLdb
db = MySQLdb.connect("162.243.109.160","root","hunter2","trump");
c = db.cursor()
count = 0
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print("hit rate limit")
            time.sleep(15 * 60)
while True:
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
        for Status in limit_handled(tweepy.Cursor(api.user_timeline,user_id = "25073877",since_id= sinceid).items()):
            print("in tweet loop")
            parsed_json = Status_json
            markov += parsed_json.text;
            values  = [str(parsed_json.x) if x=="id" else (base64.b64encode(str(parsed_json[x]).encode("UTF8"))).decode("UTF8") for x in columns]
            tweets += values
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
