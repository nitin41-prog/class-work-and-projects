print("How are you?")
print("I am fine")
print("How are you? I am fine.")
# \  backward slash: escape sequence (only 1 character)    / forward slash
# gives you power or take away from power
print("How are you?\nI am fine.")  # \n = newline
print("How are you?\tI am fine.")  # tab space \t

# \n is used for newline in Python
print("\\n is used for newline in Python")
# to print \n in Python we need to give \\n
print("to print \\n in Python we need to give \\\\n")

# He asked me,"What's your name?"

print('''He asked me,"What's your name?"''')
print('He asked me,"What\'s your name?"')
# filename: C:\Folder1\Folder2\file.txt  => C:\\Folder1\\Folder2\\file.txt
# or you can also use: C:/Folder1/Folder2/file.txt
# print has inbuilt newline (\n) which is not visible
# to bring below two print content in sameline, we need to remove this invisible \n
print("How are you?")
print("I am fine")
# we need to first make that invisible \n visible and then delete it
print("How are you?",end=" ")
print("I am fine",end="\n")

# program will always finish with exit code
# Process finished with exit code 0 (code = 0 program is successful)
a = 10
print(a)
b= input()
print(b)
print(type(b))
# Python cant guess what we want to enter so it always reads input value has a string
b = int(b)
print(b, type(b))
# functions to explicit data type conversion:  str(), int(), float(), bool(), complex()
c= int(input("Enter the length of the rectangular field: "))
print(c, type(c))
print("Area = ",b*c)

# Operations: Multiple operations that can be performed on the various data
# Arithmetic operations (mathematical operations)
# Operators:  +  -   *  /  ** (power)  // (integer division)  % (modulus - remainder)
num1, num2  = 10,5
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 ** num2)
print(num1 // num2)
print(num1 % num2)

print(30 ** (1/3))
print(19 // 5)
print(199 // 100)
print(19 % 5)

# currency notes of Rs 100, 50, 20, 10, 5, 1
# make a payment of 368
# 100 * 3 + 50 * 1 + 20 * 0 + 10 * 1 + 5 * 1 + 1 * 3
payment = int(input("Enter the payment to be made: "))
left_pay = payment
n_100 = n_50 = n_20 = n_10 = n_5 = n_1 = 0
n_100 = left_pay // 100
left_pay = left_pay % 100

n_50 = left_pay // 50
left_pay = left_pay % 50

n_20 = left_pay // 20
left_pay = left_pay % 20

n_10 = left_pay // 10
left_pay = left_pay % 10

n_5 = left_pay // 5
left_pay = left_pay % 5

n_1 = left_pay

print(f"{payment} = 100 * {n_100} + 50 * {n_50} + 20 * {n_20} + "
      f"10 * {n_10} + 5 * {n_5} + 1 * {n_1}")
# Operation: relational operators : check the relationship between 2 values
# operators:  <<=   >>=   ==    !=
# output : output is always boolean
num1, num2,num3 = 10,5,10

print("======== 1. ==============")
print(num1 < num2)  # F
print(num1 < num3)  # F
print(num1 <= num2)  # F
print(num1 <= num3)  # T
print("======== 2. ==============")
print(num1 > num2)  #  T
print(num1 > num3)  #  F
print(num1 >= num2)  # T
print(num1 >= num3)  #  T

print("======== 3. ==============")
print(num1 == num2)  #  F
print(num1 == num3)  #  T
print(num1 != num2)  # T
print(num1 != num3)  #  F

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

print("======== 1. ==============")
print(num1 < num2)  # F
print(num1 < num3)  # F
print(num1 <= num2)  # F
print(num1 <= num3)  # T
print("======== 2. ==============")
print(num1 > num2)  #  T
print(num1 > num3)  #  F
print(num1 >= num2)  # T
print(num1 >= num3)  #  T

print("======== 3. ==============")
print(num1 == num2)  #  F
print(num1 == num3)  #  T
print(num1 != num2)  # T
print(num1 != num3)  #  F

