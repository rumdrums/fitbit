#!/usr/bin/python

import fitbit
import webbrowser
import os
import datetime
from requests_oauthlib import OAuth1


# initialize: 
""" 	fitbit.Fitbit.__init__(
		self, 
		consumer_key, 
		consumer_secret, 
		resource_owner_key=resource_owner_key, 
		resource_owner_secret=resource_owner_secret
	)
"""

# getting a time series:
# 	a.time_series(resource='body/weight',base_date='2015-01-01',end_date='2015-05-01')

# logging activity:
""" activity: { 	'date': datetime.datetime.today().strftime('%Y-%m-%d',
				'activityName': 'Jogging',
                'startTime': '18:00',
				'durationMillis': 30*60000,
                'manualCalories':, 250,
                'distance': 1.75,
                'distanceUnit': 'Mile'
			}

		Jfitbit.log_activity(self, activity)	
"""

class Jfitbit(fitbit.Fitbit):
	def __init__(self, consumer_key, consumer_secret, resource_owner_key, resource_owner_secret):
		# call init of parent class:
		fitbit.Fitbit.__init__(
			self, 
			consumer_key, 
			consumer_secret, 
			resource_owner_key=resource_owner_key, 
			resource_owner_secret=resource_owner_secret)

	def log_weight(self, weight, date=datetime.datetime.now().strftime('%Y-%m-%d')):
		# https://wiki.fitbit.com/display/API/API-Log-Body-Weight
		# weight = x.xx
		# date = yyyy-MM-dd
		
		data = {
		    'weight': weight,
		    'date': date,
		}
		url = "%s/%s/user/-/body/log/weight.json" % (
		    self.API_ENDPOINT,
		    self.API_VERSION,
		)
		self.make_request(url, data=data, method="POST")
	def get_activities(self, date='2012-01-01'):
		url = "%s/%s/user/-/activities/list.json" % (
			self.API_ENDPOINT,
			self.API_VERSION,
		)
		params = {
			'afterDate': date,
			'offset': 10,
			'limit': 100,
			'sort': 'desc',
		}
		stuff = self.make_request(url, method="GET", params=params)
		print(stuff)
	
class Jfitbit_cli(Jfitbit):
	""" This class instantiates the FitbitOauthClient class, gets the application's authorization token from that,
	directs customer to go to the website with that token, get verifier token, and instantiate Fitbit class,
	which allows pulling/modifying of customer data -- the app's key/secret are stored in class so I have don't have to load it each time
	"""
	def __init__(self, consumer_key, consumer_secret):
		auth = fitbit.FitbitOauthClient(consumer_key, consumer_secret)
		# This creates initial request token; data is used to generate URL 
		# (URL appears to just take request_token['oauth_token'] and append it to URL):
		request_token = auth.fetch_request_token()
		# Launch web browser to get the authorization token then enter it in:
		website = auth.authorize_token_url()
		#stderr = os.dup(2)
		#os.open(os.devnull, os.O_RDWR)
		#webbrowser.open(website)
		#os.dup2(stderr, 2)
		verifier = raw_input("\n\tGo to:\n\t\t %s \n\n\tand enter the key you find there:\n" % website)
		access_token = auth.fetch_access_token(verifier)
		# Take variables from 'token' and create authenticated session:
		self.resource_owner_key = access_token['oauth_token']
		self.resource_owner_secret = access_token['oauth_token_secret']
		self.consumer_key = consumer_key
		self.consumer_secret = consumer_secret
		# call init of parent class:
		fitbit.Fitbit.__init__(
			self, 
			self.consumer_key, 
			self.consumer_secret, 
			resource_owner_key=self.resource_owner_key, 
			resource_owner_secret=self.resource_owner_secret
		)

def unauth():
	#Setup an unauthorised client (e.g. with no user)
	unauthd_session = fitbit.Fitbit(consumer_key, consumer_secret)
	return unauthd_session
