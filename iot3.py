#iot using post method
import httplib, urllib
import time, Adafruit_DHT
sleep(60)
key=""

def thermometer()
	while True:
		h,t = Adafruit_DHT.read_retry(11,4)
		print "Temp: ",t,"Humi:",h
		params = urllib.urlencode({'field1':h,'field2':t,'key':key})
		headers

