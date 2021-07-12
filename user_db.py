#USER DATABSASE WILL CONTAIN ALL THE DETAILS ABOUT THE SHOPPING HISTORY

import sqlite3
def creating_table(execution_statement):
    #CREATING CONNECTION
    con = sqlite3.connect("user.db")

    #create a cursor
    cursor = con.cursor()

    #create a Table for product
    cursor.execute(execution_statement)

    #commit our command
    con.commit()
    #close our connection
    con.close()

#TABLE shop_his WILL BE IN FOLLOWING TUPLE FORMAT 
#TABLE 
#(NAME , ADDRESS , PRODUCT , AMOUNT)
creating_table("""CREATE TABLE IF NOT EXISTS shop_his(name text,address text,product text,amount real)""")


