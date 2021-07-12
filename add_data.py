import sqlite3

conn = sqlite3.connect("item.db")
#create a cursor
cursor = conn.cursor()

many_items = [("CLOTHES","PANT",230.23,23),
                ("ELECTRONICS","TV",50000.4,54),
                ("FOOD","CAKE",1980,4)]
conn.executemany("INSERT INTO items VALUES (?,?,?,?)",many_items)

print("command executed successfully")
#commit our command
conn.commit()
#close our connection
conn.close()