import MySQLdb as connector     #pip install MySQLdb
from pandas import *            #pip install pandas
from datetime import datetime
from password_strength import PasswordPolicy,PasswordStats    #pip install password_strength
import time

# Password Policy
policy = PasswordPolicy.from_names(
    strength = 0.40
)

inp1 = input("Enter The Name of the host :")
inp2 = input("Enter The Name of the user :")
inp3 = input("Enter The Name of the Database :")
inp4 = input("Enter The Password :")

# Connection in my system
# conn = connector.connect(host='localhost',user='root',passwd='skype123',db='SCHOOL')

# Connecting Databse
conn = connector.connect(host=inp1,user=inp2,passwd=inp4,db=inp3)
cur = conn.cursor()

if conn:
    print("Database successfully connected")
else:
    print("Not Connected \nTerminating...")

print("\n****************School Management System****************")
print("1. Sign up\n2. Existing User\n3. Retrieve information\n4. Exit")

try:
    inp1 = int(input("Enter Your Choice :"))
except:
    print("INPUT SHOULD BE IN INTERGER!!")
    inp1 = int(input("Enter Your Choice :"))

if inp1 == 1:
    while True:
        b = False
        inp0 = int(input("SECRET CODE OF THE SCHOOL :"))
        if inp0 == 25235:
            pass
        else:
            print("SCHOOL CODE IS WRONG!!")
            break
        username = input("Enter a Username :")
        # Checking of the availaiblity of the username
        pd_username = []
        sql = "select * from user"
        cur.execute(sql)
        for row in cur.fetchall():
            pd_username.append(row[0])
        for i in pd_username:
            if username == i:
                print(f"{username} already exist as a username.\nTry with a different username.")
                b = True
        if b:
            break


        name = input("Enter The name :")
        age = int(input("Enter The age of the person :"))
        password = input("Enter a Strong Password :")
        stats = PasswordStats(password)
        if policy.test(password) == []:
            confirm_password = input("Confirm Your Password :")
            if password == confirm_password:
                query = f"insert into user values('{username}','{password}','{name}','{age}');"
                cur.execute(query)
                conn.commit()
                print("User Created...")
        else:
            print(f"Please Enter a Strong Password...\nYour Password Strength is {stats.strength()}")
            print("It should be more that 0.40")
        break

elif inp1 == 2:
    username = input("Enter Your Username :")
    pd_username = []
    sql = "select * from user"
    cur.execute(sql)
    for row in cur.fetchall():
        pd_username.append(row[0])
    if username not in pd_username:
        print("Username Not Registered Kindly Register it.")
        exit()
    password = input("Enter Your Password :")
    query = "select * from user where username='{}' and password='{}'".format(username,password)
    cur.execute(query)
    data = cur.fetchall()
    if any(data):
        print(f"Welcome {username}!!")
        while True:
            print("What Do you like to do?")
            print("1. Register a Student")
            print("2. Register a Staff")
            print("3. Exit")
            try:
                inp2 = int(input("Enter Your Choice :"))
            except:
                print("INPUT SHOULD BE IN INTERGER!!")
                inp2 = int(input("Enter Your Choice :"))

            if inp2 == 1:
                name = input("Name of the Student :")
                age = int(input("Age of the Student :"))
                #admn should not be same of two students since its a primary key in our Table.
                admn = int(input("Enter The admission number :"))
                mother_name = input("Student's Mother Name :")
                father_name = input("Student's Father Name :")
                gender = input("Enter Student's Gender (m or f) :")
                year_of_admission = datetime.now().year
                query = f"insert into student values('{name}','{age}','{admn}','{mother_name}','{father_name}','{gender}','{year_of_admission}');"
                cur.execute(query)
                conn.commit()
                print("Details Inserted!!")
            elif inp2 == 2:
                name = input("Name of the Staff :")
                #id_no should not be same of two Staffs since its a primary key in our Table.
                id_no = int(input("Enter The ID :"))
                age = int(input("Age of the Staff :"))
                role = input("Enter The Role (eg. Teacher) :")
                year_of_joining = datetime.now().year
                query = f"insert into staff values('{name}','{id_no}','{age}','{role}','{year_of_joining}')"
                cur.execute(query)
                conn.commit()
                print("Details Inserted!!")
            elif inp2 == 3:
                print("Terminating")
                exit()
            else:
                print("Wrong Choice")
            print("Do you want to continue?")
            inp10 = input("y or n :")
            if inp10 == ('y' or 'Y'):
                continue
            else:
                break
    else:
        print("Your password or Username is incorrect\nTry Again.")

