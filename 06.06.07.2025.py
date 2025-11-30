# Mini -Project building a guessing number game
# computer v computer
import random  # random module has random generation related functions
num = random.randint(1,100)
attempts = 0
st,ed = 1,100
is_invalid = False
while True:  # infinite loop

    #guess = int(input("Guess the number (1-100): "))
    guess = random.randint(st, ed)
    if guess <1 or guess>100:
        if is_invalid:
            print("You lose! This is your second invalid attempt!")
            break
        else:
           is_invalid = True
           print("This is your first invalid attempt, one more will end the game!")
           continue
    attempts+=1
    if guess == num:
        print(f"Congratulations! You guessed it correctly in {attempts} attempts!")
        break
    elif guess<num:
        st = guess + 1
        print("Sorry! thats incorrect, Try again with a higher number... ")
    else:
        ed = guess - 1
        print("Sorry! thats incorrect, Try again with a lower number... ")

# Mini -Project building a guessing number game
# run the program 1 lakh times to find the average attempts
import random  # random module has random generation related functions
total = 100000
# average attempt = total_attempts / total
total_attempts = 0
for i in range(total):
    num = random.randint(1, 100)
    attempts = 0
st,ed = 1,100
is_invalid = False
while True:  # infinite loop

        #guess = int(input("Guess the number (1-100): "))
        guess = random.randint(st,ed)
        if guess <1 or guess>100:
            if is_invalid:
               print("You lose! This is your second invalid attempt!")
               break
            else:
             is_invalid = True
             print("This is your first invalid attempt, one more will end the game!")
             continue
        attempts+=1
        if guess == num:
             print(f"Congratulations! You guessed it correctly in {attempts} attempts!")
             break
        elif guess < num:
             st = guess + 1
             print("Sorry! thats incorrect, Try again with a higher number... ")
        else:
             ed = guess - 1
             print("Sorry! thats incorrect, Try again with a lower number... ")

print("Average attempts = ",total_attempts/total)

'''
WAP to input 2 numbers and then provide menu to choose from
different operations.
'''

while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("  MENU : ")
    print("1. Add \n2. Subtract \n3. Multiply")
    print("4. Divide \n5. Exit")
    ch = input("Enter your choice: ")
    if ch=="1":
       print("Addition of given numbers: ",num1 + num2)
    elif ch=="2":
       print("Subtraction of given numbers: ",num1 - num2)
    elif ch=="3":
       print("Multiplication of given numbers: ",num1 * num2)
    elif ch=="4":
       print("Division of given numbers: ",num1 / num2)
    elif ch=="5":
       print("Thank you for using our program.")
    break


'''
WAP to input 2 numbers and then provide menu to choose from
different operations - using match-case
'''

while True:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("  MENU : ")
    print("1. Add \n2. Subtract \n3. Multiply")
    print("4. Divide \n5. Exit")
    ch = input("Enter your choice: ")
    match ch:
        case "1":
           print("Addition of given numbers: ",num1 + num2)
        case "2":
           print("Subtraction of given numbers: ",num1 - num2)
        case "3":
           print("Multiplication of given numbers: ",num1 * num2)
        case "4":
           print("Division of given numbers: ",num1 / num2)
        case "5":
           print("Thank you for using our program.")
           break
        case _:
           print("Invalid option, try again!")
           continue

'''
Strings (str) are ways to handle handle
there is no difference between ' and " : they can handle single line of text

there is no difference between triple ' and ": they are used to
handle multiple lines
'''

a= 'hi'
b = "hello"
c = '''how are you?
Where are you?
How do we do?'''
d = """I am fine
I am super fine
I am super duper fine"""

print(type(a),type(b),type(c),type(d))
print(c)
print(d)


# indexing / slicing - [] is used here
# [] is used for indexing not only in str but also
# everywhere else: list, tuple, dict, numpy, pandas
# single character: I need to know the index or the position
'''
H   E   L    L     0
0   1   2    3     4   => Left to right indexing
-5  -4  -3   -2   -1   <= Right to Left indexing
'''
txt1 = "I am fine"
tot = len(txt1)
print(txt1[2], txt1[-tot+2])
print(txt1[5], txt1[-4])
# continous values start:end (start in inclusive and end is exclusive)
# first 3 characters
print(txt1[0:3], txt1[:3])
# am f
print(txt1[2:6])
# last 3 characters
print(txt1[-3:])

# give me alternate characters- start:end:step
print(txt1[::2])  # start is default, end is default and step is 2

# add two strings together
print("abc"+"xyz")
#multiplication
print("abc"+"xyz"*3)

for i in "abcde":
    print(i)

print("---")
# WAP to count the number of vowels in a given string
txt1 = "I am fine How are you doing there Come here when you have time."
total_vowels = 0
for ch in txt1:
    if ch in "aeiouAEIOU":
          total_vowels+=1

print("Total vowels = ",total_vowels)

txt = ""
print(type(txt)) #<class 'str'>
# class means group of similar data which has same properties
# "abc", "5", "" -> these are similar data belonging to group called str class
# what are the properties of a str class?
# properties can be variables and methods (functions belonging to a class)
# Official documentation for str: https://docs.python.org/3.13/library/stdtypes.html#str

txt = "I AM FINE how are you?"
print(txt.capitalize())
print(txt)
print(txt.upper())
print(txt.lower())
txt= "hello123"
print(txt.isalnum()) # if it has alpha numeric:atoz and 0 to 9
print()

num1 = input("Enter a number: ")
# strip() removes blank spaces before and after the text
num1 = num1.strip()
if num1.isdigit() :  # check if the text has only digits
   num1 = int(num1)
   print(num1 * 10)
else:
   print("Invalid number")


#
txt1 = "I am fine How are you doing there Come here when you have time."
total_vowels = 0
for ch in txt1.lower():
    if ch in "aeiou":
       total_vowels+=1

print("Total vowels = ",total_vowels)
print("Total characters: ",len(txt1))
print("Non-Vowels characters: ",len(txt1) - total_vowels)

total_conso = 0
for ch in txt1.lower():
    if c in "aeiou .":
       total_conso+=1

print("Total consonants = ",total_conso)

abc = "            "
print("Is ABC blank text: ",abc.isspace())


txt1 = "I am fine How 22323 &*** ((( are you doing there Come here when you have time."
total_conso = 0
for ch in txt1.lower():
    if ch.isalpha() and c in "aeiou":
       total_conso+=1
print("Total consonants = ",total_conso)

txt1 = "I am fine How are you doing You there Come YOU here when you have time."
print(txt1.index("f",0,6))
print(txt1.index("f"))
print("YOU count: ",txt1.lower().count("you"))
print(txt1.lower().replace("you","them"))
print(txt1.lower().replace("you","them",1))

# Home work: For this given text, replace 3rd and 4th
# occurrence and not first 2 occurrences




