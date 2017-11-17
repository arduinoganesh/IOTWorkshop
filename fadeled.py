import RPi.GPIO as gpio
import time
gpio.setmode(gpio.BCM)
gpio.setup(17,gpio.OUT)
p=gpio.PWM(17,50)
p.start(0)
try:
	while True:
		for i in range (100):
			p.ChangeDutyCycle(i)
			time.sleep(0.02)
		for i in range (100):
                        p.ChangeDutyCycle(100-i)
                        time.sleep(0.02)
except KeyboardInterrupt:
	pass
	p.stop()
	gpio.cleanup()

