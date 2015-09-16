#!/usr/bin/python

# A test script to upload data to numerous

# https://github.com/outofmbufs/Nappy/issues/1
import sys
import os
from numerous import Numerous
#import numerous

n_key = os.environ["NUMEROUS_KEY"]
n_humidity1 = os.environ["NUMEROUS_HUMIDITY1"]
n_temp_f1 = os.environ["NUMEROUS_TEMP_F1"]

foo = Numerous(apiKey=n_key)
h1 = foo.metric(n_humidity1)
tf1 = foo.metric(n_temp_f1)

new_value = 81
current_value = h1.read()
print("h1.read()")
if ( new_value != current_value ):
    print(new_value)
    h1.write(new_value)
