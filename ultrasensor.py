import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

TRIG = 23 
ECHO = 24
BUZZER = 18
print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)
GPIO.setup(BUZZER,GPIO.OUT)

GPIO.output(TRIG, False)

def blinkled(duration):
	GPIO.output(BUZZER,GPIO.HIGH)
	time.sleep(duration*0.01)
	GPIO.output(BUZZER,GPIO.LOW)
	time.sleep(duration*0.01)

print "Waiting For Ultrasonic Sensor"
try:
	while True:
		time.sleep(0.1)
		GPIO.output(TRIG, True)
		time.sleep(0.00001)
		GPIO.output(TRIG, False)

		while GPIO.input(ECHO)==0:
			pulse_start = time.time()

		while GPIO.input(ECHO)==1:
			pulse_end = time.time()

		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17150
		distance = round(distance, 2)

		print "Distance:",distance,"cm"
		blinkled(distance)
		if distance <=3.0:
			print 'Too near'
		elif distance <=10.0:
			print 'SAFE'
		else:
			print 'Too Far'

except KeyboardInterrupt :
	GPIO.cleanup()
