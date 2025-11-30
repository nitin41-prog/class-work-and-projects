# Class: creating a blueprint/template
# every Object will be copy of this template (class)

from p2 import Cars

class Books:
    pass

book1 = Books()
print(type(book1))
c1 = Cars()
print("Cars: ",type(c1))