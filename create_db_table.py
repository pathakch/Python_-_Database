import sqlite3
record = (123,'bob',34444)
records = [(1400,'Max',150000),(14001,'Jennier',250000)]              # Creating list of tuple to insert multiple records in database.
try:
    # conn = sqlite3.connect("employeesystem.db")
    # cur = conn.cursor()
    conn=sqlite3.connect("seond_databases.db")
    cur=conn.cursor()
    cur.execute("create table table_1(rollno integer,name text,feesn real)")
    cur.execute("insert into table_1 values(1,'anil',43000)")
    # cur.execute("create table myemployee (empid integer, name text, salary real)")
    # cur.execute("show Database")
    # cur.execute("insert into myemployee values(123,'Anil',5000.78)")
    # cur.execute("insert into employee values(?,?,?)",record)               # Note : This is the better method to insert values (create tuple and pass that tuple.) to ignore the sql injection.
    # cur.executemany("insert into employee values(?,?,?)", records)        # Note : to pass multiple records use .executemany
    conn.commit()
    # cur.execute("select * from myemployee")
    # print(cur.fetchone())
    # print(cur.fetchmany(3))
    # print(cur.fetchall())
    # for rec in cur.execute("select * from employee where empid='123' and name like 'J%' and salary >100000 "):
    #   print(rec)
    # cur.execute("update employee set empid=456,salary=300000,name='Alex'")
    # conn.commit()
    # cur.execute()
    conn.close()
# except Exception as err:
#     print(err)
# New_Example :
# try:
#     conn=sqlite3.connect("newstudent.db")
#     cur=conn.cursor()
    # cur.execute("create table student_1 (rollno integer,name text,percentge real)")
    # cur.execute("insert into student_1 values (2,'Joy',56)")
    # cur.execute("update student_1 set rollno =4,name='Max',percentge=45")
    # cur.execute("Delete from student_1 where rollno = 4 ")
    # records=[(1,'Jenny',87),(3,'Ronny',89),(5,'Simpson',86)]
    # cur.executemany("insert into student_1 values (?,?,?)",records)
    # conn.commit()

    # rec =cur.execute("select * from student_1")
    # print(rec)



    # cur.execute("select * from student_1")                      # fetchall,fetchmany,and fetchone will work only when we will select * rom table first then write fetch command.
    # print(cur.fetchone())
    # print(cur.fetchmany(3))
    # print(cur.fetchall())
    # conn.close()                                                # Here


    # for rec in cur.execute("select * from student_1"):
         # print(rec)
         # conn.close()                     # comment this part/take outside the loop when fetchig the records within the lopps:Otherwise connection will be closed and will not fetch any records.



    # cur.rowcount
    # cur.next()
    # help(cur.rowcount)
    # cur.execute("delete from student_1 where name='Joy' ")
    # cur.execute("truncate table student_1")
    # conn.commit()
    # conn.close()
except Exception as err:
    print(err)
