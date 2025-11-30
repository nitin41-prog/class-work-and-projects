# Ditionary
# pair of key:value
# WAP to capture marks of 3 students with their roll number and marks in 3 subjects
# {101:[44,55,54], 105: [], 110: []}
# noinspection PyUnusedImports
import idx

subs = ["Maths", "Physics", "Chemistry"]
all_data = {}
num_students, num_subjects = 3, len(subs)
for i in range(num_students):
    roll = input("Enter the roll number of student " + str(i + 1) + ": ")
    marks = []
    for j in range(num_subjects):
        # noinspection PyTypeHints
        m = int(input("Enter the marks in " +subs[j] + ": "))
        marks.append(m)
    stu_dict = {roll: marks}
    all_data.update(stu_dict)

print("Marks for the students are:\n", all_data)
'''
 {'101': [44, 55, 54], '89': [78, 65, 49], '109': [65, 75, 49]}
'''

# task 2: calculate the total marks obtained by each student and update the list with the last value

for k in all_data.keys():
    tot = sum(all_data[k])
    print("total is: ",tot)
    all_data[k].append(tot)
    print(k, " = ", all_data[k])

print("All Data:\n", all_data)

students = {'89': "Sachin", '99': "Dhoni", '101': "Surya", '105': "Hardik",
            '106': "Sami", '107': "Jaiswal", '108': "Virat", '109': "Rohit"}
# task 3: find who topped in each subject and also the overall topper
'''
step 1: [[roll,m1],[[roll,m],[roll,m3],[roll,total]]
step 2: I will first assume, the first roll number has topped in all the subjects and also
is the overall topper.
step 3: take next sets of values one by one and compare with existing topper details
and update if required.
'''
toppers = []  # step 1: creating variable to save the data
isfirst = True
for k in all_data.keys():
    for i in range(num_subjects + 1):
        if isfirst:  # implemeting step 2
           toppers.append([k, all_data[k][i]])
        else:
             # step 3: compare other values
             # noinspection PyTypeHints
             if all_data[k][i] > toppers[i][1]:
                 # noinspection PyTypeHints
                 toppers[i][1] = all_data[k][i]
                 # noinspection PyTypeHints
                 toppers[i][0] = k

isfirst = False

print("List of toppers are: \n", toppers)
result = ""
# noinspection PyUnresolvedReferences,PyUnboundLocalVariable
for idx in range(len(toppers)):
    # noinspection PyTypeChecker
    if idx >= len(subs):
        # noinspection PyTypeHints,PyTypeChecker
        result = result + f"And the overall topper is {students[toppers[idx][0]]} with total marks of {toppers[idx][1]}."
    else:
        # noinspection PyTypeHints,PyTypeChecker
        result = result + f"Topper in the {subs[idx]} is {students[toppers[idx][0]]} with marks {toppers[idx][1]}. "

print(result)

all_data = {'101': [44, 55, 54, 153], '89': [78, 65, 49, 192], '109': [65, 75, 49, 189]}

all_data.pop('89')
print("After pop: ", all_data)

'''
Deep and Shallow copy
'''
all_data1 = all_data  # deep copy - they point to the same data
all_data2 = all_data.copy()  # shallow copy
# noinspection PyTypeChecker
all_data.update({105: [78, 89]})
print("All Data 1: ", all_data1)
print("All Data 2: ", all_data2)

# SETS - undordered collection: duplicates are not allowed and order doesnt matter
# Set are used to represent a value
# give me names of 5 fruits- A, B, G, M, P
# A AAAA => Duplicates are not allowed
# Order doesnt matter

# sets also like dict uses {}
s1 = {}
print("1. Type =", type(s1))

s1 = {7, "hello", 7, 99, "hello", 5.5}
print("2. Type =", type(s1))
print("Set: ", s1)

my_fruits = {"Apple", "Banana", "Guava", "Mango", "Pineapple"}
ur_fruits = {"Banana", "Guava", "Orange"}
print("UNION")
print(my_fruits | ur_fruits)  # | union operator
print(my_fruits.union(ur_fruits))

print("DIFFERENCE")
print(ur_fruits - my_fruits)
print(my_fruits.difference(ur_fruits))
print("SYMMETRIC DIFFERENCE")
print(my_fruits.symmetric_difference(ur_fruits))

print("INTERSECTION")
print(ur_fruits & my_fruits)
print(my_fruits.intersection(ur_fruits))

# Home Work - try following methods: all these methods will update the first set with the result
# update: A = A union B
# difference_update
# symmetric_difference_update:
# intersection_update:

my2_fruits = my_fruits.copy()  # shallow copy
my3_fruits = my2_fruits  # deep copy
print("Before pop: ", my_fruits)
# pop
my_fruits.pop()  # doesnt take any value - any value is removed
print("After pop: ", my_fruits)
# remove
my_fruits.remove("Apple")  # doesnt take any value - any value is removed
print("After remove: ", my_fruits)

# add an element (not compelete set)
my_fruits.add("Papaya")

print("My fruits: ", my_fruits)

print(my_fruits.issuperset(my_fruits))
print(my_fruits.issubset(my_fruits))
print(my_fruits.isdisjoint(my_fruits))

# Tuple, List and Set - are all inter convertible

set1 = {1, 5, 9, 3}
l1 = list(set1)
t1 = set(set1)

