import tweepy
import MySQLdb

consumer_key = 'QP7MbFO95FieQ5H7rAN0y4Pyx'
consumer_secret = 'omILtAWJlKcrSrxcuxFSHe46SMzU00ufyebqJVzVO7CbUFtE8C'
access_token = '832832529757564928-zFGSnlBgFZIzLR8lHDkzt1r2Mu3dGED'
access_token_secret = 'shGM3d38uVk37zgMEbEu2e7nKF456sDxq9ml6yrfGbW1d'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

#db code
ipaddress = "162.243.109.160"
user = "root"
password = "hunter2"
dbname = "trump"
db = MySQLdb.connect(ipaddress,user,password,dbname);