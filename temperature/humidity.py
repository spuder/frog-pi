#!/usr/bin/python

import sys
import os
import Adafruit_DHT
#import xively
from phant import Phant
from numerous import Numerous


phant_id = os.environ["PHANT_ID"]
phant_key = os.environ["PHANT_KEY"]
p = Phant(phant_id, 'humidity', 'tempc', 'tempf', private_key=phant_key)

# Numerous variables, sourced from external script
n_key = os.environ["NUMEROUS_KEY"]
n_humidity1 = os.environ["NUMEROUS_HUMIDITY1"]
n_temp_f1 = os.environ["NUMEROUS_TEMP_F1"]

mynumerous = Numerous(apiKey=n_key)
h1 = mynumerous.metric(n_humidity1)
tf1 = mynumerous.metric(n_temp_f1)

# Parse command line parameters.
sensor_args = { '11': Adafruit_DHT.DHT11,
				'22': Adafruit_DHT.DHT22,
				'2302': Adafruit_DHT.AM2302 }
if len(sys.argv) == 3 and sys.argv[1] in sensor_args:
	sensor = sensor_args[sys.argv[1]]
	pin = sys.argv[2]
else:
	print 'usage: sudo ./Adafruit_DHT.py [11|22|2302] GPIOpin#'
	print 'example: sudo ./Adafruit_DHT.py 2302 4 - Read from an AM2302 connected to GPIO #4'
	sys.exit(1)

# Try to grab a sensor reading.  Use the read_retry method which will retry up
# to 15 times to get a sensor reading (waiting 2 seconds between each retry).
humidity, tempc = Adafruit_DHT.read_retry(sensor, pin)

tempf = tempc * 9/5.0 + 32

# Note that sometimes you won't get a reading and
# the results will be null (because Linux can't
# guarantee the timing of calls to read the sensor).
# If this happens try again!
if humidity is not None and tempc is not None:
	print 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(tempc, humidity)
	p.log(humidity, tempc, tempf)
	current_humidity_1 = h1.read()
	current_temperature_f_1 = tf1.read()
	if ( current_humidity_1 != humidity ):
		h1.write(humidity)
	if ( current_temperature_f_1 != tempf ):
		tf1.write(tempf)
	# humidity_datastream.update(fields=[humidity])
else:
	print 'Failed to get reading. Try again!'
	sys.exit(1)
