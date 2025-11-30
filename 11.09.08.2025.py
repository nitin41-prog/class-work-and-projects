'''
Property Inheritance:
1. We end up creating Parent (Base class) - Child (Derived class) relationships.
All the properties of the base class is available to the derived class but if the
derived class already has those properties then derived class will use its own.
Relationship doesnt stop at 1 or 2 levels, same concept goes through multiple levels

Encapsulation (Data hiding):
variable: Public variable
_variable (1 underscore): Protected variable : concept is there but not yet implemented in python
    behaves like public only
__variable (double underscore): Private variable: these variables can not be used outside of the class
'''
class MyCollection:
    def __init__(self, type_col):
        self.mycollection = []
        self.type_col = type_col
        self.__test_var = "HELLO"

    def DisplayC(self):
        if len(self.mycollection) ==0:
            print(f"Nothing to display in the {self.type_col}!")
        else:
            print(f"The members in the {self.type_col} are: \n",self.mycollection)

    def AddC(self,element):
            self.mycollection.append(element)
            print("ADD ========== Test Variable is: ", self.__test_var)
class MyQueue(MyCollection):
    def __init__(self):
        MyCollection.__init__(self, "Queue")
# noinspection PyPep8Naming
    def RemoveC(self):
        # removes the first element
        if len(self.mycollection) == 0:
            print("Queue is already Empty!!!")
        else:
            self.mycollection.pop(0)
            print("REMOVE ========== Test Variable is: ", self.__test_var)


# noinspection PyPep8Naming
class MyStack(MyCollection):
    def __init__(self):
            MyCollection.__init__(self,"Stack")
    def RemoveC(self):
        #removes the first element
        if len(self.mycollection) ==0:
           print("Stack is already Empty!!!")
        else:
           self.mycollection.pop(-1)
        print("REMOVE ========== Test Variable is: ", self._test_var)

s1 = MyStack()
s1.AddC(30)
s1.AddC(33)
s1.AddC(38)
s1.AddC(40)
s1.AddC(50)
s1.DisplayC()
s1.RemoveC()
s1.DisplayC()

s1 = MyQueue()
s1.AddC(30)
s1.AddC(33)
s1.AddC(38)
s1.AddC(40)
s1.AddC(50)
s1.DisplayC()
s1.RemoveC()
s1.DisplayC()



