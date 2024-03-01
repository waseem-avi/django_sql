import mysql.connector
db = mysql.connector.connect(
    host     = "localhost",
    user     = "root",
    password = "root

)
cursorObject = db.cursor()
cursorObject.execute("CREATE DATABASE Student_records")