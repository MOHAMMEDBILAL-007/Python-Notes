import pandas as pd
df = pd.read_csv("D:\learning\Python-study\self learning\Pandas\data.csv")

print(df["Pulse"])
df.sort_values(by = "Pulse",ascending = True,inplace = True)# single column
print(df["Pulse"])

df.sort_values(by = ["Pulse","Maxpulse"],ascending= [True,False],inplace = True)
# one row ascending and one descending
print(df[["Pulse","Maxpulse"]])

# statistics
print("\nsum :",df["Pulse"].sum())
print("\nmean :",df["Pulse"].mean())

print(df.groupby("Duration")["Pulse"].mean())
print(df.groupby(["Duration","Pulse"])["Maxpulse"].mean())

