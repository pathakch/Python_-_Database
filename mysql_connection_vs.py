import mysql.connector

""" This file is for visual studio environment testing
    This code is working fine in visual studio code 
    This mySQL connection is for localhost means 
    this server is running on this same laptop in mySQL database
    And it's found to be working.
"""

conn = mysql.connector.connect(host='localhost',password='mqb237@007H',user='root')
if conn.is_connected():
    print("connection established")
cur=conn.cursor()    

query='show databases;'
cur.execute(query)
rslt=cur.fetchall()
print(rslt)