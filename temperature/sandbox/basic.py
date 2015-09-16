#!/usr/bin/python
# A test script to use xively.com for uploading data

import sys
import os
import Adafruit_DHT

import xively


FEED_ID = os.environ["FEED_ID"]
API_KEY = os.environ["API_KEY"]

api = xively.XivelyAPIClient(API_KEY)
feed = api.feeds.get("Frog Tank")
humidity_datastream = feed.datastreams.create("Humidity")
humidity_datastream = feed.datastreams.get('Humidity')

print "humidity is %s" % humidity_datastream
