import mysql.connector
mydb = mysql.connector.connect(
  host="aws-stocks.clwj5kkqkr3e.us-east-2.rds.amazonaws.com",
  user="admin",
  password="Csmri2021!",
  database='US_STOCK'
)

mycursor = mydb.cursor()
test_str = '2021-01-21T16:24:35.842324502-05:00'
from datetime import datetime
test_str = test_str.split('.')[0]
timestamp = datetime.strptime(test_str,"%Y-%m-%dT%H:%M:%S")
print(timestamp)
print(type(timestamp))
sql = "INSERT INTO test_table (update_message_type, update_time) VALUES (%s, %s)"
val = ("dv", timestamp)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

print(mydb) 