import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
i = int(input('Enter Number of times blink: '))
for n in range(i):
	print('LED ON')
	GPIO.output(11,GPIO.HIGH)
	GPIO.output(12,GPIO.LOW)
	time.sleep(1)
	print('LED OFF')
	GPIO.output(11,GPIO.LOW)
	GPIO.output(12,GPIO.HIGH)
	time.sleep(1)
GPIO.cleanup()
