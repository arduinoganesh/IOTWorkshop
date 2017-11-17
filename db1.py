import MySQLdb

db = MySQLdb.connect("localhost","root","root","college")
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print "Database Version: ",data
db.close()
