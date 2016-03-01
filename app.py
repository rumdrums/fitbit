import flask
from pymongo import MongoClient
import ConfigParser 
import jfitbit
from fitbit import FitbitOauthClient

config = 'config.ini'
parser = ConfigParser.SafeConfigParser()
parser.read(config)
consumer_key = parser.get('Fitbit', 'KEY')
consumer_secret = parser.get('Fitbit', 'SECRET')

client = jfitbit.Jfitbit_cli(consumer_key, consumer_secret)


MONGODB_HOST = parser.get('DB', 'HOST')
MONGODB_PORT = parser.get('DB', 'PORT')
DB_NAME = parser.get('DB', 'DB_NAME')
APP_PORT = parser.get('APP', 'APP_PORT')

connection = MongoClient(MONGODB_HOST, MONGODB_PORT)

@app.route("/verify", methods=['GET'])
def verify():
	if flask.request.method == 'GET':
		verifier = request.args.get('oauth_verifier')	
		print('verifier: %s' % verifier)
	"""
        access_token = auth.fetch_access_token(verifier)
        # Take variables from 'token' and create authenticated session:
        resource_owner_key = access_token['oauth_token']
        resource_owner_secret = access_token['oauth_token_secret']
	"""

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=APP_PORT,debug=True)

