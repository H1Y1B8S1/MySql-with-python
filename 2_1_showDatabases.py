from mysql.connector import connect

# getting details about all database in local host
myconn1 = connect(host='localhost',user='root',passwd="")
cur = myconn1.cursor()

cur.execute('show databases')
for dbs in cur:
    print(dbs)

print('\n\n')


myconn1.close()


# getting details about all tables in perticuler database
myconn2 = connect(host='localhost',user='root',passwd='',database='performance_schema')
cur = myconn2.cursor()

cur.execute('show tables')
for tables in cur:
    print(tables)

myconn2.close()
