'''
Functions:
Types based on who is coding/creating:
1. Inbuilt functions : comes prebuilt with Python installations
2. User defined functions: comes written by the users

Based on return type: 1) Returns  2) Doesnt return

Based on input parameters:
1. Required parameter
2. Positional
3. Default
4. Keywords
5. Variable number of arguments

Lambda/One line function
'''
# High order functions: Map, Filter, Reduce

# MAP : makes a function get applied over all the values of a list
# WAP to convert all the values given in the USD into INR
usd_val = [23,44,43,29, 30,20,56,54,111,99,105,107,55,95]
# 1 USD = 88 INR

def usd_inr(a):
    return a*88

# Approach 1
inr_val1=[]
for i in usd_val:
    inr_val1.append(usd_inr(i))
print("Approach 1. Values in INR: ", inr_val1)

# Approach 2 - using MAP
inr_val2 = list(map(usd_inr,usd_val))
print("Approach 2. Values in INR: ", inr_val2)
# Approach 3: we will use lambda instead
inr_val3 = list(map(lambda x:x*88,usd_val))
print("Approach 3. Values in INR: ", inr_val3)
# FILTER: you filter out values from the existing list
# WAP to display only the values that are multiple of 5
# Approach 1
filter_val = []
for i in usd_val:
 if i%5==0:
     filter_val.append(i)
print("1. Filtered list: ",filter_val)

# Approach 2: using filter function
# the function passed to filter has to return either True or False
filter_val2 = list(filter(lambda x:x%5==0,usd_val))
print("2. Filtered list: ",filter_val2)

# Reduce: gives a single value as output
# takes a function and list of values and reduces the entire list into a single value
# reduce is based on the logic that is applied to all the values in the given list
# the function that goes into Reduce() takes 2 parameters, and the return value is the logic
# that is applied over 2 values
# reduce() we need to import functools
from functools import reduce
ret_val = reduce(lambda a,b:a+b,usd_val)
# first take 2 paramters from the list and add them
# then keep repeating by taking the previous result and add next value from the list
# Total repeatation would be n-1 (n=number of items in the list)
# first iteration, we take 2 values from the list and then 1 value at a time
print("Total Dollar spent = ", ret_val)

# CLASS & OBJECTS
# class that defines a group (properties)
# object is the usable form of that class
'''
properties:
1. Some properties are common for all the class - that makes them belong to same class
2. some properties are specific to each object
'''

l1 = [3,4,5,6]
l2 = [1,2,3,4,5]

# l1 and l2 are two different objects of the same class - LIST
# class properties: append(), sort(), insert(), ...
# object properties: values of the list, first member, second member

'''
Properties for class and objects:
1. variable
2. methods (functions that are defined in a class)

We will see 4 types of properties:
1. Class variable  X
2. Class method   X
3. Object variable  X
4. Object method   X
'''


# noinspection PyAttributeOutsideInit
class Books:
    total_books = 0
    '''
    Above variable is directly inside a class hence its neither regular nor object variable
    But its a CLASS VARIABLE
    CLASS properties are same for all the members of the class
    '''
    '''
    Lets define two methods - one to get the object details, and the second
    method to display the details.
    '''
    def get_book(self,title,author,price):
        '''
        Self is just a keyword which is acting like a label to indicate that this
        is a object method. Why self? You can use anything, any text as a label
        but self is internationally recognized and accepted.
        '''
        print("I am in get_book!")
        # whereever you use self from now, it means you are calling object
        # lets create 3 object variables for each of the 3 variables being passed here
        self.title = title
        # noinspection PyAttributeOutsideInit
        self.author = author
        # noinspection PyAttributeOutsideInit
        self.price = price

    def count_books(self):
        pass


# accessing class variable here
Books.total_books +=1

# second object method
def display_book(self):
        print("="*30)
        print("Book Title: ",self.title)
        print("Author    :",self.author)
        print("Price     :",self.price)
        print("=" * 30)

def count_books(cls):
        print("-"*30)
        print("Total number of books in the library = ",cls.total_books)
        print("-" * 30)

book1 = Books()
print("Value of total_books:")
print("-"*25)
print("using class: ",Books.total_books)
Books.total_books += 1
print("using object: ",book1.total_books)
print("-"*25)


book1.get_book("Learn and Practice Python","Swapnil Saurav",295)
book2 = Books()
book2.get_book("Machine Learning","Saurav Swapnil",650)
# so far we have created 2 objects of the class Books
book2.display_book()
book1.display_book()

print("Calling Class Methods: can be called using both class name and object name(s)")
Books.count_books()
book1.count_books()
book2.count_books()


# WAP to implement Queue
'''
__init__() - its a special method which is called immediately when object is created
this method is used for initializing the variables and the members to be used later

'''
class MyQueue:

    def __init__(self):
        self.myqueue = []
    def DisplayQ(self):
        if len(self.myqueue) ==0:
            print("Queue is Empty!")
        else:
            print("The members in the Queue are: \n",self.myqueue)


def AddQ(self,element):
    self.myqueue.append(element)

def RemoveQ(self):
#removes the first element
    if len(self.myqueue) ==0:
         print("Queue is already Empty!!!")
    else:
        self.myqueue.pop(0)

q1 = MyQueue()  # __init__() is automatically called here
q1.AddQ(50)
q1.AddQ(70)
q1.AddQ(60)
q1.DisplayQ()
q1.RemoveQ()
q1.RemoveQ()
q1.RemoveQ()
q1.DisplayQ()
