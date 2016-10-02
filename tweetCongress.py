#Quick Python script to tweet at all the members of congress

import tweepy

tempNames = ''	#variable used to combine two names into one tweet
message = ''	#tweet message

consumer_key		="####"
consumer_secret		="####"
access_token		="####"
access_token_secret	="####"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

with open(congress_users) as myFile:
    for num, line in enumerate(myFile, 1):
	tempNames += '@' + line[:-1] + ' '
	if num % 2 == 0:
		print tempNames
		#api.update_status("tempNames" + message)
		tempNames = ''
