import mysql.connector
def createtable():
    mydb=mysql.connector.connect(host='localhost',
                                 user='root',
                                 database='dam'
                                 )

    cur=mydb.cursor()
    sensorData = "create table SensorData (Time timestamp primary key, Data float)"
    people = "create table People (Time timestamp primary key , Data int)"
    remTime = "create table RemTime (Time timestamp primary key , Rem varchar(30))"
    inflow = "create table Inflow (Time timestamp primary key , Data float)"
    inflowSlope = "create table InflowSlope (Time timestamp primary key , Data float)"

    cur.execute(sensorData)
    cur.execute(people)
    cur.execute(remTime)
    cur.execute(inflow)
    cur.execute(inflowSlope)
    mydb.commit()


