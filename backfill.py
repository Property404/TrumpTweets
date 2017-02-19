import tweepy
import base64
import time
import json
import io
import MySQLdb
db = MySQLdb.connect("162.243.109.160","root","hunter2","trump");
c = db.cursor()

with open(r'C:\Users\Atlas\Desktop\trump tweets\TrumpTweets\all_trump_tweets.json') as json_data:
    masterlist = json.load(json_data)
for x in masterlist:
    status_json = x
    userobj =  status_json['user']
    userid = userobj['id_str']
    parsed_json = {'id' : status_json['id'], 'created_at' : status_json['created_at'],'user_id': ['userid'], 'text':status_json['text'], "favorite_count":  status_json['favorite_count'],"retweet_count" : status_json['retweet_count'],
                   "in_reply_to_user_id" : status_json['in_reply_to_user_id'],
                   'in_reply_to_status_id' : status_json['in_reply_to_user_id']}
    columns = ["id", "created_at",'user_id', "text", "favorite_count", "retweet_count", "in_reply_to_user_id",
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
    print(c.fetchall())
    print(values);
    a = io.open("markov.txt", "w",encoding="utf-8");
    a.write(markov);
    a.close();
with io.open(r'/home/hackfsu/TrumpTweets/all_trump_tweets.json', 'w') as json_data:
    json.dump(masterlist, json_data)
    os.close(json_data)
    print('\nhit limit going to sleep be back in 15\n')
    lastread = status_json.id
    print(lastread)