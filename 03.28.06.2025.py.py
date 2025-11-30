print("Hello",end=" ")
print("There")

# logical operators:
# Rohit and Jaiswal will open the batting - prediction - 1
# Rohit or Jaiswal will open the batting - prediction - 2
# Rahul and Jaiswal opened the batting - actual
# Prediction 1 is WRONG
# Prediciton 2 is CORRECT
'''
# and:
True and True = True
False and True = False
True and False = False
False and False = False
'''
'''
# OR:
True or True = True
False or True = True
True or False = True
False or False = False
'''
# not: Not True = False; not False = True
n1,n2,n3=5,6,5
print(n1==n2 and n2!=n3 or n1>n2 and n1 <n3 or n3>n2 and n3<n2 or n2==n1 and  n1==n3)
#  F and T or F and F or F and T or F and  T
# # and (*) or (+)
#  F or F or F or F
#  F
print(not n1==n2 and n2!=n3 or n1>n2 and n1 <n3 or n3>n2 and n3<n2 or n2==n1 and  n1==n3)
# not F and T or F and F or F and T or F and  T
# T and T or F and F or F and T or F and  T
# T
print(not(n1==n2 and n2!=n3 or n1>n2 and n1 <n3 or n3>n2 and n3<n2 or n2==n1 and  n1==n3))
# not F
# T


# membership operator- in , not in

print("i" in "india")  # T
print("i" in "India")  # T
print("i" in "INDIA")  # F
print("i" not in "INDIA")  # T

'''
Conditional statements (conditions in Python) helps us to choose right 
set of code based on a certain condition
if ... elif ... else are used to check conditions
and if the condition is true in that block then those statement will be called
'''

# scenario 1: take input from user and if its a multiple of 10 print AWESOME
# and thank the user in any condition
usr = int(input("Enter a number: "))
if usr % 10==0:
       print("Awesome")
print("Thank you")
# 0 = False
if not usr % 10 :
       print("Awesome")
print("Thank you")


# scenario 2: take input from user and if its a multiple of 10 print AWESOME Multiple of 10
# otherwise print - not a multiple of 10
# and thank the user in any condition
usr = int(input("Enter a number: "))
if usr % 10==0:
    print("Awesome")
    print("Multiple of 10")
else:
    print("not a multiple of 10")
print("Thank you")
# 0 = False
if not usr % 10 :
    print("Awesome")
    print("Multiple of 10")
else:
    print("not a multiple of 10")
print("Thank you")

# scenario 3: take input from user and if its a multiple of 10 print AWESOME Multiple of 10
# otherwise check if its multiple of 5 then print Half Awesome
# otherwise print - not a multiple of 10 or 5
# and thank the user in any condition
usr = int(input("Enter a number: "))
if usr % 10==0:
    print("Awesome")
    print("Multiple of 10")
elif usr % 5 ==0:
    print("Half Awesome")
else:
    print("not a multiple of 10")
print("Thank you")
# 0 = False
if not usr % 10 :
    print("Awesome")
    print("Multiple of 10")
elif usr % 5 ==0:
    print("Half Awesome")
else:
     print("not a multiple of 10")
print("Thank you")

# program 1 scenario 1: wap to check if a number is positive or not
num=int(input("Enter a number: "))
if num>0:
    print("Number is positive")


# program 1 scenario 2: wap to check if a number is positive or not
num=int(input("Enter a number: "))
if num>0:
    print("Number is positive")
else:
    print("Number is not positive")


# program 1 scenario 3: wap to check if a number is positive, negative or zero
num=int(input("Enter a number: "))
if num>0:
    print("Number is positive")
elif num ==0:
    print("Number is zero")
else:
    print("Number is negative")

'''
3 BIGGEST POINT TO NOTE: DO NOT DUPLICATE
1. program which will take marks of 5 subjects and calculate avg
Based on average of the student assign grades
Condition for assigning grades:
1. < 50 % : E
2. 50-60: D
3. 60-70: C
4. 70-80: B
5. >80: A

Nested condition - condition inside a condition
1. If average is >90: Remark is Excellent and Very good for (80-90)
2. if avg>=95, President Medal
'''
m1 = int(input("Enter marks in subject 1: "))
m2 = int(input("Enter marks in subject 2: "))
m3 = int(input("Enter marks in subject 3: "))
m4 = int(input("Enter marks in subject 4: "))
m5 = int(input("Enter marks in subject 5: "))
total = m1 + m2 + m3 + m4 + m5
avg = total / 5
if avg>=80:
  print("Grade A")
if avg>=90:
  print("Remarks: Excellent")
if avg>=95:
  print("You win President Medal")
else:
  print("Remarks: Very Good")
'''
    elif avg>=70:
        print("Grade B")
        print("Remarks: Good")
    elif avg>=60:
        print("Grade C")
        print("Remarks: Good")
    '''


#
# Based on the complete program, write down what this program does
num = 19*110
if num%11 ==0:
       print(f"{num} is divisible by 11")
       if num //11 <10:
            print(f"{num} is a single digit multiple of 11")
       elif num //11 <100:
            print(f"{num} is a double digit multiple of 11")
else:
            print(f"{num} is a more than double digit multiple of 11")
if num%13 ==0:
       print(f"{num} is divisible by 13")
       # Home work, similar to what we did in if, complete this part as well

else:
       print(f"{num} is neither divisible by 11 or 13")