elif inp1 == 3:
    username = input("Enter Your Username :")
    pd_username = []
    sql = "select * from user"
    cur.execute(sql)
    for row in cur.fetchall():
        pd_username.append(row[0])
    if username not in pd_username:
        print("Username Not Registered Kindly Register it.")
        exit()
    password = input("Enter Your Password :")
    query = "select * from user where username='{}' and password='{}'".format(username,password)
    cur.execute(query)
    data = cur.fetchall()
    if any(data):
        while True:
            print("1. Details of all Student")
            print("2. Details of all Staff")
            print("3. Details of particular Student")
            print("4. Details of particular Staff")
            print("5. Total Number Of Students.")
            print("6. Total Number of Staff")
            inp3 = int(input("Enter Your Choice :"))
            if inp3 == 1:
                name = []
                age = []
                admn = []
                mother = []
                father = []
                gender = []
                year = []
                main_dict = {}
                sql = "select * from student;"
                cur.execute(sql)
                for row in cur.fetchall():
                    name.append(row[0])
                    age.append(row[1])
                    admn.append(row[2])
                    mother.append(row[3])
                    father.append(row[4])
                    gender.append(row[5])
                    year.append(row[6])
                main_dict['Name'] = name
                main_dict['Age'] = age
                main_dict['ADMN'] = admn
                main_dict['Mother Name'] = mother
                main_dict['father Name'] = father
                main_dict['Gender'] = gender
                main_dict['Year of Admission'] = year
                df = DataFrame(main_dict)
                df.index = range(1,len(name) + 1)
                print("Do you want to create a csv file? (y or n)?")
                inp6 = input("Enter Your Choice :")
                if inp6 == ('y' or 'Y'):
                    inp100 = input("Enter The Name of the csv file including .csv :")
                    df.to_csv(f'{inp100}',index=False)
                    print(df)
                    print(f"CSV file Created!!\nName = {inp100}")
                else:
                    print(df)
                                
            elif inp3 == 2:
                name = []
                id_no = []
                age = []
                role = []
                year = []
                main_dict = {}
                sql = "select * from staff;"
                cur.execute(sql)
                for row in cur.fetchall():
                    name.append(row[0])
                    id_no.append(row[1])
                    age.append(row[2])
                    role.append(row[4])
                    year.append(row[5])
                main_dict['Name'] = name
                main_dict['ID Number'] = id_no
                main_dict['Age'] = age
                main_dict['Role'] = role
                main_dict['Year_of_Joining'] = year
                df = DataFrame(main_dict)
                df.index = range(1,len(name) + 1)
                print("Do you want to create a csv file? (y or n)?")
                inp6 = input("Enter Your Choice :")
                if inp6 == ('y' or 'Y'):
                    inp100 = input("Enter The Name of the csv file including .csv :")
                    df.to_csv(f'{inp100}',index=False)
                    print(df)
                    print(f"CSV file Created!!\nName = {inp100}")
                else:
                    print(df)
            elif inp3 == 3:
                inp4 = int(input("Enter The Admission number of the student :"))
                query = f"select * from student where admn = {inp4};"
                cur.execute(query)
                list1 = ['Name','Age','Admn.','Mother','Father','GEN','YOA']
                print()
                for row in cur.fetchall():
                    for i in list1:
                        print(i,row[list1.index(i)],sep=" - ")
                print()
            elif inp3 == 4:
                inp4 = int(input("Enter The ID Number of the Staff :"))
                query = f"select * from staff where ID_no = {inp4};"
                cur.execute(query)
                list1 = ['Name','ID Number','Age','Role','YOJ']
                print()
                for row in cur.fetchall():
                    for i in list1:
                        print(i,row[list1.index(i)],sep=" - ")
                print()
            elif inp3 == 5:
                query = "select * from student;"
                cur.execute(query)
                list1 = []
                for row in cur.fetchall():
                    list1.append(row[0])
                print("Total Number Of Student in our School =",len(list1))
            elif inp3 == 6:
                query = "select * from staff;"
                cur.execute(query)
                list1 = []
                for row in cur.fetchall():
                    list1.append(row[0])
                print("Total Number Of Staff in our School =",len(list1))
            else:
                print("Wrong Choice \nTerminating")
                exit()
            print("Do you want to continue? (y or n)")
            inp5 = input("Enter Your Choice :")
            if inp5 == ('y' or 'Y'):
                continue
            else:
                break
    else:
        print("Your password or Username is incorrect\nTry Again.")

if inp1 == 4:
    print("Termianting")
    time.sleep(1)
    exit()