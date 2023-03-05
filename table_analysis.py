import mysql.connector

conn=mysql.connector.connect(host='localhost',password='mqb237@007H',user='root',database='mydb')
if conn.is_connected():
    print("connection established")

cur=conn.cursor()

query_1 = """create table employee
        (id integer,
         name varchar(20),
         salary double)
        """
query_2 = """
          insert into employee
        (id,name,salary) 
values
(1,'Alex',1000),
(2,'Bob',2000),
(3,'Alex',3000),
(4,'John',4000),
(5,'Remi',5000),
(6,'August',6000),
(7,'Neil',7000),
(8,'Boyz',8000)

          """
cur.execute(query_1)
cur.execute(query_2)

conn.commit()
conn.close()











