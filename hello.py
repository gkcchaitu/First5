import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root", passwd="chaitu",database="studdent")
mycursor=mydb.cursor()
mycursor.execute("select * from studinfo")
for i in mycursor:
    print(i)