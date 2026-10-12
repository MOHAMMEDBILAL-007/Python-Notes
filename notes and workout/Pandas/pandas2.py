import pandas as pd

df = pd.read_csv("D:/learning/self learning/Pandas/New_data.csv")
print("dataframe created ...")
print("\nfirst 5 rows")
print(df.head())

print("\nlast 5 rows")
print(df.tail())

print("\ndisplaying the info of the data set")
print(df.info())

print("\nDiscription of teh dataset")
print(df.describe())

print("\nshape of the dataset")
print(df.shape)

print("\ncolumns of the dataset")
print(df.columns)

# data manipulation

# accessing a specific column
print(df["name"])# single column 
#for multiple columns
print(df[["age","place"]])

# filter rows
adult = df[df["age"]>18]# only 1 condition
print(adult)

eastblueadults = df[(df["age"]>18 )&( df["place"]=="eastblue")]
print(eastblueadults)