import socket
s=socket.socket()
s.bind(("localhost",1234))
s.listen(5)

try:
	while True:
		print "Waiting for Client Connection"
		c,addr = s.accept()
		print "Got Connection From ", addr
		data = c.recv(10)
		c.send(data.upper())
except:
	c.close()

