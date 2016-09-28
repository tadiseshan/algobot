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

	#query nyt api
	# nyt_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json?q=" + query + "&api-key=" + NYT_KEY
	# response = requests.get(nyt_url)
	# nyt_data = response.json()
	# nyt_docs = nyt_data["response"]["docs"]
	# headlines = []
	# for i in nyt_docs:
	# 	headlines.append(i['headline']['main'])

	# #query guardian api
	# g_url = "http://content.guardianapis.com/search?q=" + query + "&api-key=" + GUARDIAN_KEY
	# g_response = requests.get(g_url)
	# g_data = g_response.json()
	# g_docs = g_data["response"]["results"]
	# for j in g_docs:
	# 	headlines.append(j['webTitle'])

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