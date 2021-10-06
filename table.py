import MySQLdb as connector     #pip install MySQLdb

inp1 = input("Enter The Name of the host :")
inp2 = input("Enter The Name of the user :")
inp3 = input("Enter The Name of the Database :")
inp4 = input("Enter The Password :")

# Connection in my system
# conn = connector.connect(host='localhost',user='root',passwd='skype123',db='SCHOOL')

# Connecting Databse
conn = connector.connect(host=inp1,user=inp2,passwd=inp4,db=inp3)
cur = conn.cursor()

# Creation of User table
query1 = "create table user(username varchar(50),password varchar(50),name char(30),age int);"
cur.execute(query1)
conn.commit()
print("User table Created!!")

# Creation of student Table 
query2 = "create table student(name char(40),age int,admn int primary key,mother_name char(40),father_name char(40),gender varchar(1),year_of_admission int);"
cur.execute(query2)
conn.commit()
print("Student Table created!!")

# Creation of Staff Table
query3 = "create table staff(name char(40),ID_no int primary key,age int,role varchar(15),year_of_joining int);"
cur.execute(query3)
conn.commit()
print("Staff Table created!!")