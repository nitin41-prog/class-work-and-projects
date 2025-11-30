# Loops
# For loop - repeat when we know exactly how many times to run
# while loop: while loop is based on a condition:
# we can use while loop in 2 kinds of situation:
# 1. Entry condition: before you run the loop, condition is checked and
# if true loop will be performed.
# 2. Exit condition: it easily starts the loop but exit is checked

# add first 10 multiples of 5
num = 5
count = 1
total = 0
while count <=10:
    total+=num# total = total + num
count+=1
num+=5

print("Total value is",total)

# calculate sum of all positive numbers entered
total = 0
to_continue = True
while to_continue:
   num = int(input("Enter the number: "))
   if num>=0:
        total+=num
else:
   to_continue = False

print("1. Total of all the numbers entered is",total)

# red0 above program
total = 0
while True:
  num = int(input("Enter the number: "))
  if num>=0:
            total+=num
  else:
      break


print("2. Total of all the numbers entered is",total)


# break is a command which will throw you out of the loop
'''
loop 1
loop 2
break  # loop 2ends -which means loop 3 also ends
loop 3
break # thro you out of loop 3
   

'''

# generate fibonacci numbers  - using FOR Loop
# 0, 1, 1,2, 3, 5, 8, 13,21, 34, 55, .
# prev = 0
curr = 1
num = int(input("Enter how many Fibonacci numbers you want: "))
if num<1:
   print("No numbers to generate")
else:
   print("\n Fibonacci numbers are:")
print("0",end=", ")
if num>=2:
  print("1",end=", ")
for i in range(num-2):
  print(prev + curr,end=", ")
'''
            tot = prev + curr
prev = curr
curr = tot
            '''
prev,curr = curr, prev+curr
'''
            lines 15 and 16 is NOT same as line 18, because in 15 and 16, we are running them
            in an order but in line 18, we are running them parallely

            '''
print("")

# generate fibonacci numbers  - using FOR Loop
# 0, 1, 1,2, 3, 5, 8, 13,21, 34, 55, ...
prev,curr = 0,1
count = 1
num = int(input("Enter how many Fibonacci numbers you want: "))
if num<1:
   print("No numbers to generate")
else:
   print("\n Fibonacci numbers are:")
   print("0",end=", ")
if num>=2:
    print("1",end=", ")
while count<=num-2:
    print(prev + curr,end=", ")
prev,curr = curr, prev+curr
count+=1
print("")

# prime number generation
# 12: 1,2,3,4,6,12
# 13: 1,  13

num = int(input("Enter a number: "))
is_prime = True

for i in range(2, num//2+1):
    if num %i ==0:
          is_prime = False
          break

if is_prime:
       print(num,"is a prime number!")
else:
       print(num,"is not a prime number!")

# prime number generation between given range
num1 = int(input("Enter the starting number: "))
num2 = int(input("Enter the ending number: "))
print("Prime numbers are: ")
for num in range(num1,num2+1):
      is_prime = True
for i in range(2, num//2+1):
      if num %i ==0:
          is_prime = False
          break
if is_prime:
      print(num,end=", ")

# Mini -Project building a guessing number game
'''
Computer (thought of the number) v Human (Guessing)

1. check if the number has been guessed correctly
2. Keep repeating untill use gets it correctly
3. Count the steps taken to guess it
4. Guess number should be between 1 and 100, if guessed invalid more than once
 game should be over
5. Invalid attempts neednt be calculated as an attempt
6. add hint to the user, tell if the guess is higher or lower than the number

continue: keyword will take you to the beginning of the loop
Functions to generate random numbers are not available directly. They are
there with python install but hidden. You need to inport them by importing
module. Module is a file with many functions added there.
randint() which is in random module generated random number between given ranges
both inclusive.
'''
import random  # random module has random generation related functions
num = random.randint(1,100)
attempts = 0
is_invalid = False
while True:  # infinite loop

    guess = int(input("Guess the number (1-100): "))
    if guess <1 or guess>100:
        if is_invalid:
           print("You lose! This is your second invalid attempt!")
           break
        else:
             is_invalid = True
             print("This is your first invalid attempt, one more will end the game!")
             continue
    attempts+=1

# Remove any leading spaces from the 'elif' line:
# Define variables first
secret_number = 42
attempts = 0

# --- Start of the LOOP ---
while True:  # This loop runs indefinitely until a 'break' is hit
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == num:
        print(f"Congratulations! You guessed it correctly in {attempts} attempts!")
        break
    elif guess < num:
        print("Sorry! thats incorrect, Try again with a higher number... ")
    else:
        print("Sorry! thats incorrect, Try again with a lower number... ")

'''
Next step:
1. We played Computer v Human game. Can we change it to Computer v Computer where
computer will think and also try to guess - Try as home work - we will in the next class
2. We took 5 steps to guess - is that a good job or bad job? We will only know when we 
calculate the average value. If our guess is < average then we did well otherwise we did bad!
In the next class we will see how to find the average value

last topic in loops:
 1. How to work with Menu generation program
 and also share assignment 2 (Python 1) based on Loops and conditions (ATM Simulator)

 2. We will move on to Strings (and advanced data structure: collections)
'''




