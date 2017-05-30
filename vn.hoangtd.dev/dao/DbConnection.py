# import MySQL module
import MySQLdb

## config url, user, pass, dbName
host = "localhost"
username = "hoangtd"
password = "123456"
db = "demorest"

# connect
db = MySQLdb.connect(host, username, password,db)

# create a database cursor
cursor = db.cursor()

# execute SQL select statement
cursor.execute("SELECT * FROM userdto")

# get the number of rows in the resultset
numrows = int(cursor.rowcount)

# get and display one row at a time
for x in range(0,numrows):
    row = cursor.fetchone()
    print "ID: ",row[0], "Username: ", row[3]

# disconnect from serve
db.close()
