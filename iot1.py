import sys
import RPi.GPIO as GPIO
from time import sleep  
import Adafruit_DHT
import urllib2

def getSensorData():
    RH, T = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 23)
    # return dict
    return (str(RH), str(T))

# main() function
def main():
    # use sys.argv if needed
    print 'starting...'

    baseURL = 'https://api.thingspeak.com/update?api_key=SYWL6F0CIDY1C7SG'

    while True:
        try:
            RH, T = getSensorData()
            f = urllib2.urlopen(baseURL +
                                "&field1=%s&field2=%s" % (RH, T))
            print f.read()
            f.close()
            sleep(15)
        except:
            print 'exiting.'
            break

# call main
if __name__ == '__main__':
    main()
