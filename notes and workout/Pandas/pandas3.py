import pandas as pd
df = pd.read_csv("D:\learning\Python-study\self learning\Pandas\data.csv")
print(df.head())
# this is a direct method
df["Bill"] = [el*1000 for el in range(0,32)]# Adds the column at the end of the dataset
print(df.head())

# using insert method
df.insert(0,"Id",[f"Hos{i}" for i in range(0,32)])# places the column in the 0 th index of the dataset
print(df.head())

# value modify
df.loc[22,"Date"] = "'2020/12/22'"
print(df.head())

# updating an entair column
df["Pulse"] = df["Pulse"]*1

# drop column
df.drop(columns=["Id","Bill"],inplace= True)
print(df.head())

# missing values detecting
print(df.isnull())
# or
print(df.isnull().sum())

# filling missing values
df.fillna(df["Calories"].mean(),inplace = True)

print(df)