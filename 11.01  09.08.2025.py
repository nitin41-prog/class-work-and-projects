'''
Error handling:
Three types of errors:
1. sysntax error: when you get the syntax wrong (not follow the rule)
    these are the easiest of all the errors to find and fix
2. Logical error: implementation of the solution is wrong: eg use * instead of +
    Most difficult errors to find and fix
3. Run time errors or Exceptions: (errors that happens based on the given situation)
    Difficult to find but relatively easy to fix

'''

# print("Hello"  # SyntaxError: '(' was never closed
print(3 * 2)
a = 10
b = 10
print("A/B = ",a/b)
# ZeroDivisionError

# Exception Handling - handle these errors so that program dont end abruptly
# Steps need to follow:
# 1. Predict which line of code can give us error
# 2. Catch the error with pre-defined error code
'''
Error handling:
Three types of errors:
1. sysntax error: when you get the syntax wrong (not follow the rule)
    these are the easiest of all the errors to find and fix
2. Logical error: implementation of the solution is wrong: eg use * instead of +
    Most difficult errors to find and fix
3. Run time errors or Exceptions: (errors that happens based on the given situation)
    Difficult to find but relatively easy to fix

'''

# print("Hello"  # SyntaxError: '(' was never closed
print(3 * 2)
a = 10
b = 10
print("A/B = ",a/b)
# ZeroDivisionError

# Exception Handling - handle these errors so that program dont end abruptly
# Steps need to follow:
# 1. Predict which line of code can give us error
# 2. Catch the error with pre-defined error code
# 3. Decide what to do if there is an error and what to do if there is no error

# WAP to read two numbers and find their division
# ValueError, ZeroDivisionError
try:
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    rat = n1/n2
except ValueError:
    print("Invalid numbers")
except ZeroDivisionError:
    print("Denominator cant be zero")
else:  # else part will execute if there is no error
    print("N1 divided by N2 is",rat)
finally:
    print("Thank You!")

while True:
    try:
        n1 = int(input("Enter the first number: "))
    except ValueError:
     print("Invalid numbers! Fix and try again")
    else:
        break

while True:
    try:
        n2 = int(input("Enter the second number: "))
    except ValueError:
        print("Invalid numbers! Fix and try again")
    else:
        if n2==0:
            print("Denominator cant be zero, try again!")
        else:
            break
rat = n1/n2
print("N1 divided by N2 is",rat)

# Accessing the database from Python
# we need a library that understands how Python and the database works
# pymysql - this helps to connect to MYSQL database
# need to know: database name, where it is hosted, username, password
# select (2 way -> u need to send the query and get the result),
# insert, update, delete (1 way -> we only send the query) nothing is required to get back
# noinspection PyUnresolvedReferences
import pymysql
conn = pymysql.connect(host="localhost",database="moviedb",user="root",password="learnSQL")
# cursor is an object that will take your commands to the database
cur_obj = conn.cursor()
# SELECT
select_qr = "Select * from title where ID >= 110;"
# command to execute: cursor to execute
cur_obj.execute(select_qr)
# save the data returned from the database: recordset
results = cur_obj.fetchall()
print("Data from the DB:")
for row in results:
        print(row)
# method 2: passing value dynamically
print("Passing value dynamically")
# noinspection PyShadowingBuiltins
id = 132 # int(input())
select_qr = "Select * from title where ID >= '%d';"%(id,)
# command to execute: cursor to execute
cur_obj.execute(select_qr)
# save the data returned from the database: recordset
results = cur_obj.fetchall()
print("Data from the DB:")
for row in results:
    print(row)
# Next: Performing Data Manipulation Language: Like Insert, Update, Delete
# DML statements is temporary and active in that session only
# to save it, we need to use COMMIT

# query3 = "Insert into CASTS (ID, NAME, ROLE) values (1, 'Shah Rukh Khan', 'Actor')"
# noinspection SqlNoDataSourceInspection
qr4 = '''Select max(ID) \
             from casts;'''
cur_obj.execute(qr4)
results = cur_obj.fetchone()
# noinspection PyShadowingBuiltins
id = tuple(results)[0] + 1
print("New ID value = ", id)
names = ['A', 'B', 'C', 'D', 'Madhuri', 'Tabu', 'Sridevi']
roles = ['A', 'B', 'C', 'D', 'Actress', 'Actress', 'Actress']
# noinspection PyTypeHints,SqlNoDataSourceInspection
query3 = "Insert into CASTS (ID, NAME, ROLE) values ('%d','%s','%s')" % (id, names[id], roles[id])
cur_obj.execute(query3)
conn.commit()
elect_qr = "-- noinspection SqlNoDataSourceInspection"
# command to execute: cursor to execute
cur_obj.execute(select_qr)
# save the data returned from the database: recordset
results = cur_obj.fetchall()
print("Data from the DB:")
for row in results:
    print(row)
conn.close()
