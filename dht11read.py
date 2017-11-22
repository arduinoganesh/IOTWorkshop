import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)

try:
	while True:
		hum, temp = dht.read_retry(11,4)
		print "Humidity = %f , Temperature = %f "%(hum,temp)
		
except KeyboardInterrupt:
	GPIO.cleanup()
