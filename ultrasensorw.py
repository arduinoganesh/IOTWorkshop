import RPi.GPIO as GPIO
import time, signal, sys
import urllib2

GPIO.setmode(GPIO.BCM)
pinTrigger = 23
pinEcho = 24
baseURL = 'https://api.thingspeak.com/update?api_key=SYWL6F0CIDY1C7SG' 
def close(signal,frame):
	print('Turning off ultrasonic Sensor')
	GPIO.cleanup()
	sys.exit(0)

signal.signal(signal.SIGINT,close)
GPIO.setup(pinTrigger,GPIO.OUT)
GPIO.setup(pinEcho,GPIO.IN)
GPIO.setup(18,GPIO.OUT)
while True:
	GPIO.output(pinTrigger,True)
	time.sleep(0.00001)
	GPIO.output(pinTrigger,False)
	
	startTime = time.time()
	stopTime = time.time()

	while 0==GPIO.input(pinEcho):
		startTime = time.time()
	while 1==GPIO.input(pinEcho):
		stopTime = time.time()
	
	TimeElapsed = stopTime - startTime
	distance = (TimeElapsed * 34300)/2
#	if distance <=50.0:
#		GPIO.output(18,GPIO.HIGH)
#		time.sleep(0.01*distance)
#		GPIO.output(18,GPIO.LOW)
#		time.sleep(0.01*distance)
#	else:
#		GPIO.output(18,GPIO.LOW)
#		time.sleep(0.1)
	print('Distance: %.1f cm'%distance)
	#time.sleep(2)
	f = urllib2.urlopen(baseURL + "&field1=%s&field2=%s" % (50,distance))
	print f.read()
	f.close()
	time.sleep(5)


