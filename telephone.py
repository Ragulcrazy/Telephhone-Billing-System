import mysql.connector as mq
from tabulate import tabulate
def menu():
    print("\n\t\t\t TELEPHONE BILLING SYSTEM")
    print("\t\t\t ========================\n\n")
    print("\t\t\t\t MAIN MENU")
    print("\t\t\t\t =========")

    print("\t\t1.Register User \t 2.Search Customer \n")
    print("\t\t3.Update Customer \t 4.Generate Bill\n")

    print("\t\t5.Delete Customer \t 6.Help\n\n \t\t7.Exit")


def register():
    print("\t\t\t\tNew Customer Registration")
    print("\t\t\t\t-------------------------\n\n")
    ph_num = int(input("\nEnter Your Phone Number : "))
    name = input("\nEnter Your Name : ")
    address = input("\nEnter Address : ")
    aadhar_num = input("\nEnter Aadhar Number : ")
    con = mq.connect(host="localhost",user="root",passwd="Ragul@29@root@123",database="telephone_billing")
    cur = con.cursor()
    query = "insert into customer(ph_no,name,address,aadhar_no)values({},'{}','{}','{}')".format(ph_num,name,address,aadhar_num);
    cur.execute(query);
    con.commit()
    print("\nSuccessfully Registered...")

def Search():
    print("\t\t\t\tSearch Customer...")
    print("\t\t\t\t-------------------------\n\n")
    ph_num = int(input("\nEnter Your Phone Number : "))
    con = mq.connect(host="localhost",user="root",passwd="Ragul@29@root@123",database="telephone_billing")
    cur = con.cursor()
    query = "select * from customer where ph_no={}".format(ph_num)
    cur.execute(query)
    result = cur.fetchall()
    if result == []:
        print("Customer doesn't exist...")
    else:
        print("\n PhNo    Name       Address       AadharNo    Bill Status")
        print(tabulate(result))
    con.close()
    

def modify():
    print("\t\t\t\tUpdate Customer Details...")
    print("\t\t\t\t-------------------------\n\n")
    ph_num = int(input("\nEnter Your Phone Number : "))
    con = mq.connect(host="localhost",user="root",passwd="Ragul@29@root@123",database="telephone_billing")
    cur = con.cursor()
    query = "select * from customer where ph_no={}".format(ph_num)
    cur.execute(query)
    result = cur.fetchall()
    if result == []:
        print("Customer doesn't exist...")
    else:
        print("1.Name\n2.Address\n3.Aadhar No")
        ch = int(input("Enter choice to Update : "))
        if ch == 1:
            name = input("Enter New Name : ")
            query = "update customer set name ='{}' where ph_no={}".format(name,ph_num)
            cur.execute(query)
            con.commit()
            print("\nName has been Updated Successfully...")
        elif ch == 2:
            address = input("Enter New Address : ")
            query = "update customer set address ='{}' where ph_no={}".format(address,ph_num)
            cur.execute(query)
            con.commit()
            print("\nAddress has been Updated Successfully...")
        elif ch == 3:
            aadhar = input("Enter New Aadhar : ")
            query = "update customer set aadhar ='{}' where ph_no={}".format(aadhar,ph_num)
            cur.execute(query)
            con.commit()
            print("\nAadhar Number  has been Updated Successfully...")
        else:
            print("Please choose coreect choice...")

def billing():
    print("\t\t\t\tGenerate Bill")
    print("\t\t\t\t--------------\n\n")
    #print("\t\t\t\t-------------------------\n\n")
    ph_num = int(input("\nEnter Your Phone Number : "))
    con = mq.connect(host="localhost",user="root",passwd="Ragul@29@root@123",database="telephone_billing")
    cur = con.cursor()
    query = "select * from customer where ph_no={}".format(ph_num)
    cur.execute(query)
    result = cur.fetchall()
    if result == []:
        print("Customer doesn't exist...")
    else:
        calls = int(input("Enter No of calls : "))
        bill = 0
        if calls > 150:
            bill = bill +(calls-150)*3 + 50 * 2.5 + 50 * 1.5
        elif 100<calls<150:
            bill = bill  + (calls-100)*2.5 + 50 * 1.5
        elif 50<calls<100:
            bill = bill + (calls-50)*1.5
        print("\t\t\t\tBilling")
        print("\t\t\t\t-------\n")
        print("\t\t\t-------------------------")
        if result[0][5]!="Paid":
            old_bill = result[0][4]
        else:
            old_bill = 0
        print("\n\t\t\tPending Bill Amount : ",old_bill)
        print("\n\t\t\tNew Bill Amount     :",bill)
        print("\t\t\t-------------------------")
        
        print("\t\t\tTotal Bill Amount : ",bill + old_bill)

        print("\t\t\t-------------------------")
        ch = input("Please Y to Pay the Bill now or press any other key to Pay later : ")
        if ch in ["y","Y"]:
            query = "update customer set bill ={},status='Paid' where ph_no={}".format(bill+old_bill,ph_num)
            cur.execute(query)
            con.commit()
            print("\nPayment has been Paid Successfully!!")
        else:
            query = "update customer set bill ={},status='Un-Paid' where ph_no={}".format(bill+old_bill,ph_num)
            cur.execute(query)
            con.commit()
            print("\nPlease!! make a Payement as soon as possible")
    con.close()

def delete():
    print("\t\t\t\tDelete Customer")
    print("\t\t\t\t----------------")
    ph_num = int(input("\nEnter Your Phone Number : "))
    con = mq.connect(host="localhost",user="root",passwd="Ragul@29@root@123",database="telephone_billing")
    cur = con.cursor()
    query = "select * from customer where ph_no={}".format(ph_num)
    cur.execute(query)
    result = cur.fetchall()
    if result == []:
        print("Customer doesn't exist...")
    else:
        ch = input("Are you sure to delete customer ..Y/N : ")
        if ch in ["Y","y"]:
            query = "delete from  customer where ph_no={}".format(ph_num)
            cur.execute(query)
            con.commit()
            print("\n Customer Database has been deleted Successfully!!")
        else:
            print("No changes made in your Database")
    con.close()
        
    

def helping():
    print("\t\t\tHelp")
    print("\t\t\t----")
    print("First 50 calls are Free")
    print("50-100 calls are  1.5rs per call")
    
while True:

    menu()
    ch = int(input("Enter Your Choice : "))

    if ch == 1:
        register()
    elif ch == 2:
        Search()
    elif ch == 3:
        modify()
    elif ch == 4:
        billing()
    elif ch == 5:
        delete()
    elif ch == 6:
        helping()
    elif ch == 7:
        exit()
    else:
        print("Please Choose Correct Choice...")


    ch = int(input("\n\nPress 0 to continue..Any other Key to Exit : "))
    if ch != 0:
        break
    

