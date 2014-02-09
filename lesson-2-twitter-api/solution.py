#!/usr/bin/env python

import requests
import json
from pprint import pprint

fake_twitter_url = "http://people.apache.org/~brock/twitter-data.json"

# program
raw_tweets = requests.get(fake_twitter_url).text
# the object returned from type() is not a string so we use str() to make it a string
print "type(raw_tweets) " + str(type(raw_tweets))
parsed_tweets = json.loads(raw_tweets)
print "type(parsed_tweets) " + str(type(parsed_tweets))
pprint(parsed_tweets)
