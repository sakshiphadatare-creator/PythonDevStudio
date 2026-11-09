#Pandas
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
print(pd.__version__)

# series , dataframe and panel
l1 = [10,20,'Pune','ICCS']
s1 = pd.Series(l1)
print(s1)
print(type(l1))

#indexing
s1 = pd.Series(l1,index=['a','b','c','d'])
print(s1)
print(type(l1))

#Slicing the series
d = {'a':1,'b':2,'c':3,'d':4}  #convert dictionary into series
s2 = pd.Series(d)
print(s2)

s2[1:4]
s2.min()
s2.max()

#DataFrame

l1 = [[1,2,3],[4,5,6],[7,8,9]]
d1 = pd.DataFrame(l1)
print(d1)

#from list of dictionary
l2 = [{'a':1,'b':2},{'a':3,'b':4}]
d2 = pd.DataFrame(l2)
print(d2)

#Access the file
df = pd.read_csv("./student_result.csv")
print(df)

df.shape
df.info()
df.describe()

#Boxplot for check the outliers
sns.boxplot(df['Percentage'])
