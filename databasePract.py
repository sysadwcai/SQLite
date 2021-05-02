import sqlite3

conn = sqlite3.connect('Customer.db')

# create a cursor
c = conn.cursor()

# create a table
# c.execute("""CREATE TABLE #customers (
#   first_name text,
#  last_name text,
# email text
# )""")

# many_customers = [
#   ('Wes', 'Brown', 'wes@brown.com'),
#  ('Steph', 'Kuewa', 'steph@kuewa.com'),
# ('Dan', 'Pas', 'dan@pas.com')
# ]


# c.executemany("INSERT INTO #customers VALUES (?,?,?)", #many_customers)

#c.execute("SELECT * FROM  customers WHERE email like '%codemy.com'")
# c.fetchone()
# c.fetchmany(3)
# print(c.fetchall())
#items = c.fetchall()
#print("NAME" + "\t\tEMAIL")
#print("----------" + "\t--------")
# for item in items:
#   print(item)

#print("Command executed successfully...")
# commit our command

# c.execute(""" UPDATE customers SET first_name = 'John' WHERE rowid = 1
# """)

c.execute("DELETE from customers WHERE rowid = 6")
conn.commit()

c.execute("SELECT rowid, * FROM customers ORDER BY last_name DESC")
items = c.fetchall()
for item in items:
    print(item)

conn.commit()
# close our connection
conn.close()
