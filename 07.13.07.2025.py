# tomorrow ie 13 JULY - No session, we shall meet on July 19th
txt1 = "I am fine How are you doing You there Come YOU here when you have time."
print(txt1.index("f",0,6))
print(txt1.index("f"))
print("YOU count: ",txt1.lower().count("you"))
print(txt1.lower().replace("you","them"))
print(txt1.lower().replace("you","them",1))

# Home work: For this given text, replace 3rd and 4th
# occurrence and not first 2 occurrences

txt1_out = txt1.split()
print("Split: \n",txt1_out)

txt1_out = txt1.split('a')
print("Split: \n",txt1_out)

# output of split is stored as a LIST (ie within a square bracket [])
txt2= ['where','are','you','going']
txt3 = " - ".join(txt2)
print(txt3)

'''
Collections / Data Structure / Advanced data types
    List, Tuple, Dictionary and Sets

List: can store multiple values (may belong to different data type)
List is created using []
'''

l1 = []
print(type(l1))
print("1. Number of members of L1 = ",len(l1))
l1 = ['Apple', 45,34.3, True,[2,3,4]]
print("2. Number of members of L1 = ",len(l1))
print(l1[0],l1[-1],l1[2])
print(type(l1[0]),type(l1[-1]),type(l1[2]))
print(l1[:3])
print([1,2,3] + [5,6,7])
print([1,2,3] + [5,6,7]*3)
print("1. For loop 1: ")
for member in l1:
    print(member)
print("2. For loop 2: ")
for idx in range(len(l1)):
    print(idx," : ", l1[idx])

# LIST Properties
# LIST: linear ordered mutable collection
str1 = "hello"
str1.upper()
print(str1) # immutable
list1 = [2, 3, 5]
print(list1) # mutable
list1[0] = 10
print(list1)
#str1[0] = "K" # TypeError: 'str' object does not support item assignment


l1 = [31]
# methods in the list:
# 1. append - will add given member at the end of the list
print("1. L1 = ",l1)
l1.append(21)
print("2. L1 = ",l1)
l1.append(41)
print("3. L1 = ",l1)
# 2. insert -
l1.insert(0,42)
print("4. L1 = ",l1)
l1.insert(2,22)
print("5. L1 = ",l1)
l1.insert(99,22)
print("6. L1 = ",l1)

# check if the value is available in the list before removing: count
val = 220
cnt = l1.count(val)
if cnt>0:
    l1.remove(val)
else:
    print("List doesnt have the given value")
l1.remove(22)  # will remove first occurrence of the value
# ValueError: list.remove(x): x not in list if value is not in the list
print("7. L1 = ",l1)
idx = 14
if len(l1) > idx >= 0:
    l1.pop(idx)
else:
     print("Invalid Index")
l1.pop(3) # takes index value from where to remove
# IndexError: pop index out of range error if index is invalid
print("8. L1 = ",l1)

l1.reverse()
print("9. L1 = ",l1)
l1.sort() # arrange the elements in increasing order
print("10. L1 = ",l1)
l1.sort(reverse=True) # arrange the elements in decreasing order
print("11. L1 = ",l1)

l2 = l1 # deep copy - L1 and L2 they point to the same data
l3 = l1.copy() # shallow copy - creates a duplicate copy - photocopy
print("12. L1 = ",l1)
print("12. L2 = ",l2)
print("12. L3 = ",l3)
l1.append(25)
l2.append(55)
l3.append(35)
print("13. L1 = ",l1)
print("13. L2 = ",l2)
print("13. L3 = ",l3)
idx = l1.index(22)
print("Position: ",idx)
# extend = l1 = l1+l2
l1.extend([10,20,30])
print("14. L1 = ",l1)
l1.clear() #delete all the members
print("15. L1 = ",l1)
print("15. L2 = ",l2)

# append - u can add a single member (any data type)
# extend - u can only add a list


'''
Lets write a program to implement a stack data structure
Stack: First In Last Out / Last In First Out


Home work: write a program to implement a Queue DS
Queue : First In First Out / Last In Last Out
'''
list_of_data = []
while True:
          print("Pick Your Option:")
          print("1. Add to the stack")
          print("2. Remove from the stack")
          print("3. Display the members")
          print("4. Quit")
          ch=input("Enter your choice: ")
          if ch=="1":
             val = input("Enter the member to be added: ")
             # list_of_data.append(val)
             list_of_data.insert(0,val)
          elif ch=="2":
              if len(list_of_data):
                 #list_of_data.pop() # last element by default
                 list_of_data.pop(0)
              else:
                   print("Stack is empty!")
          elif ch=="3":
               if len(list_of_data):
                  print("Values in the list: ",list_of_data)
               else:
                  print("Stack is empty!")
          elif ch=="4":
                  print("Thank you for using Stack!")
                  break
          else:
                  print("Invalid option try again...")
                  continue

# TUPLE: linear ordered immutable collection
# Tuple declared/created using  ()

t1 = ()
print(type(t1), ": ",len(t1))
t1 = (5,)
print(type(t1), ": ",len(t1))
t1 = (5,10,20,40,[1,2,3])
print(type(t1), ": ",len(t1))

print("Indexing: ", t1[0],t1[-1])
for i in t1:
    print(i)

#
print("Position: ",t1.index(10))
print("Value at: ",t1.count(10))

# reading data is fast in tuple compared to list
# when you are comparing collections, elements are checked by index
t2 = (10,40,100)
t3 = (10,30,300,900)
print("Which is greater?")
if t2 > t3:
   print(t2)
elif t3 > t2:
   print(t3)
else:
   print("they both are same!")

#Tuple and lists are convertible in each others format
t1 = (1,3,5,7)
t1 = list(t1)
t1.append(9)
t1 = tuple(t1)

'''
Dictionary: Linear unoredered mutable collection
data is stored in dictionary as a key-value pair
dict is created using {}
any datatype can be key and value but keys cant be repeated
'''

d1 = {}
print("type: ",type(d1))
d1 = {"Name":"Sachin","City":"Mumbai","Runs":36000,100: 289}
print(d1["Runs"])
print(d1["Name"])
# return values of all below 3 will be a list
print("List of keys in D1 = ",d1.keys())
print("List of values in D1 = ", d1.values())
print("List of keys-values pair (items) in D1 = ",d1.items())

print("List of keys in D1 = ",len(d1.keys()))
print("List of dictionary items in D1 = ",len(d1))
d2 = dict.fromkeys(["Name","City"])
d2["Name"] = "Virat"
print(d2)

