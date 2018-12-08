import mysql.connector
import subprocess

mysql_args = ['net', 'start', 'mysql57']

def connect():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12345678",
        database="btl"
    )
    return mydb

def restart_mysql():
    mysql_args[1] = 'start'
    subprocess.run(mysql_args)
    mysql_args[1] = 'stop'
    subprocess.run(mysql_args)
    mysql_args[1] = 'start'
    subprocess.run(mysql_args)

def mysqlConnect(sql, num):
    # restart_mysql()
    mydb = connect()
    mycursor = mydb.cursor()
    mycursor.execute("SET PROFILING = 1")
    mycursor.execute(sql)
    if num == 0:
        myresult = mycursor.fetchall()
    mycursor.execute("SHOW PROFILES")
    myresult = mycursor.fetchall()[-1]
    mycursor.execute("SET PROFILING = 0")
    mydb.commit()
    return myresult;