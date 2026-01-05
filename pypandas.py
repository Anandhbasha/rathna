import pandas as pd

# list
# s1 = pd.Series([10,20,30,40],index=["a","b","c","d"])

# s3 = pd.Series([60,70,80,90])


# print(s1)
# print(s3*2)

# print(s1[s1>30])
# print(s1["a"])


# data = {"name1":"arun","name2":"ajay","name3":"Karthick"}

# s2 = pd.Series(data)
# print(data)
# print(s2)

# Dataframe

# data = {
#     'Name':['Raja','Ravi','Balu'],
#     'Age':[25,32,80],
#     'city':["cbe","erode","salem"]
# }

# df = pd.DataFrame(data)

# print(df)

# df1 = pd.DataFrame(data,index=["x","y","z"])

# print(df1)

data_dict = [
    {"Name":"arun","age":25,"city":"Erode"},
    {"Name":"ajay","age":25,"city":"CBE"},
    {"Name":"Bala","age":25,"city":"Salem"},
]



dfList = pd.DataFrame(data_dict)
# print(dfList)

# print(dfList.head(2))
# print(dfList.tail(1))
# print(dfList.shape)
# print(dfList.columns)
# # print(dfList.dtypes)
# print(dfList['Name'])
# print(dfList[['Name',"age"]])
dfList["Salary"] = [50000,70000,58000]
# print(dfList)

# # print(dfList[dfList["Salary"]>55000])
# # Sclar Method (at)
# print(dfList.at[0,"Name"])

# # location
# print(dfList.loc[0])
# print(dfList.loc[0:2,"Salary"])

# #isin
# print(dfList[(dfList["Salary"].isin([50000,75000]))])

# print(dfList[(dfList["city"]=="Salem") & (dfList["Salary"]>50000)])

# print(dfList.query("age>22 and Salary<60000"))


# create

# csv

# dfList.to_csv("output.csv",index=False)
# print("Created Succesfully")


# dfList.to_csv("output.csv",index=True)
# print("Created Succesfully")

# csvData = pd.read_csv("output.csv")
# print(csvData.head(1))



dfList.to_excel("output.xlsx",sheet_name="Persons",index=False)
print("Created Succesfully")