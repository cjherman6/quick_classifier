import os
import tweepy
from textblob import TextBlob

#Login info
consumer_key = os.environ['TWITTER_API_KEY']
consumer_secret = os.environ['TWITTER_API_SECRET_KEY']
access_token = os.environ['TWITTER_ACCESS_TOKEN']
access_token_secret = os.environ['TWITTER_ACCESS_TOKEN_SECRET']

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('climate')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)


# wiki = TextBlob("I like to eat sushi on Wednesday")
# tags = wiki.tags
# words = wiki.words
# sentiment = wiki.sentiment.polarity
# print(words,sentiment)
#
# wiki = TextBlob("I hate hate hate it so much it's the worst")
# words = wiki.words
# sentiment = wiki.sentiment.polarity
# print(words,sentiment)
#
# wiki = TextBlob("I love love love it I'm so happy all the time it's the greatest!")
# words = wiki.words
# sentiment = wiki.sentiment.polarity
# print(words,sentiment)
