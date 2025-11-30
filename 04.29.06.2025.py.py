"""
# calculate tax liability
# ask monthly income and calculate total annual income
based on the following parameters, calculate the taxes:
1. 0 - 50K: 0%
2. 50K-1L : 10%
3. 1L-3L : 15%
4. 3L to 5L : 20%
5. >5L: 25%
"""
mi = int(input("Enter your monthly income: "))
bonus = int(input("Enter your annual bonus: "))
yi = mi * 12 + bonus
print("Your total income for the year: ",yi)

case1 = 0  #income 0-50K
case2 = 0.1 * 50000  # >1L
case3 = 0.15 * 200000 # > 3L
case4 = 0.2 * 200000 # > 5L
case5 = (yi-500000) * 0.25

total_tax = 0
if yi>500000:
           total_tax = case1 + case2 + case3 + case4 + case5
elif yi>300000:
           total_tax = case1 + case2 + case3 + (yi-300000)*0.2
elif yi>100000:
           total_tax = case1 + case2 + (yi-100000)*0.15
elif yi>50000:
           total_tax = case1 + (yi - 50000) * 0.1
else: # <50K
           total_tax = case1

print("Your total tax liability is",total_tax)
'''
235,000
50K: 0 tax = 0
50-1L: 10%: = 5K
1- 3L: 15% = 135000*15% = 20250

1,035,000
50K: 0 tax = 0
50-1L: 10%: = 5K
1L-3L: 15% = 30K
3l-5L: 20% = 40K
5L * 25% = 1.25L
2L
'''
# usage of pass: indicate empty code
case1 = case2 = case3 = case4 = case5 = yi = 1
if yi>500000:
     pass
elif yi>300000:
     pass
elif yi>100000:
     pass
elif yi>50000:
     pass
else: # <50K
     pass

'''
Loops: programming uses loops to repeat certain set of logic
2 types of loops:
a. for loop: when you know exactly how many times to repeat a certain logic
b. while: you dont know exactly how many times to repeat but we know certain logic of repeating
c. switch: menu option

keywords: pass, break, continue
pass: just a placeholder /indicate empty code
# range() that will generate range of values - you need to give:
a. start value (inclusive)  b. stop value (exclusive - upto) c. step: increment
range(5,54,7): start=5, stop=50 and step=7
values: 5, 12, 19,26,33,40,47
range(5,10): default step is 1:  5,6,7,8,9
range(5): default start = 0, default step = 1: 0,1,2,3,4
'''
for counter in range(5,54,7):
      print(counter, end=", ")
print("\n==============")
for counter in range(5,10):
      print(counter, end=", ")
print("\n==============")
for counter in range(5):
      print(counter, end=", ")
print("\n==============")


# Generate first 20 odd numbers:
st_num = 1
for counter in range(20):
    print(st_num,end=", ")
st_num = st_num + 2
print()

for counter in range(1,40,2):
    print(counter,end=", ")
print()

# Home work: convert above program to generate Even numbers

# multiplication table
for num in range(1,11):
      for i in range(1,11):
          print(f"{i} * {num:<2} = {i*num:<2}", end= "   ")
      print()

for j in range(5):
  for i in range(5):
      print("*",end=" ")
  print()
print("===============")

for j in range(8):
   for i in range(j+1):
      print("*",end=" ")
   print()

print("===============")
num = 8
for j in range(num):
  for i in range(num-j):
       print("*",end=" ")
  print()

print("===============")

# While
st = 1
while st<= 5:
# while loop to have True condition for it to start
   print("Hello")
st += 1 #st = st+
'''
    x *= 5 : x = x*5
    x -= 6 : x = x-6
    '''




