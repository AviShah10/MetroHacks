import json
import csv
import tweepy
import re

print('hello')

if __name__ == '__main__':
    # def search_for_hashtags(consumer_key, consumer_secret, access_token, access_token_secret, hashtag_phrase):
    # create authentication for accessing Twitter
    ACCESS_TOKEN = '1132298551411630080-TxbsTVojtHBCpZC0pjgCbDYsx3XcwO'
    ACCESS_SECRET = 'MjksGvOspEXk7EF8HUVgmgHJpTIgAifI5SY8SWpLyqeaI'
    CONSUMER_KEY = '9Q7tOjRTcnk0GDgLGfMYESmFx'
    CONSUMER_SECRET = 'Oy98g2cuXlPkTs75akfeVvDq2YiPiMvzSP9e4Z2wOronPBaGDp'
    hashtag_phrase = input('Hashtag Phrase ')

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    # initialize Tweepy API
    api = tweepy.API(auth)

    # get the name of the spreadsheet we will write to
    # fname = '_'.join(re.findall(r'#(\w+)', hashtag_phrase))

    # open the spreadsheet we will write to
    with open("alabama.csv", 'wt', encoding="utf8") as output:
        w = csv.writer(output)

        # write header row to spreadsheet
        w.writerow(['timestamp', 'tweet_text', 'username', 'all_hashtags', 'followers_count'])

        # for each tweet matching our hashtags, write relevant info to the spreadsheet
        for tweet in tweepy.Cursor(api.search, q=hashtag_phrase + ' -filter:retweets',
                                   lang="en", tweet_mode='extended').items(10):
            w.writerow([tweet.created_at, tweet.full_text.replace('\n', ' ').encode('utf-8'),
                        tweet.user.screen_name.encode('utf-8'),
                        [e['text'] for e in tweet._json['entities']['hashtags']], tweet.user.followers_count])
