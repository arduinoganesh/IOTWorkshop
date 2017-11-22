import RPi.GPIO as GPIO
import time

irled = 18
buzzer = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(irled,GPIO.IN)
GPIO.setup(buzzer,GPIO.OUT)
try:
	while True:
		i=GPIO.input(irled)    # reading IR Sensor
		if i==1:
			print('Obstacke Detected!!')
			GPIO.output(buzzer,GPIO.HIGH);
			time.sleep(1)
		elif i==0:
			print('No one Here')
			GPIO.output(buzzer,GPIO.LOW);
      time.sleep(1)
except	KeyboardInterrupt:
	GPIO.cleanup()
