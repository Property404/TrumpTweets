import base64
import tweepy
import time
import json
from secrets import*
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
import time
import json
from secrets import*
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)
import MySQLdb
db = MySQLdb.connect("localhost","root","hunter2","trump");
c = db.cursor()
count = 0
def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print("hit rate limit")
            lastread = status_json.id
            print('\n' + lastread)
            print('\n' + count)
            time.sleep(15 * 60)

with open(r'/home/hackfsu/TrumpTweets/all_trump_tweets.json') as json_data:
    masterlist = json.load(json_data)
    masterlist.sort()
for x in masterlist:
    status_json = api.get_status(x)
    parsed_json = {'id' : status_json.id, 'created_at' : status_json.created_at, 'text':status_json.text, "favorite_count":  status_json.favorite_count,"retweet_count" : status_json.retweet_count,
                   "in_reply_to_user_id" : status_json.in_reply_to_user_id,
                   'in_reply_to_status_id' : status_json.in_reply_to_user_id}
    columns = ["id", "created_at", "text", "favorite_count", "retweet_count", "in_reply_to_user_id",
               "in_reply_to_status_id"]
    tweets = []
    markov = ""
    markov += parsed_json["text"];
    values = [
        str(parsed_json[x]) if x == "id" else (base64.b64encode(str(parsed_json[x]).encode("UTF8"))).decode("UTF8") for
        x in columns]
    tweets += values
    query = "INSERT IGNORE INTO tweets (" + ",".join(columns) + ") VALUES(" + values[0] + ",\"" + "\",\"".join(
        values[1::]) + "\");"
    print(query);
    c.execute(query);
    db.commit();
    print(c.fetchall());
    print(values);
    a = open("markov.txt", "w");
    a.write(markov);
    a.close();
    count += 1
    if count == 850:
        print('\nhit limit going to sleep be back in 15\n')
        lastread = status_json.id
        print('\n' + lastread)
        time.sleep(15 * 60)
    continue
