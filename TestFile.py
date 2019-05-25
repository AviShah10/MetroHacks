import tweepy
import sys
import os
import jsonpickle
from twitterscraper import query_tweets
import json
import csv

if __name__ == '__main__':
    list_of_tweets = query_tweets("Trump OR Clinton", 10)

    #print the retrieved tweets to the screen:
    for tweet in query_tweets("Trump OR Clinton", 10):
        print(tweet)

    #Or save the retrieved tweets to file:
    # file = open("output.txt","w")
    with open("alabama.csv", 'wt', encoding="utf8") as output:
        writer = csv.writer(output)
        writer.writerows([tweet.text] for tweet in query_tweets("Abortion", 10))
    # file.close()
