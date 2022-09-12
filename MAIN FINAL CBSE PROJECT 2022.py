import mysql.connector as m
import random
conn=m.connect(host="localhost",user="root",password="root",database="eldorado_booking")
cursor = conn.cursor()
print("\n********************WELCOME TO ELDORADO BOOKING SYSTEM***********************")
def customer_selections():
    while True:
        acc = input("\nDO YOU HAVE A ACCOUNT (Y/N)")
        em = []
        if acc=='y' or acc=='yes' or acc=='Y' or acc=='YES':
            email = input("\nENTER YOUR EMAIL ID:-")
            em.append(email)
            pas = input("\nENTER YOUR PASSWORD:-")
            otp = int(input("\nENTER A OTP CODE ON YOUR EMAIL AND PHONE NO:-"))
            
            print("\n-------LOGIN SUCCESSFUL-------")
        else:
            nam = input("\nENTER YOUR FULL NAME:-")
            pn = int(input("\nENTER YOUR PHONE NO:-"))
            srt = input("\nENTER YOUR STREET NAME:-")
            emrt = input("\nENTER YOUR EMIRATES:-")
            em = input("\nENTER YOUR EMAIL ID:-")
            em=em+"@gmail.com"
            passw = input("\nENTER YOUR PASSWORD:-")
            print(f"\nOTP SEND TO {pn} AND {em}")
            ot = int(input("\nENTER THE OTP NO:-"))
            
            print("\n-------YOUR ACCOUNT IS CREATED SUCCESSFULLY-------")
            print("\n THESE ARE THE LATEST MOVIES----")
            sql1 = "select movies from movies"
            cursor.execute(sql1)
            for a in cursor:
                print(a)
                
    
            name = []
            movname = input("\n WHICH MOVIE YOU WANT TO WATCH :-")
            ticket = int(input("\n ENTER NUMBER OF TICKETS YOU WANT :-"))
            for b in range(ticket):
                nam = input("\nENTER NAME :-")
                name.append(name)
            
            hall = []
            date = []
            timing = []
            charges = []
            sql2 = "select hall from movies where movies = '{}' ".format(movname)
            cursor.execute(sql2)
            for c in cursor:
                hall.append(c)
                
            sql3 = "select date from movies where movies = '{}'".format(movname)
            cursor.execute(sql3)
            for d in cursor:
                date.append(d)
            
            sql4  = "select timing from movies where movies = '{}'".format(movname)
            cursor.execute(sql4)
            for e in cursor:
                timing.append(e)
            
            sql5 = "select charges*{} from movies where movies = '{}'".format(ticket, movname)
            cursor.execute(sql5)
            for f in cursor:
                charges.append(f)
                
            seatnum = random.randint(1, 100)
            
            print(f"YOU HAVE TO PAY {charges} DIRHAMS")
            pay = input("TO PAY ENTER (P) :-")
            
            print("\nYour Ticket is Here - ")
            
            if ticket==1:
                print(f"\nNAME = {name}          MOVIE NAME = {movname}      HALL = {hall}")
                print(f"TIMING = {timing}      DATE = {date}             CHARGES = {charges}      ")
                print(f"seat number = {seatnum}")
                print(f"your ticket has been send to your email {em}")
            if ticket>1:
                print(f"\nNAME = {name}          MOVIE NAME = {movname}      HALL = {hall}")
                print(f"TIMING = {timing}      DATE = {date}             CHARGES = {charges}      ")
                print(f"seat number = {seatnum} to {seatnum+(ticket-1)}")
                print(f"your ticket has been send to your email {em}")
                break

def add():
    while True:
        print("ADD CUSTOMER DETAILS")
        s_no=int(input("ENTER SNO:"))
        nam = input("\nENTER FULL NAME:-")
        pn = int(input("\nENTER PHONE NO:-"))
        em = input("\nENTER EMAIL ID:-")
        em=em+"@gmail.com"
        movie=input("\nENTER MOVIE NAME:-")
        sql6="insert into customer_details values('{}','{}','{}','{}','{}')".format(s_no,nam,pn,em,movie)
        cursor.execute(sql6)
        conn.commit()
        print("DETAILS ENTERED SUCCESSFULY")
        break

