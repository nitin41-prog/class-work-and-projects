import pandas as pd

d1 = {'Fruit':['Apple','Banana','Guava','Mango'],
'Production':[1122,3212,980,1111],
'Price':[235,75,90,210]}
print(type(d1))

df1 = pd.DataFrame(d1, index=['City A','CityB','CityC','City D'])
print(df1)
# indexing: reading subpart of the dataframe
print("Reading column values: Single column (Series)")
print(df1['Production'])
print("Read column as numpy array")
np1 = df1['Production'].values
print(np1)
print("Read column as List")
l1 = df1['Production'].tolist()
print(l1)

print("Multiple columns from the dataframe:")
print(df1[['Fruit','Production']])

print("=========== HANDLING INDEX =======")
print(df1.index)
print(df1.index.tolist())
print("Index values:")
print(df1.index[1])

'''
iloc() = works on the reference of columns and index (0,1...)
loc() - works on the names (of columns and index)
'''
print(" All data from index called City C:")
print(df1.loc['CityC'])
print(df1.loc['CityC'].to_dict())
print(df1.iloc[2])
print(df1.iloc[2].values) # numpyaaray

'''
Reference is given to each row and column (0,1,2..)
If name is given then its takes new name and also retains the reference
and if name is not given then the reference is also their names
'''
print("Dataframe:\n",df1)
print("How much production does in City B?")
print(df1.loc['CityB','Production'])
print(df1.iloc[1,1])

print(df1.iloc[1,:])
print(df1.iloc[1,[0,2]])

print("Whats the total production?")
print(df1['Production'].sum()) # you can use any aggregate function:
# aggfunc: sum() mean() sd(), variance() min() max()..

print("Where clause of SQL:")
print(df1[df1['Fruit'].isin(['Apple','Guava'])])

'''
JOINS On Pandas:

Data is available here:
https://github.com/swapnilsaurav/dataset

Dataset 1: user_device.csv
https://github.com/swapnilsaurav/Dataset/blob/master/user_device.csv

Dataset 2: user_usage.csv
https://github.com/swapnilsaurav/Dataset/blob/master/user_usage.csv

'''
import pandas as pd
user_usage="https://raw.githubusercontent.com/swapnilsaurav/Dataset/refs/heads/master/user_usage.csv"
user_device="https://raw.githubusercontent.com/swapnilsaurav/Dataset/refs/heads/master/user_device.csv"
common_col = "use_id"

user_usage_df = pd.read_csv(user_usage)
print("Dataframe: ",user_usage_df)
print("top 5 rows:\n",user_usage_df.head()) #default value gives 5 rows
print("last 3 rows:\n",user_usage_df.tail(3))
print("Number of rows and columns: ",user_usage_df.shape)  # (rows,cols) (240, 4)
print("Total rows = ",user_usage_df.shape[0])
print("Different column types: \n",user_usage_df.info())
print("Basic Statistics: \n",user_usage_df.describe())

# user_device
user_device_df = pd.read_csv(user_device)
print("Dataframe: ",user_device_df)
print("top 5 rows:\n",user_device_df.head()) #default value gives 5 rows
print("last 3 rows:\n",user_device_df.tail(3))
print("Number of rows and columns: ",user_device_df.shape)  # (rows,cols) (272, 6)
print("Total rows = ",user_device_df.shape[0])
print("Different column types: \n",user_device_df.info())
print("Basic Statistics: \n",user_device_df.describe())

# JOIN = Merge() function of Pandas will help in joining these tables
result_inner = pd.merge(user_usage_df, user_device_df,
on=common_col)  # how="inner" - default
print(result_inner)
print(result_inner.shape)  # [159 rows x 9 columns]

result_left = pd.merge(user_usage_df, user_device_df,
on=common_col, how="left")  # how="inner" - default
print(result_left)
print(result_left.shape)  # [240 rows x 9 columns]

result_right = pd.merge(user_usage_df, user_device_df,
on=common_col, how="right")  # how="inner" - default
print(result_right)
print(result_right.shape)  # [272 rows x 9 columns]

result_full = pd.merge(user_usage_df, user_device_df,
on=common_col, how="outer")  # how="inner" - default
print(result_full)
print(result_full.shape)  # [353 rows x 9 columns]
# 272 + 240 - 159

