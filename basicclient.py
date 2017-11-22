import socket
s=socket.socket()
port = 1234
s.connect(("172.16.14.36",port))

s.send("iot workshop, sitrc")

print "Received: ",s.recv(1024)
s.close()
