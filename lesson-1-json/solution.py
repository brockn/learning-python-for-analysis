#!/usr/bin/env python

import requests
import json
from pprint import pprint

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

# program
parsed_json = json.loads(example_json)
print "Parsed JSON is type  " + str(type(parsed_json))
print "Parsed JSON has keys: " + str(parsed_json.keys())

name = parsed_json['name']
print "Name is type " + str(type(name))
print "Name: " + name

age = parsed_json['age']
print "Age is type " + str(type(age))
print "Age: " + str(age)

attributes = parsed_json['attributes']
print "Attributes are type " + str(type(attributes))
print "Attributes have keys: " + str(attributes.keys())
favorite_color = attributes['favorite_color']
print "Favorite Color is type " + str(type(favorite_color))
print "Favorite Color: " + favorite_color
print "Favorite Foods:"
favorite_foods = attributes['favorite_foods']
print "Favorite Foods are type " + str(type(favorite_foods))
for favorite_food in favorite_foods:
  print "  Favorite Food is type " + str(type(favorite_food))
  print "  " + favorite_food
