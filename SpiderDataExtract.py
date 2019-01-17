import os
try:
	os.system("pip install -r requirements.txt")
	os.system("cls")
except: pass

import tweepy
import csv
Access_token = "574351903-SirnPuk7fIlK3jv291U0rEHKkiXuOchA6RjgI4YK"
Access_secret = "xN1dnpz6SvKd3hIUy0MlR09rAIkLqbl7QiQhH09xxE9sI"
consumer_token = "xydSNCHSXfxQy9OjrkMxOl2NL"
consumer_secret = "SQJirubS0PZl49zMbWnQgqHbyuRUIi3L9oWFWB8ncl05RoxcrF"
auth = tweepy.OAuthHandler(consumer_token, consumer_secret)


auth.set_access_token(Access_token,Access_secret)
api=tweepy.API(auth,wait_on_rate_limit=True)

csvFile=open('spiderman.csv','a')
csvWriter = csv.writer(csvFile)
try:
	for tweet in tweepy.Cursor(api.search,q="Spider man: far from home", count=100,lang="en",since="2018-01-01").items():
		print(tweet.text)
		csvWriter.writerow([tweet.text.encode('utf-8')])
	
except: pass
os.system ("pip freeze > requirements.txt")
