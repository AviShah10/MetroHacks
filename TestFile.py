from twitterscraper import query_tweets
import json
import csv

if __name__ == '__main__':
    with open("alabama.csv", 'wt', encoding="utf8") as output:
        writer = csv.writer(output)
        writer.writerows([tweet.user] for tweet in query_tweets("Abortion", 10))

# Or save the retrieved tweets to file: