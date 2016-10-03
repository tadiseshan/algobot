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

def process(headline):
	sep = ' - '
	rest = headline.split(sep, 1)[0]
	sep2 = ' ...'
	rest2 = rest.split(sep2, 1)[0]
	return rest2

def add_id_to_file(tweet):
	with open('already_tweeted.txt', 'a') as file:
		file.write(str(tweet) + "\n")

def duplicate_check(tweet):
	found = 0
	with open('already_tweeted.txt', 'r') as file:
		for line in file:
			if tweet in line:
				found = 1
	return found

def tweet(headline):
	auth = tweepy.OAuthHandler(C_KEY, C_SECRET)
	auth.set_access_token(A_TOKEN, A_TOKEN_SECRET)
	api = tweepy.API(auth)

	tweet = process(random.choice(headline))
	
	if duplicate_check(tweet) == 0:
		add_id_to_file(tweet)
		api.update_status(tweet)
	else: print('tweet already tweeted')

if __name__ == "__main__":
    get()