def display():
    x=int(input("CUSTOMER_DETAILS TABLE ->1 MOVIES TABLE ->2 \nEnter no:"))
    if x==1: #CUSTOMER_DETAILS TABLE
        print("Contents from table:")
        sql7=("select * from customer_details")
        cursor.execute(sql7)
        rs=cursor.fetchall()
        for i in rs:
            for j in i:
                print(j,end="\t |")
            print()
    elif x==2: #movies table
        print("Contents from table:")
        sql8=("select * from movies")
        cursor.execute(sql8)
        rs=cursor.fetchall()
        for i in rs:
            for j in i:
                print(j,end="\t |")
            print()
    
def edit():
    movname=input("Enter Movie Name:")
    chrgs=int(input("Enter new charges:"))
    sql9=("update movies set charges={} where movies='{}'").format (chrgs,movname)
    cursor.execute(sql9)
    conn.commit()
    print("Printed Successfully!!")

def delete():
    movname=input("Enter Movie Name:")
    sql10=("delete from movies where movies='{}'").format(movname)
    cursor.execute(sql10)
    conn.commit()
    print("Deleted Successfully!!")

def search():
    sql11=("select s_no,movies,charges from movies where charges<30")
    cursor.execute(sql11)
    rs=cursor.fetchall()
    for i in rs:
        for j in i:
            print(j,end="\t |")
        print()
    print("Printed Successfully!!")
    
def sort():
    sql12=("select * from movies order by charges desc")
    cursor.execute(sql12)
    rs=cursor.fetchall()
    for i in rs:
        for j in i:
            print(j,end="\t |")
        print()
    print("Printed Successfully!!")


def login():  # Log in the user
    login_username = input("Enter your username: ")
    password = input("Enter your password: ")
    cursor.execute("SELECT username, password FROM auth")
    rs = cursor.fetchall()

    if len(rs) == 0:
        sys.exit("Username doesn't exist!")

    while True:

        for i in rs:
            if i[0] == login_username and i[1] == password:
                print("Login successful!")
                print("Hello,", login_username + "!" "\n")

            elif i[0] != login_username or i[1] != password:
                sys.exit("Username or password is incorrect!")

        break

def register_customer():  # Register a new customer
    name = input("Enter your Full Name: ")
    email = input("Enter your email: ")
    phone_number = input("Enter your phone number in international format: ")
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    db.execute("INSERT INTO customers(name, email, phone_number, username, country_code) VALUES(%s, %s, %s, %s)",
               (name, email, phone_number, username))
    cdb.commit()
    db.execute("INSERT INTO auth VALUES(%s, %s)", (username, password))
    conn.commit()


while True:
    print("""
    +-----------------------+
    |   ELDORADO BOOKING    |
    +-----------------------+
    | 1. SIGN UP            |
    | 2. SIGN IN            |
    +-----------------------+ 
    """)
    ch1 = int(input("Enter your choice: "))
    if ch1 == 1:
        register_customer()
        v = input("Would you like to continue? (y/n): ")
        if v.lower() != 'y':
            break
        
    
    elif ch1 == 2:
        login()


    print("""
+-----------------------+
|   ELDORADO BOOKING    |
+-----------------------+
| 1. CUSTOMER SELECTION |
| 2. ADD RECORD         |
| 3. DISPLAY            |
| 4. EDIT               |
| 5. DELETE             |
| 6. SEARCH             |
| 7. SORT               |
+-----------------------+ """)
    ch=int(input("Enter your choice:"))
    if ch==1:
        customer_selections()
    elif ch==2:
        add()
    elif ch==3:
        display()
    elif ch==0:
        break
    elif ch==4:
        edit()
    elif ch==5:
        delete()
    elif ch==6:
        search()
    elif ch==7:
        sort()
    else:
        print("Invalid Option!!")
    
print("\n \t THANK YOU!")
