#ITEM DATABSASE WILL CONTAIN ALL THE DETAILS ABOUT THE PRODUCT 



import sqlite3
def creating_table(execution_statement):
    #CREATING CONNECTION
    con = sqlite3.connect("item.db")

    #create a cursor
    cursor = con.cursor()

    #create a Table for product
    cursor.execute(execution_statement)

    #commit our command
    con.commit()
    #close our connection
    con.close()

#TABLE ITEMS WILL BE IN FOLLOWING TUPLE FORMATE 
#TABLE ITEMS
#(PRODUCT TYPE , PRODUCT NAME , PRODUCT PRICE , STOCK)

creating_table("""CREATE TABLE IF NOT EXISTS items(product_type text,product_name text,product_price real,stock int)""")

#TABLE CART
creating_table("""CREATE TABLE IF NOT EXISTS cart(product_type text,product_name text,product_price real,no_of_product int)""")

#TABLE WISHLIST
creating_table("""CREATE TABLE IF NOT EXISTS wishlist(product_type text,product_name text,product_price real,no_of_product int)""")
