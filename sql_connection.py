import mysql.connector

"""This file is for pycharm testing. 
   This code has been tested that its working in pycharm or not
   This mySQL server is localhost server means it's running on this same
   laptop in mySQL database and found to be working
"""

conn = mysql.connector.connect(host='localhost',password='mqb237@007H',user='root')
if conn.is_connected():
    print("connection established")
cur=conn.cursor()
query='show databases'
cur.execute(query)
result=cur.fetchall()
print(result)

conn.close()
cur.close()
del cur




