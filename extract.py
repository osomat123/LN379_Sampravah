def extract_from_SensorData():
    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',
                                 user='root',
                                 password='mysql',
                                 database='dam'
                                 )

    cur=mydb.cursor()
    #s="create table SensorData(TIME timestamp primary key, DATA float)"
    #a="create table People(TIME timestamp primary key, DATA int)"

    #cur.execute(s)
    #cur.execute(a)
    #mydb.commit()


    #extracting data from tables
    s = "select * from SensorData"
    #a="select * from People"
    cur.execute(s)
    #cur.execute(a)
    result=cur.fetchall()
    for rec in result:
        print(rec)
        mydb.commit()
        return result
        