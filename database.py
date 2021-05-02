import sqlite3
# query the database and return all records


def show_all():
    # connect to database
    conn = sqlite3.connect('customer.db')
    # create a cursor
    c = conn.cursor()

    # query the database
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    # commit our command
    conn.commit()
    # close our connection
    conn.close()

# add a new record to the table


def add_one(first, last, email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES (?,?,?)", (first, last, email))
    # commit our command
    conn.commit()
    # close our connection
    conn.close()

# add many records to table


def add_many(list):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES (?,?,?)", (list))
    # commit our command and close connection
    conn.commit()
    conn.close()

# delete record from table


def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)
    # commit our command and close connection
    conn.commit()
    conn.close()

# lookup with where


def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers WHERE email = (?)", (email,))
    items = c.fetchall()

    for item in items:
        print(item)

    # commit our command and close connection
    conn.commit()
    conn.close()
