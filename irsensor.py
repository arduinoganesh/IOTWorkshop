import RPi.GPIO as GPIO
import time

servo = 17
irled = 18

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(irled,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)
GPIO.setup(servo)
p=GPIO.PWM(22,50)
p.start(0)
try:
	while True:
		i=GPIO.input(irled)
		if i==1:
			print('Someone Coming')
			p.ChangeDutyCycle(12.5)
			time.sleep(1)
		elif i==0:
			print('No one Here')
			p.ChangeDutyCycle(0)
			time.sleep(1)
except	KeyboardInterrupt:
	GPIO.cleanup()
