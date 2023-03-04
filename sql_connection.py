import mysql.connector

conn = mysql.connector.connect(host='localhost',password='mqb237@007H',user='root')
if conn.is_connected():
    print("connection established")
cur=conn.cursor()
query='show databases'
cur.execute(query)
result=cur.fetchall()
print(result)


