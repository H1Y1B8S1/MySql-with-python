from mysql.connector import connect

#Creat the connection object
myconn = connect(host='localhost',user='root',passwd="")

#Creating the cursure object
cur = myconn.cursor()
try:
    #creating a new database
    cur.execute("create database college1") 
    print('database created')


except Exception as e:
    # myconn.rollback()
    print("can not proces\nMay be database name already existed")
    print(e)

# # getting the list of all the database
# dbs = cur.execute('show database')
# print(dbs)

myconn.close()
