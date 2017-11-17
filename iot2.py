import RPi.GPIO as GPIO
from time import sleep  
import Adafruit_DHT as dht
import urllib2

def getSensorData():
	RH, T = dht.read_retry(dht.DHT11, 4)
	return (str(RH), str(T))

baseURL = 'https://api.thingspeak.com/update?api_key=6P7F8NL1E4ZTXF1L'

while True:
	try:
		RH, T = getSensorData()
		f = urllib2.urlopen(baseURL +"&field1=%s&field2=%s" % (str(RH), str(T)))
		print f.read()
		f.close()
		sleep(12)
	except:
		print 'exiting.'
		break
