#Modified MySQL operation code
#code to create or delete a database and table in mysql
import mysql.connector as sql

def connection_to_server():
    connection=sql.connect(host='localhost',user='root',password='root')                    #connection to mysql server 
    if connection.is_connected():
        print(connection)                                                                   #checking for the connection
        print('connected')
        
    return connection

def create_database():
    Database=input("select the database u want to create   ")
    cursor.execute("create database %s "%Database)                          #be in database
    print('Database created successfully  ')

def Database_showing():
    cursor.execute("show databases;")
    for i in cursor:
        print(i)

def Table_showing():#error error error
    cursor.execute('show tables')
    print("this database contains following tables")
    for i in cursor:
        print(i)
    else:                           #if no data in table 
        print("No table found ")    
        #break
    
def Table_data_showing():
    cursor.execute("select * from %s "%Table)
    for i in cursor:
        print(i)
    print('\nAbove data is there in the selected table  Avoid if no data found,')

def Table_creation():
    Table=input(" \n Enter the table name U Want to create \n  ")#table name
    create_table_command=("create table %s "%Table)             #%s replaces the variable
    str_table_elements=""
    column_no=int(input('how many columns to create  \n'))# for a loop to run that times
    a=1
    while a<=column_no:
        column_name=input('enter column name \n')
        col_type=input('enter datatype \n ')
        col_element=(str(column_name)+' '+str(col_type))#adding strings to resemble mysql command
        print(col_element)
        if not col_type in['integer','int']:                                     #int type datatype doesnot require bytes
            col_bytes=input('enter the desired bytes in bracket \n')
            col_element=(str(col_element)+str(col_bytes))
            print(col_element)
        a+=1
        str_table_elements+=col_element                 #
        str_table_elements+=(",")#inserting a comma after each column entry
    str_table_elements=("("+str_table_elements[:-1:]+")")   # adding parentheis before and after the command and removing the last comma, #bug two paraentheis at end
    #will use rstrip to remove the comma
    print(str_table_elements)
    create_table_command=(create_table_command+' '+str_table_elements)
    print(create_table_command)
    cursor.execute(create_table_command)


def end():
    print("re - run to try again\n you must enter valid password !!!")
    

        

print('Hi \n what do u want to do among these \n 1.Create a Database \n 2.Create Table \n 3.Delete database \n 4.Delete Table \n 5. Close\n\t Type the key associated to your choice \n')
choice=input()                                      #taking the input  from user to work further
while choice:
    if choice=='1':
        print ('You have chosen to create database  ')
        connection=connection_to_server()
        cursor=connection.cursor()#cursor creation
        create_database()
               

            
            
    elif choice=='2':
        connection=connection_to_server()
        cursor=connection.cursor()
        print("You have chosen To create a table  \n The following are available databases in this system... \n")
        Database_showing()
        print("\nSelect the database you want to use : ")
        Database=input('\n\n')
        cursor.execute("use %s "%Database)
        Table_showing()
        Table_creation()    
        
            

    elif choice=='3':
        connection=connection_to_server()
        cursor=connection.cursor()
        print("You have chosen To delete a database  \n Select the database you want to delete \n")
        Database_showing()
        Database=input('\n\n')
        password=input("Enter the password : ")
        if not password=='nothing':
            print("Wrong Password... You cant delete the database  ")
            end()
            break
            #improve  break
        cursor.execute("use %s"%Database)
        warning=input("Are you sure ??? this database contains the following tables\n\nyou are going to delete these tables too\n")
        Table_showing()
        if not warning in ['no','cancel','sorry']:
            cursor.execute("drop database %s"%Database)#command to delete a database
            print('database deleted succesfully \n\n')
        else:
            print('Database retained\n')


    elif choice=='4':
        connection=connection_to_server()
        cursor=connection.cursor()
        print('You have chosen to delete a table ')
        Database_showing()
        database=input("\nSelect The Database in which the table lies \n")
        cursor.execute("use %s"%database )                  #mysql command
        Table_showing()
        
                          #end loop
        Table=input('select the table to delete\n')
        Table_data_showing()
        warning=input( '\n ARE YOU SURE YOU WANT TO DELETE THE DATA ??? \n')
        if not warning in ['no','cancel','sorry']:
            cursor.execute("drop table %s"%Table)
            print("Table deleted successfuly\n\n")
        else:
            print("operation cancelled\n")
            
                    
                
    else:
        print('you have chosen not to do anything   ... bye,,, ')
        sys.exit()
    
        break                               #to terminate loop
    choice=input('want to work further?  \n 1.Create a Database \n 2.Create Table \n 3. Delete Database \n 4.Delete Table \n 5.Close\n\t Type the key associated to your choice \n') # asking if to re run the loop 
        
        

