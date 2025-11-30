'''
Numpy will be used for Matrix

'''
import numpy as np
x = range(12)
mat1 = np.reshape(x,(3,4)) # rows=3,columns=4
print("Matrix 1:\n",mat1)

y = [[2,5,3,4],[4,7,1,5],[3,0,5,8]]
print(type(y))
mat2 = np.array(y)
print("Matrix 2:\n",mat2)
# indexing []
print(mat2[1,1],mat2[2,1])
print("Shape of the matrix: ",mat2.shape)

import pandas as pd
# array in numpy to create matrix
# dataframe in pandas to create table structure

l1 = [['Rohit','Virat','Bumrah','Sahi','Rishabh'],
      ['Bat','Bat','Ball','Ball','Wicket'],
      [221,198,168,122,99]]
print(l1)

df1 = pd.DataFrame(l1)
print(df1)
'''
DataFrame will convert into table and have numeric values starting from 0
to reference each row and column in the table.
Also, it has the header for row and column which we can add but if we dont add
then it will give same referene as the name also for these row and column

'''
print("# option 1: reference and namme are same for both ROWS and COLUMNS")
l2 = [['Rohit','Bat',221],['Virat','Bat',198],['Bumrah','Ball',168],
      ['Sami','Ball',122],['Rishabh','Wicket',99]]
df1 = pd.DataFrame(l2)
print(df1)

print("Option 2: Name the columns but now the rows")
df2 = pd.DataFrame(l2, columns=['Player','Type','Matches']) # pass column names as a list
print(df2)

print("Option 3: Name the columns and also the rows (Index)")
df3 = pd.DataFrame(l2, columns=['Player','Type','Matches'],
index=['Pos 1','Pos 2','Pos 3','Pos 4','Pos 5']) # pass column names as a list
print(df3)

print("Option 4: converting dictionary to dataframe: keys will become Column automatically")
d1 = {'Fruit':['Apple','Banana','Guava','Mango'],
'Production':[1122,3212,980,1111],
'Price':[235,75,90,210]}
print(type(d1))

df4 = pd.DataFrame(d1)
print(df4)

