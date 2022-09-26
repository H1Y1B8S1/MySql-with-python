import mysql.connector

myconn = mysql.connector.connect(host = 'localhost',user='root',passwd='',database='college1')

cur = myconn.cursor()

try:
    data = cur.execute('create table CSE(sid int(2) primary key, name varchar(20) not null)')

    print('done')

except Exception as e:
    print('can not process')
    print(e)

myconn.close()