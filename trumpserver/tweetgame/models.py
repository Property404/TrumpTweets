from django.db import models

class Tweet(models.Model):
    tweet_id = models.IntergerField(max_length = 25)
    created_at= models.CharField(max_length = 50)
    text = models.Textfield(max_length = 200)
    favorite_count =  models.IntergerField(max_length = 25)
    retweet_count =  models.IntergerField(max_length = 25)
    in_reply_to_status_id = models.IntergerField(max_length = 25, null =True)
    in_reply_to_user_id = models.IntergerField(max_length = 25, null =True)
    hashtags = models.Charfield(max_length = 200, null =True)
