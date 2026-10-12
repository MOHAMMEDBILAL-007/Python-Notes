import pandas as pd
# creating a data frame 
df = pd.read_csv("D:\learning\self learning\Pandas\data.csv")
print(df)

# lets create a dataframe using a dictionary

new_data = {
    "name":["luffy","zoro","sanji"],
    "age":[17,19,19],
    "place":["east blue","east blue","east blue"]
}

dfn = pd.DataFrame(new_data)# when we create the data frame like this the system will assign index to every row as a new collumn
print(dfn)
dfn.to_csv("New_data.csv",index = False)# do index = false if you dont want index column
dfn.to_excel("new_data.xlsx")
dfn.to_json("newjson.json")