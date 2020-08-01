import mysql.connector
def createtable():
    mydb=mysql.connector.connect(host='localhost',
                                 user='root',
                                 database='dam'
                                 )

    cur=mydb.cursor()
    s="create table SensorData (Time timestamp primary key, Data float)"
    a="create table People (Time timestamp primary key , Data int)"
    b="create table RemTime (Time timestamp primary key , Rem varchar(30))"

    cur.execute(s)
    cur.execute(a)
    cur.execute(b)
    mydb.commit()


