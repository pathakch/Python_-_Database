import sqlite3

record = (123,'bob',34444)
records = [(1400,'Max',150000),(14001,'Jennier',250000)] 
try:
    conn=sqlite3.connect("new_db.db")
    cur=conn.cursor()
    #cur.execute("create table table_new(rollno integer,name text,feesn real)"

    cur.execute("insert into table_new values(1,'anil',43000)")
    conn.commit()
    conn.close()

except Exception as err:
    print(err)
