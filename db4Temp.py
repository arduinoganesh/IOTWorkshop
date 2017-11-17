import MySQLdb
import Adafruit_DHT as dht
import time

db = MySQLdb.connect("localhost","root","root","college")
cursor = db.cursor()


while True:
	try:
		hum,temp = dht.read_retry(11,4)
		print "Temp: ",temp,"Hum: ",hum
		db = MySQLdb.connect("localhost","root","root","college")
		cursor = db.cursor()
		sql="INSERT INTO datalogger VALUES (%d, %d)"%(temp,hum)
		cursor.execute(sql)
	        db.commit()
		time.sleep(5)
	except KeyboardInterrupt as e:
        	db.rollback()
		try:
			db = MySQLdb.connect("localhost","root","root","college")
			cursor = db.cursor()
			cursor.execute("select avg(temp) from datalogger")
			data = cursor.fetchone()
			print "Average Temperature: %.3f "%data
		except:
			pass
			db.close()
	db.close()

