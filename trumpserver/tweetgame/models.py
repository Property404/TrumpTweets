from django.db import models

class Tweet(models.Model):
    tweet_id = models.IntegerField(max_length = 25)
    created_at= models.CharField(max_length = 50)
    text = models.TextField()
    favorite_count =  models.IntegerField(max_length = 25)
    retweet_count =  models.IntegerField(max_length = 25)
    in_reply_to_status_id = models.IntegerField(max_length = 25, null =True)
    in_reply_to_user_id = models.IntegerField(max_length = 25, null =True)
    hashtags = models.CharField(max_length = 200, null =True)

    def __unicode__(self):
        return self.text


