import tweepy 
from secrets import *
import random
import json
import requests 
import sys
import time
import feedparser

def get():
	query = "algorithm"

	def parseRSS(rss_url):
		return(feedparser.parse(rss_url))

	def getHeadlines(rss_url):
		headlines = []
		feed = parseRSS(rss_url)
		for item in feed['items']:
			headlines.append(item['title'])
		return(headlines)

	tweet(getHeadlines('https://news.google.com/news?cf=all&hl=en&pz=1&ned=us&q=algorithm&output=rss'))

def tweet(headline):
	auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
	auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
	api = tweepy.API(auth)

	tweet = random.choice(headline)

	api.update_status(tweet)

if __name__ == "__main__":
    get()