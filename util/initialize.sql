use trump;
drop table tweets;
create table tweets(id BIGINT NOT NULL PRIMARY KEY,
created_at TEXT,
user_id TEXT,
text TEXT,
favorite_count TEXT,
retweet_count TEXT,
in_reply_to_status_id TEXT,
in_reply_to_user_id TEXT,
hashtags TEXT);

