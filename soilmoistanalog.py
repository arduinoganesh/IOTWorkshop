import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
a_pin =18
b_pin = 17

def discharge():
	GPIO.setup(a_pin,GPIO.IN)
	GPIO.setup(b_pin,GPIO.OUT)
	GPIO.output(b_pin,False)
	time.sleep(0.02)
def charge_time():
	GPIO.setup(a_pin,GPIO.OUT)
	GPIO.setup(b_pin,GPIO.IN)
	count =0
	GPIO.output(a_pin,True)
	while not GPIO.input(b_pin):
		count +=1
	return count

def analog_read():
	discharge()
	return charge_time()

try:
	while True:
		#i=GPIO.input(a_pin)
		# if i==0:
		print "Moisture intensity: ",analog_read()
		time.sleep(1.0)
		#elif i==1:
		#print "Dry ",analog_read()
		#time.sleep(0.1)
except KeyboardInterrupt:
	GPIO.cleanup()
	exit(0)	