'''
Practicing Visualization using Seaborn

Data is available here:
https://github.com/swapnilsaurav/dataset

Dataset 1: Iris.csv
https://github.com/swapnilsaurav/Dataset/blob/master/Iris.csv

More about the flower and the dataset:
https://en.wikipedia.org/wiki/Iris_flower_data_set

'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_link="https://raw.githubusercontent.com/swapnilsaurav/Dataset/refs/heads/master/Iris.csv"

df = pd.read_csv(df_link)
print("Dataframe: ",df)
print("top 5 rows:\n",df.head()) #default value gives 5 rows
print("last 3 rows:\n",df.tail(3))
print("Number of rows and columns: ",df.shape)  # (rows,cols) (240, 4)
print("Total rows = ",df.shape[0])
print("Different column types: \n",df.info())
print("Basic Statistics: \n",df.describe())

print("Checking for missing values: ")
print(df.isnull().sum())

print("Want to check for unique species value:")
print(df.drop_duplicates(subset="Species"))

print("Checking if the dataset is balanced or not")
print(df.value_counts('Species'))

print("#####  VISUALIZATION  #####")
print("Count plot for 1 categorical value")
sns.countplot(x="Species",data=df)
plt.title("Count of Each Species")
plt.xlabel("Types of Species")
plt.ylabel("Count of each Species")
plt.savefig("Plot1.png")
plt.show()

print("Check for 1 variable numerical: Histogram")
fig,axes = plt.subplots(nrows=2,ncols=2, figsize=(8,8))
axes[0,0].set_title("SepalLengthCm")
axes[0,0].hist(df['SepalLengthCm'])
axes[0,1].set_title("SepalWidthCm")
axes[0,1].hist(df['SepalWidthCm'])
axes[1,0].set_title("PetalLengthCm")
axes[1,0].hist(df['PetalLengthCm'])
axes[1,1].set_title("PetalWidthCm")
axes[1,1].hist(df['PetalWidthCm'],bins=20)
plt.show()

print("2 variables: Numeric v Numeric Scatter Plot")
sns.scatterplot(data=df,x="PetalLengthCm",y="PetalWidthCm")
plt.show()

sns.scatterplot(data=df,x="PetalLengthCm",y="PetalWidthCm",hue="Species")
plt.title("Numeric v Numeric Scatter Plot")
plt.show()

print("2 variables: Numeric v Categorical")
sns.boxplot(data=df, x="Species",y="PetalLengthCm").set(title="Box and Whisker Plot")
plt.show()

'''
Data Wrangling: Data Preprocessing: Data cleaning
making the data ready for the analysis

Data is available here:
https://github.com/swapnilsaurav/dataset

Dataset 1: hotel_bookings.csv
https://github.com/swapnilsaurav/Dataset/blob/master/hotel_bookings.csv

'''
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df_link="https://raw.githubusercontent.com/swapnilsaurav/Dataset/refs/heads/master/hotel_bookings.csv"

df = pd.read_csv(df_link)
print("Dataframe: ",df)
print("top 5 rows:\n",df.head()) #default value gives 5 rows
print("last 3 rows:\n",df.tail(3))
print("Number of rows and columns: ",df.shape)  # (rows,cols) [119390 rows x 33 columns]
print("Total rows = ",df.shape[0])
print("Different column types: \n",df.info())
print("Basic Statistics: \n",df.describe())

print("Checking for missing values: ")
print(df.isnull().sum())


# We will work on this next week


'''
# Data Analysis has to be done only after data cleaning:
# We need to handle the missing values
print("Want to check for unique country value:")
df2 = df.drop_duplicates(subset="country")
print(df2["country"])

print("Checking if the dataset is balanced or not")
print(df.value_counts('Species'))

print("#####  VISUALIZATION  #####")
print("Count plot for 1 categorical value")
sns.countplot(x="Species",data=df)
plt.title("Count of Each Species")
plt.xlabel("Types of Species")
plt.ylabel("Count of each Species")
plt.savefig("Plot1.png")
plt.show()

print("Check for 1 variable numerical: Histogram")
fig,axes = plt.subplots(nrows=2,ncols=2, figsize=(8,8))
axes[0,0].set_title("SepalLengthCm")
axes[0,0].hist(df['SepalLengthCm'])
axes[0,1].set_title("SepalWidthCm")
axes[0,1].hist(df['SepalWidthCm'])
axes[1,0].set_title("PetalLengthCm")
axes[1,0].hist(df['PetalLengthCm'])
axes[1,1].set_title("PetalWidthCm")
axes[1,1].hist(df['PetalWidthCm'],bins=20)
plt.show()

print("2 variables: Numeric v Numeric Scatter Plot")
sns.scatterplot(data=df,x="PetalLengthCm",y="PetalWidthCm")
plt.show()

sns.scatterplot(data=df,x="PetalLengthCm",y="PetalWidthCm",hue="Species")
plt.title("Numeric v Numeric Scatter Plot")
plt.show()

print("2 variables: Numeric v Categorical")
sns.boxplot(data=df, x="Species",y="PetalLengthCm").set(title="Box and Whisker Plot")
plt.show()
'''






