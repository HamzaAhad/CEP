import sqlite3


#Query the data and return ALL records
def show_all(database_name,table_name):
    '''Takes two argunments database_name and table_name and return its all data'''
    database_name=str(database_name)
    table_name=str(table_name)
    Query = "SELECT rowid,* FROM " + table_name
    con = sqlite3.connect(database_name)
    #create a cursor
    cursor = con.cursor()
    cursor.execute(Query)
    elements=cursor.fetchall()
    for element in elements:
        print(element)
    return elements
    #commit our command
    conn.commit()
    #close our connection
    conn.close()

#ADD DATA TO THE DATABASE
def add_one_data(database_name,table_name,element):
    '''Takes two argunments database_name and table_name and add all data to respective table of database'''
    database_name=str(database_name)
    table_name=str(table_name)
    Query = "INSERT INTO" + " " + table_name + " " + "VALUES (?,?,?,?)"
    print(Query)
    conn = sqlite3.connect(database_name)
    #create a cursor
    cursor = conn.cursor()
    #element is in tuple format
    conn.execute(Query,element)

    print("command executed successfully")
    #commit our command
    conn.commit()
    #close our connection
    conn.close()

def add_many(database_name,table_name,list):
    database_name=str(database_name)
    table_name=str(table_name)
    Query = "INSERT INTO" + " " + table_name + " " + "VALUES (?,?,?,?)"
    conn = sqlite3.connect(database_name)
    #create a cursor
    cursor = conn.cursor()   
    cursor.executemany(Query,list)  
     #commit our command
    conn.commit()
    #close our connection
    conn.close()


def delete_one(database_name,table_name,product_name):
    database_name=str(database_name)
    table_name=str(table_name)
    Query = "DELETE from" + " " + table_name + " " + "WHERE product_name =" + " " + "'" + str(product_name) + "'"
    print(Query)
    conn = sqlite3.connect(database_name)
    #create a cursor
    cursor = conn.cursor()
    #delete records:
    cursor.execute(Query)
    conn.commit()
    #commit our command
    conn.commit()
    #close our connection
    conn.close()
# for table cart and wishlist 
def update_data(database_name,table_name,update_what,update_where):
    database_name=str(database_name)
    table_name=str(table_name)
    Query = "UPDATE" + " " + table_name + " " + "SET no_of_product =" + " " + str(update_what) + " " + "WHERE product_name =" + " " +"'"+ str(update_where)+"'"
     
    print(Query)
    #print(Query) 
    conn = sqlite3.connect(database_name)
    #create a cursor
    cursor = conn.cursor()
    
    cursor.execute(Query)    
    #commit our command
    conn.commit()
    #close our connection
    conn.close()

#for table items
def update_data_items(database_name,table_name,update_what,update_where):
    database_name=str(database_name)
    table_name=str(table_name)
    Query = "UPDATE" + " " + table_name + " " + "SET stock =" + " " + str(update_what) + " " + "WHERE product_name =" + " " +"'"+ str(update_where)+"'"
     
    print(Query)
    #print(Query) 
    conn = sqlite3.connect(database_name)
    #create a cursor
    cursor = conn.cursor()
    
    cursor.execute(Query)    
    #commit our command
    conn.commit()
    #close our connection
    conn.close()