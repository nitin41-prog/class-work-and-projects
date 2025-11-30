'''
User defined functions (udf)
* Defining doesnt mean calling
* Needs to be defined before calling
* def keyword to define a function
* docstring : multiline comment add as the very first line in the function
    docstrings are not mandatory but highly recommended.
    Purpose: users will be able to know about the function before using them

* when you see a function or a variable with double underscore (__) before and after its name,
    means they have some specific meaning. Hence we create our own variables or functions
    dont use __ before and after the name
    For example, __doc__ gives the docstring of the function
'''
# functions with no input parameters and no return value
def myquestions():
   '''
    This is a sample function created to learn how functions work.
    :return: it doesnt return anything
    '''
print("What's your name?")
print("Where are you from?")
print("What's going?")


myquestions()
myquestions()
myquestions()
print(myquestions.__doc__)
help(myquestions)
help(print)

'''
arguments:
* required: you have to pass the values
* positional: you have to pass in that specific order
* (non-required) default: it has a default value and takes that when no values are passed to it
* (non-positional) Keyword: using the same argument name while calling you can change the order too
* variable length arguments: any number of arguments - 0 to any number. Values can be saved as a
    Tuple (arguments) or as a dictionary (keyword arguments)
'''
def myaddition1():
    print("MyAddition1: ")
    a,b=20,30
    print(f"Value of a is {a} and b is {b}.")
    c = a + b
    print("Sum of these two values are: ",c)

def myaddition2(a,b):
    print("MyAddition2: ")
    print(f"Value of a is {a} and b is {b}.")
    c = a + b
    print("Sum of these two values are: ",c)

def myaddition3(a,b=10): # b has default value
    print("MyAddition3: ")
    print(f"Value of a is {a} and b is {b}.")
    c = a + b
    return c

def myaddition4(a,*b,**c):
    print("MyAddition 4:")
    print("A (required argument)= ",a)
    print("B (Tuple) = ",b)
    print("C (Dictionary) = ",c)


# noinspection PyShadowingNames
def isprime(num):
    out = True
    # noinspection PyShadowingNames
    for i in range(2, num//2+1):
        if num%i==0:
           out = False
        break
    return out




print("Filename: class work python.py: __name__ = ",__name__)
if __name__ =="__main__":

     myaddition1()

     x=55
     y = 75

     myaddition2(x,y)
    # myaddition2() missing 2 required positional arguments: 'a' and 'b'

# noinspection PyUnboundLocalVariable
result = myaddition3(x,y)
print("The output generated is ",result)
result = myaddition3(x)
print("The output generated is ",result)
result = myaddition3(b=x,a=y)
print("The output generated is ",result)


myaddition4(8)
myaddition4(1,3,5,7,9,2,4,6,8)
myaddition4(1,3,5,7,9,2,4,6,8,name="Sachin",city="Mumbai",game="Cricket")
val = 15
if isprime(val):
    print("Its a Prime number!")
else:
    print("Its not a Prime number!")
val = 45
if isprime(val):
    print("Its a Prime number!")
else:
    print("Its not a Prime number!")
val = 13
if isprime(val):
    print("Its a Prime number!")
else:
    print("Its not a Prime number!")
val = 5
if isprime(val):
    print("Its a Prime number!")
else:
    print("Its not a Prime number!")

# WAP to generate prime numbers from 500 to 700
for i in range(500,700):
  if isprime(i):
   print(i,end=", ")
print()


'''
We have 1 line function:
We have 1 line condition:
We have 1 line loops:
    if the logic can be written in one line

'''

# check if a number is positive or not
num = -5
if num>0:
   print("Positive")
else:
   print("Not Positive")
result = "Positive" if num>0 else "Not Positive"
print(result)
print("Positive" if num>0 else "Not Positive")


# one line loops output can be saved as a list
# generate first 10 natural numbers: 1..10
for i in range(1,11):
    print(i)

vals = [i for i in range(1,11)]
print(vals)

# check for Odd and Even for first 10 natural numbers: 1..10
vals = [i%2==0 for i in range(1,11)]
print(vals)

# pick only even numbers from first 10 natural numbers: 1..10
vals = [i for i in range(1,11) if i%2==0]
print(vals)

# write a function to perform cube of given numbers: lambda function (1 line function)
# lambda arguments: expression
# noinspection PyShadowingNames
my_cube = lambda x: x**3

print(my_cube(10))
