import tweepy
import time
import json
import django
from models.py import Tweet

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            time.sleep(15 * 60)


for status in limit_handled(tweepy.Cursor(api.user_timeline,user_id = "25073877").items()):
    parsed_json = json.loads(status)
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
