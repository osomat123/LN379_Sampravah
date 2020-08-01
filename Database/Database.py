import mysql.connector
from datetime import datetime

def InsertIntoTable(data,table):
    mydb=mysql.connector.connect(host='localhost',
                                 user='root',
                                 database='dam'
                                 )
    value = data

    cur=mydb.cursor()

    query = "INSERT INTO {} VALUES (NOW(),{})".format(table,value)
    cur.execute(query)
    mydb.commit()

def ExtractFromTable(table):

    mydb = mysql.connector.connect(host='localhost',
                                   user='root',
                                   database='dam'
                                   )
    cur = mydb.cursor()

    query = "SELECT * FROM {}  ORDER BY time DES".format(table)

    cur.execute(query)
    result = cur.fetchall()

    data = []
    timestamp = []
    return (result)


