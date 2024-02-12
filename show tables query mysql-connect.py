import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="manager",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("select * from customers")
