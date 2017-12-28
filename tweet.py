import tweepy
import csv
from textblob import TextBlob

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #authentication
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth) 

public_tweets = api.search('UST Paskuhan')

download_dir = "example.csv"
csv = open(download_dir, "w")
columnTitleRow = "tweet, analysis\n"
csv.write(columnTitleRow)

for tweet in public_tweets:
	analysis = TextBlob(tweet.text)
	if analysis.sentiment.polarity == 0.0:
		result = "negative"
	else:
		result = "positive"
	row = tweet.text + "," + result + "\n"
	csv.write(row)
