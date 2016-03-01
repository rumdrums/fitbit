#!/usr/bin/env python

import jfitbit
import ConfigParser

config = 'config.ini'
parser = ConfigParser.SafeConfigParser()
parser.read(config)
consumer_key = parser.get('Fitbit', 'KEY')
consumer_secret = parser.get('Fitbit', 'SECRET')

client = jfitbit.Jfitbit_cli(consumer_key, consumer_secret)
