#import library to give access to twitter
import tweepy
# import library to give a access to CSV
import csv
# import TextBlob library
from textblob import TextBlob

#details ... details..
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

#Create authorization
auth = tweepy.OAuthHandler(consumer_key, consumer_secret) #authentication
auth.set_access_token(access_token, access_token_secret)

#Use Twitter API
api = tweepy.API(auth) 

#gather tweets
public_tweets = api.search('UST Paskuhan')

#write on csv
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
