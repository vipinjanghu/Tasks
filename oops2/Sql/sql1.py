import mysql.connector as conn

mydb=conn.connect(host="localhost",user="root",passwd="9971372013")

curser=mydb.cursor()
s=curser.execute("create database if not exists ineuron;"
               "use ineuron; create table if not exists vipin2(id int(4) NOT NULL,First_name varchar(10),Last_name varchar(10);"
               "select *from vipin2;show datasets;")
print()

#curser.execute("CREATE DATABASE if not exists INEURON")
#curser.execute("use ineuron")
#curser.execute("CREATE TABLE IF NOT EXISTS VIPIN1(id int(4) NOT NULL,First_name varchar(10),Last_name varchar(10))")
#curser.execute("select * from vipin1")
