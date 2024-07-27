while(True):
    print("""
                    =================================================================================
             
                                                     Mobile Market  

                    =================================================================================
    """)
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="ks7098")
    mycursor=mydb.cursor()
    mycursor.execute("CREATE DATABASE if not exists Eshop")
    mycursor.execute("use Eshop")
    mycursor.execute("create table if not exists customer_info(name varchar(100) primary key,contact_no varchar (20) ,address varchar(50))")
    mycursor.execute("create table if not exists product_info(product_name varchar(50) primary key,product_code varchar (20) not null,price_RS varchar (10) not null,brand_name varchar(100) not null,wareenty varchar(60),catagori varchar(20) not null,stock_available int(10))")
    mycursor.execute("create table if not exists staff_info(staff_ID varchar(10) not null,name varchar(100) primary key,age int(2) not null,address varchar(100),contact_no varchar(20),salary varchar(10) not null)")
    mycursor.execute("create table if not exists sales_info(customer_name varchar(50) not null,date_of_purchase varchar (20) not null,product_name varchar(50) not null,product_code varchar (20) not null,payment varchar(30)not null)")
    mycursor.execute("create table if not exists user_data(username varchar(30) primary key,password varchar(30) default'000')")
    mycursor.execute("create table if not exists service_info(complaint_no int(15) not null,customer_name varchar(50) not null,date_of_purchase varchar (20) not null,product_name varchar(50) not null,product_code varchar (20) not null,prombem varchar(200) not null)")


    while(True):
        print("""
                                                        1. Sign in
                                                        2. Admin
                                                        3. Sign up
                                                        4. Exit
                                                                                """)
    
        r=int(input("Enter your choice: "))

        if r==3:
            print("""

                    =================================================================================
                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Sign up!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    =================================================================================

                                                        """)
            u=input("ENTER YOUR PREFERRED USERNAME:")
            p=input("""ENTER YOUR PREFERRED PASSWORD
(Password should be lest 6 character):""")
            mycursor.execute("insert into user_data values('"+u+"','"+p+"')")
            mydb.commit()

            print("""
                    =================================================================================
                    !!!!!!!!!!!!!!!!!!!!!!!!!!!REGISTERED SUCCESSFULLY!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    =================================================================================
                                                    """)
            x=input("-------------------------------------------------PRESS ENTER TO CONTIUE-------------------------------------------------")

        
        elif r==1:

            print("""
                    =================================================================================
                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  {{SIGN IN }}  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    =================================================================================
                                                        """)
            un=input("ENTER THE USERNAME!!:")
            ps=input("ENTER THE PASSWORD!!:")
                
            mycursor.execute("select password from user_data where username='"+un+"'")
            row=mycursor.fetchall()
            for i in row:
                a=list(i)
                if a[0]==str(ps):
                    while(True):
                        print("""
                                                            1.Sales
                                                            2.Service
                                                            3.Stock Available
                                                            4.Sign Out
                                                                      
                                                                      """)
                        a=int(input("ENTER YOUR CHOICE:"))

                            
                        if a==1:
                            cname=input("ENTER CUSTOMER NAME:")
                            dop=input("ENTER DATE:")
                            pname=input("ENTER PRODUCT NAME:")
                            pcode=input("ENTER PRODUCT CODE:")
                            model=input("ENTER BRAND/MODEL:")
                            price=input("ENTER PRICE:RS.")
                            discount=input("ENTER DISCOUNT PRICE:")
                            gt=input("GRAND TOTAL:")
                            paym=input("ENTER PATMENT METHOD:")

                            mycursor.execute("insert into sales_info values('"+cname+"','"+dop+"','"+pname+"','"+pcode+"','"+paym+"')")
                            
                            mydb.commit()
                            print("""------------------------------------------------------------------------------------------------------------------------------------
                                    YOUR PURCHASE IS SUCCESSFULL
                                                                                           """)
                            x=input("----------------------------------------------------------PRESS ENTER TO CONTINUE--------------------------------------------------")

                                
                        elif a==2:
                            print("""
                    =======================================================================================
                    -----------------------------------------Service---------------------------------------
                    =======================================================================================
                                    """)

                            cno=input("ENTER COMPLAINT NUMBER:")
                            cname=input("ENTER CUSTOMER NAME:")
                            dop=input("ENTER DATE OF PURCHASE:")
                            pname=input("ENTER PRODUCT NAME:")
                            pcode=input("ENTER PRODUCT CODE:")
                            model=input("ENTER MODEL:")
                            pro=input("ENTER THE PROBLEM:")

                            mycursor.execute("insert into service_info values('"+cno+"','"+cname+"','"+dop+"','"+pname+"','"+pcode+"','"+pro+"')")
                            mydb.commit()
                            print("""------------------------------------------------------------------------------------------------------------------------
                                        YOUR COMPLAINT IS BOOKED SUCCESSFULL""")
                            x=input("----------------------------------------------------------PRESS ENTER TO CONTINUE---------------------------------------")

                        elif a==3:
                            print("""
                    =======================================================================================
                    -------------------------------------Stock Available-----------------------------------
                    =======================================================================================
                                    """)
                            
                            mycursor.execute("select * from product_info")
                            row=mycursor.fetchall()
                            for i in row:
                                b=0
                                v=list(i)
                                k=["NAME","CODE","PRICE","MODEL","FEATURE","CATAGORI","STOCK AVAILABLE"]
                                d=dict(zip(k,v))
                                print(d)

                            x=input("-------------------------------------------------------PRESS ENTER TO CONTINUE------------------------------------------")

                        elif a==4:
                            break


        elif r==2:
            
            print("""

                    =================================================================================
                    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!     Admin     !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                    =================================================================================

                                                        """)
            un=input("ENTER THE USERNAME!!:")
            ps=input("ENTER THE PASSWORD!!:")
                
            mycursor.execute("select password from user_data where username='"+un+"'")
            row=mycursor.fetchall()
            for i in row:
                a=list(i)
                if a[0]==str(ps):
                    while(True):
                        print("""
                                                            1.Staff Info
                                                            2.Product Info
                                                            3.Sales Done
                                                            4.Customer Info
                                                            5.Sign Out
                                                                      
                                                                      """)

                        b=int(input("ENTER YOUR CHOICE:"))

                        if b==1:
                            print("""
                    =================================================================================
                    ------------------------------------Staff Info-----------------------------------
                    =================================================================================

                                                             1.Add New Staff
                                                             2.Remove Staff
                                                             3.Staff Details
                                                             4.Exit
                                    """)
                            c=int(input("ENTER YOUR CHOICE:"))

                            if c==1:
                                print("""
                    ==================================================================================
                    -----------------------------------ADD NEW STAFF----------------------------------
                    ==================================================================================
                                      """)
                                                        
                                
                                sid=input("ENTER STAFF ID NO:")
                                sname=input("ENTER STAFF NAME:")
                                age=input("ENTER STAFF AGE:")
                                add=input("ENTER STAFF ADDRESS:")
                                no=input("ENTER STAFF CONTACT NO:")
                                sal=input("ENTER MONTHLY SALARY:")

                                mycursor.execute("insert into staff_info values('"+sid+"','"+sname+"','"+age+"','"+add+"','"+no+"','"+sal+"')")
                                mydb.commit()
                                
                                print("""
                    ================================================================================
                    ---------------------------SUCCESSFULL ADDED NEW STAFF--------------------------
                    ================================================================================
                                         """)
                                x=input("----------------------------------------------------------PRESS ENTER TO CONTINUE--------------------------------------------------")


                                
                            elif c==2:
                                 
                                 name=input("ENTER STAFF'S NAME:")
                                 
                                 mycursor.execute("select * from staff_info where name='"+name+"'")
                                 row=mycursor.fetchall()
                                 print(row)
                                 p=input("you really wanna delete this data? (y/n):")
                                 if p=="y":
                                     mycursor.execute("delete from staff_info where name='"+name+"'")
                                     mydb.commit()
                                     print("SUCCESSFULLY DELETED!!")
                                 else:
                                     print("NOT DELETED")


                            elif c==4:
                                break

                            elif c==3:

                                print("""
                        =======================================================================================
                        ---------------------------------------Staff Details-----------------------------------
                        =======================================================================================
                                    """)
                            
                            mycursor.execute("select * from staff_info")
                            row=mycursor.fetchall()
                            for i in row:
                                b=0
                                v=list(i)
                                k=["STAFF ID","NAME","AGE","ADDRESS","CONTACT NO","SALARY"]
                                d=dict(zip(k,v))
                                print(d)
                            x=input("-------------------------------------------------------PRESS ENTER TO CONTINUE----------------------------------------------")

                            

                        elif b==2:
                            print("""
                     =======================================================================================
                     --------------------------------------Product Info-------------------------------------
                     =======================================================================================

                                                            1.Add New Product
                                                            2.Remove Product
                                                            3.Stock Available
                                                            4.Exit
                                    """)
                            d=int(input("ENTER YOUR CHOICE:"))

                            if d==1:
                                print("""
                     ==================================================================================
                     ----------------------------------ADD NEW Product---------------------------------
                     ==================================================================================
                                      """)
                                                        
                                
                                pname=input("ENTER PRODUCT NAME:")
                                pcode=input("ENTER PRODUCT CODE:")
                                price=input("ENTER PRICE_RS:")
                                brand=input("ENTER BRAND/MODEL:")
                                war=input("ENTER WAREENTY PERIOD:")
                                cat=input("ENTER CATAGORI:")
                                stock=input("ENTER STOCK AVAILABLE:")

                                mycursor.execute("insert into product_info values('"+pname+"','"+pcode+"','"+price+"','"+brand+"','"+war+"','"+cat+"','"+stock+"')")
                                mydb.commit()
                                
                                print("""
                        ================================================================================
                        --------------------------SUCCESSFULL ADDED NEW PRODUCT-------------------------
                        ================================================================================
                                         """)
                                x=input("----------------------------------------------------------PRESS ENTER TO CONTINUE--------------------------------------------------")


                            elif d==2:

                                 
                                 name=input("ENTER PRODUCT NAME:")
                                 
                                 mycursor.execute("select * from product_info where product name='"+name+"'")
                                 row=mycursor.fetchall()
                                 print(row)
                                 p=input("you really wanna delete this data? (y/n):")
                                 if p=="y":
                                     mycursor.execute("delete from product_info where product name='"+name+"'")
                                     mydb.commit()
                                     print("SUCCESSFULLY DELETED!!")
                                 else:
                                     print("NOT DELETED")


                            elif d==4:
                                break
                                

                            elif d==3:
                                 print("""
                            =======================================================================================
                            ------------------------------------Stock Available------------------------------------
                            =======================================================================================
                                    """)
                                 
                                 mycursor.execute("select * from product_info")
                                 row=mycursor.fetchall()
                                 for i in row:
                                     b=0
                                     v=list(i)
                                     k=["NAME","CODE","PRICE","MODEL","FEATURE","CATAGORI","STOCK AVAILABLE"]
                                     d=dict(zip(k,v))
                                     print(d)

                                 x=input("-------------------------------------------------------PRESS ENTER TO CONTINUE----------------------------------------------")


                        elif b==3:

                            print("""
                    =======================================================================================
                    ----------------------------------------Sales Done-------------------------------------
                    =======================================================================================
                                    """)
                            
                            mycursor.execute("select * from sales_info")
                            row=mycursor.fetchall()
                            for i in row:
                                b=0
                                v=list(i)
                                k=["CUSTOMER NAME","DATE OF PURCHASE","PRODUCT NAME","PRODUCT CODE","PAYMENT"]
                                d=dict(zip(k,v))
                                print(d)

                            x=input("-------------------------------------------------------PRESS ENTER TO CONTINUE----------------------------------------------")

                        elif b==4:

                             print("""
                    =======================================================================================
                    ------------------------------------Customer details-----------------------------------
                    =======================================================================================
                                    """)
                            
                             mycursor.execute("select * from customer_info")
                             row=mycursor.fetchall()
                             for i in row:
                                 b=0
                                 v=list(i)
                                 k=["CUSTOMER NAME","CONTACT NUMBER","ADDRESS"]
                                 d=dict(zip(k,v))
                                 print(d)

                             x=input("-------------------------------------------------------PRESS ENTER TO CONTINUE----------------------------------------------")


                        elif b==5:
                            break

                            
                            
                        
