import mysql.connector
from datetime import datetime

def InsertIntoTable(data,table):
    mydb=mysql.connector.connect(host='localhost',
                                 user='root',
                                 password='steelchair111',
                                 database='dam'
                                 )
    value = data

    cur=mydb.cursor()

    if table == 'SensorData' or table == 'People':
        query = "INSERT INTO {} VALUES (NOW(),{})".format(table,value)

    else:
        value = "'"+value+"'"
        query = "INSERT INTO {} VALUES (NOW(),{})".format(table, value)

    cur.execute(query)
    mydb.commit()

def ExtractFromTable(table):

    mydb = mysql.connector.connect(host='localhost',
                                   user='root',
                                   password='steelchair111',
                                   database='dam'
                                   )
    cur = mydb.cursor()

    query = "SELECT * FROM (SELECT * FROM {} ORDER BY time DESC LIMIT 50) sub ORDER BY time ASC".format(table)

    cur.execute(query)
    result = cur.fetchall()

    data = []
    timestamp = []

    for r in result:
        timestamp.append(r[0])
        data.append(r[1])

    return (data,timestamp) 
