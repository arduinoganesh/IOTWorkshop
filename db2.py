import MySQLdb

db = MySQLdb.connect("localhost","root","root","college")
cursor = db.cursor()
sql="select * from student"
try:
	cursor.execute(sql)
	results = cursor.fetchall()  # return list of tuples
	for row in results:
		roll = row[0]
		name = row[1]
		marks = row[2]
		print "%-3d%-10s%-5.3f"%(roll,name,marks)
except:
	print "Error: Unable to fetch data"

db.close()


