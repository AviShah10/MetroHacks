import json
import tweepy

ACCESS_TOKEN = '1132298551411630080-TxbsTVojtHBCpZC0pjgCbDYsx3XcwO'
ACCESS_SECRET = 'MjksGvOspEXk7EF8HUVgmgHJpTIgAifI5SY8SWpLyqeaI'
CONSUMER_KEY = '9Q7tOjRTcnk0GDgLGfMYESmFx'
CONSUMER_SECRET = 'Oy98g2cuXlPkTs75akfeVvDq2YiPiMvzSP9e4Z2wOronPBaGDp'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

for status in tweepy.Cursor(api.search, q="Giraffes", since="2015-10-10", until="2016-10-11", count=100).items(200):
	print(status._json)