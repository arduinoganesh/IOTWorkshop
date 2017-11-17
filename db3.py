import MySQLdb

db = MySQLdb.connect("localhost","root","root","college")
cursor = db.cursor()
name = raw_input("enter name") #for string
roll = input("enter roll")
marks = input("enter marks")

sql="INSERT INTO student VALUES (%d, '%s',%f)"%(roll,name,marks)
try:
        cursor.execute(sql)
	db.commit()
except:
        print "Error:"
	db.rollback()

db.close()

