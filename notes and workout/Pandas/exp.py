import pandas as pd

df = pd.DataFrame({
    "Id": [12,19,20,20,5,34,45,28,23],
    "name": ["luffy","nami","zoro","sanji","chopper","brook","jimbe","robin","frankie"],
    "shoping":[2021,2023,2020,2021,2024,2016,2025,2019,2024]
})

df2 = pd.read_csv("D:/learning/Python-study/self learning/Pandas/New_data.csv")

print(df.head())
print(df.tail())

print(df.info())

print(df.describe())

print(df.shape)
print(df.columns)

print(df[["Id","name"]])

print(df[df["Id"]<18])

df["bounty"]=[12223,121212,323231,3241231,21312312,32313123,231,2133123,123112]
print(df.head())

df.drop(columns="bounty",inplace = True)

print(df.head())

df.insert(3,"bounty",[123323,123231,324234,324231,234234,234234,34241,231311,None])
print(df.head())
df.loc[4,"name"]="tony"
print(df.head())

print(df.isnull().sum())

df.dropna(axis = 0 ,inplace = True)
print(df.tail())

df.sort_values(by = "bounty",inplace = True)
print(df)

ndf = df.groupby("shoping")["bounty"].mean()
print(ndf)

df.loc[2,"bounty"]=None
print(df)

df["bounty"]=df["bounty"].interpolate(method="linear")
print(df)