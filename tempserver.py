import socket
import Adafruit_DHT as dht

s=socket.socket()
s.bind(("172.16.14.36",1234))
s.listen(5)

try:
	while True:
        	print "Waiting for Client Connection"
	        c,addr = s.accept()
	        print "Got Connection From ", addr
	        #data = c.recv(10)
#		if data.cmp("TempHum"):
		hum,temp = dht.read_retry(11,4)
		sql="Temp = %.2f Humidity %.2f "%(temp,hum)
		print "Data Send... "
		c.send(sql)
#		else:
#	        c.send("Service Not Available!!")
        	c.close()
except KeyboardInterrupt:
	s.close()

