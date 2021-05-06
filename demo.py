import sqlite3
from employee import Employee # the Employee file is in the same directory as the demo.py

conn = sqlite3.connect('employee.db') # for in-memory db use (':memory:') for testing-fresh DB on every run

c = conn.cursor() # allow to execute command

#c.execute(""" CREATE TABLE IF NOT EXISTS tblEmployees (first text, last text, pay integer)""")

def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO  tblEmployees VALUES (:first, :last, :pay)",
              {'first': emp.first, 'last': emp.last, 'pay': emp.pay})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM tblEmployees WHERE last=:last", {'last': lastname,})
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute(""" UPDATE tblEmployees SET pay = :pay
                    WHERE first = :first AND last = :last""",
                  {'first': emp.first, 'last': emp.last, 'pay': pay})

def remove_emp(emp):
    with conn:
        c.execute("DELETE FROM tblEmployees WHERE first = :first AND last = :last",
                  {'first': emp.first, 'last': emp.last})

emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 90000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)
update_pay(emp_2, 95000)
remove_emp(emp_1)
#print(emp_1.first)
#print(emp_1.last)
#print(emp_1.pay)

#c.execute("INSERT INTO  tblEmployees VALUES (?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay)) #one way to have placeholder

#conn.commit()
#2nd way placeholder - a dictionary
#c.execute("INSERT INTO  tblEmployees VALUES (:first, :last, :pay)", {'first': emp_2.first, 'last':emp_2.last, 'pay': emp_2.pay})

#conn.commit()

#c.execute("SELECT * FROM tblEmployees WHERE last=?", ('Cai',))
#print(c.fetchall())

#c.execute("SELECT * FROM tblEmployees WHERE last=:last", {'last': 'Doe',})
#print(c.fetchall())

#c.execute("delete from tblEmployees where rowid = 4")
#conn.commit()

conn.close()