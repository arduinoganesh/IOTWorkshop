import httplib, urllib
import time, Adafruit_DHT
sleep = 60 # how many seconds to sleep between posts to the channel
key = '2VBZYQL13MR3WHJV'  # Thingspeak channel to update

#Report Raspberry Pi internal temperature to Thingspeak Channel
def thermometer():
    while True:
        h, t = Adafruit_DHT.read_retry(11,18);.
		print "Temp:", t
        params = urllib.urlencode({'field1': t, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")
        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print response.status, response.reason
            data = response.read()
            conn.close()
        except:
            print "connection failed"

thermometer()

