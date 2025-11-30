#date 21.06.2025
# for comment - python please dont read this text
print(    'I am fine') # print function prints the content within () on the screen
print("How are you?")
print   ('''Hi there'''    )
print()
print("""Hello""")
# print() also has newline at the end of the function
print(5+4)
print('5+4')
print('5+4=',5+4) # number of values that you give to a function is called as arguments/parameters
# print cant take multiple arguments
print('5+4=',5+4,"and 6*10=",6*10)

# variables: y = ax + b
a = 5  # we are assigning value 5 to a variable a
b= 10
x1=20
y1 = a*x1 + b
print("Value of Y1 =",y1)

x2=-10
y2 = a*x2 + b
print("Value of Y2 =",y2)

x2=-2
y2 = a*x2 + b
print("Value of Y2 =",y2)

# HW for today ie 21 JUNE 2025
# 1. calculate surface area and volumne of a cylinder of given radius and height
# 2. calculate surface area and volumne of a cone of given radius and height

# calculate area and perimeter of a rectangle of given length and breadth
length = 151
breadth = 127
area = length * breadth
peri = 2 *(length + breadth)
print("A rectangle with length",length,"metre and breadth",breadth,"metre "
      "has area of",area,"sq mt. and perimeter of",peri,"metre.")

# calculate area and circumference of a circle of given radius
radius = 151
PI = 3.14
area = PI * radius * radius
cir = 2 * PI * radius
print("A circle with radius",radius,"metre has an area of",area,"sq mt. and circumference of",cir,"metre.")

# keep this in mind while working with variables:
# 1. case sensitive
# 2. use pnemonics (use variable names that conveys the right meaning)
#  good examples: length, breadth, area, number_of_people
# bad examples: a,b,c,d, ertertergdefvdfgdfvdf,oeritoperitoi4345wfsdofsdfsd
# 3. while naming a varible, you can use alphabets (a-zA-Z) and numbers (0-9) and _ (underscore)
# 4. variable names can start only with text (a-zA-Z) or _ (underscore)

## Simple Datatypes: Simple- one variable will have only 1 value
# data types: types of value
# Python has 5 basic data types: integer (int), float, complex, boolean (bool), string (str)
# integer (int): numbers without decimal values (both _ve and +ve values)
# eg -99, 0, -9999999, 67

# type() - returns the type of data stored in that variable
# when you have multiple functions a(b(c(d()))) - evaluate from innermost to outermost
# everything in Python is treated as class - belonging to a certain group
num_of_passengers = 56  # integer (int)
print("Data type of num_of_passengers: ",type(num_of_passengers))
average_runs = 45.85  # float
print("Data type of average_runs: ",type(average_runs))

# imaginary numbers are called as complex numbers: squareroot of -ve numbers
# squareroot(25) = 5, squareroot(-25) = 5i (i is in Maths, in Python we represent as j)
solution_1 = 25j
print("Data type of solution_1: ",type(solution_1))
print(5j*5j)  # 25(-1) = -25 + 0j
# 7.3 + 2.7 = 10.0

is_prime = False # True: spelling- first char caps and rest small
# bool will have only 2 values: True and False
print("is_prime: ",type(is_prime))

#5. string (str)- text
greeting1, greeting2, greeting3, greeting4 = "Hello",'Ola',"""Namaste""",'''take care'''
print(type(greeting1),type(greeting2),type(greeting3),type(greeting4))

# calculate area and perimeter of a rectangle of given length and breadth

length = 151
breadth = 127
area = length * breadth
peri = 2 *(length + breadth)
print("A rectangle with length",length,"metre and breadth",breadth,"metre "
      "has area of",area,"sq mt. and perimeter of",peri,"metre.")
# formatting - using f string
print(f"A rectangle with length {length} metre and breadth {breadth} metre "
f"has area of {area}sq mt. and perimeter of {peri} metre.")

# calculate area and circumference of a circle of given radius
radius = 151
PI = 3.14
area = PI * radius * radius
cir = 2 * PI * radius
print("A circle with radius",radius,"metre has an area of",area,"sq mt. and circumference of",cir,"metre.")
print(f"A circle with radius {radius} metre has an area of {area}sq mt. and circumference of {cir:.2f} metre.")

name,country,pos = "Virat","India","Batsman"
s1 = 10
print(f"The player {name:10} plays for the country {country:^17} and he is a {pos:x>15} in the team.")
name,country,pos = "Mangwaba","South Africa","Wicket-Keeper"
print(f"The player {name:<10} plays for the country {country:.^17} and he is a {pos:>15} in the team.")

print("checking");print("I am fine")

