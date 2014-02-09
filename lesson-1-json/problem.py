#!/usr/bin/env python

import requests
import json
from pprint import pprint

print "######################################################"
print "######################################################"
print "#################### Example #########################"
print "######################################################"
print "######################################################"
# example code - this shows you the tools you will need,
# but with sample data, not the actual json you will use below
# NOTE: sometimes for the "type" of a string python will
#  print <type 'unicode'> and other types <type 'str'>
#  do not worry about this for now. They are the same for
#  our purposes

example_dict = {
  "key1": "string value 1",
  "key2": 16,
  "key3": {
    "sub_key1": "string value 2",
    "sub_key2": [1, 2, 3, 4]
  }
}

# accessing key1 in the dictionary example_dict
print "Type of key1: " + str(type(example_dict['key1']))
print "Key1: " + example_dict['key1']

print "Type of key2: " + str(type(example_dict['key2']))
# The value associated with key2 is an int, so we must wrap
# the value in int in order to print the value
print "Key2: " + str(example_dict['key2'])

print "Type of key3: " + str(type(example_dict['key3']))
# The value associated with key3 is a dictionary so to access
# a dictionaries contents we must use the keys
print "Key3, keys: " + str(example_dict['key3'].keys())

print "Key3, Sub Key1 Type: " + str(type(example_dict['key3']['sub_key1']))
print "Key3, Sub Key1: " + example_dict['key3']['sub_key1']

print "Key3, Sub Key2 Type: " + str(type(example_dict['key3']['sub_key2']))
# sub_key2 is a list of integers, we must use a for loop
for item in example_dict['key3']['sub_key2']:
  print "Item Type: " + str(type(item))
  print "Item: " + str(item)

# Below is the start of the problem
print "######################################################"
print "######################################################"
print "#################### Problem #########################"
print "######################################################"
print "######################################################"
# triple double quotes below allow multi-line strings (python only)
example_json = """
{
  "name": "Brock Noland",
  "age": 25,
  "attributes": {
    "favorite_color": "blue",
    "favorite_foods": [
      "wings",
      "ribs",
      "pizza",
      "naan"
    ]
  }
}
"""

# program requirements:
# Similar to above we should traverse the sample json printing each value and
# the values type. If a value is a dictionary print it's keys

parsed_json = json.loads(example_json)
print "Parsed JSON is type  " + str(type(parsed_json))
print "Parsed JSON has keys: " + str(parsed_json.keys())
# you should write code here
