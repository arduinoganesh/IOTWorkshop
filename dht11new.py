import Adafruit_DHT as dht
import RPi.GPIO as GPIO
import time

dhtpin = 4
dhttype = 11
led = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(led,GPIO.OUT)
def blinkled():
	GPIO.output(led,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(led,GPIO.LOW)
	time.sleep(1)

try:
	while True:
		hum, temp = dht.read_retry(dhttype,dhtpin)
		print hum,temp
		if hum >= 60:
			print 'Humidity at Critical Level > 60', hum
			blinkled()
		else:
			print 'Humidity at Normal Level' , hum
			GPIO.output(led,GPIO.LOW)
except KeyboardInterrupt:
	GPIO.cleanup()

