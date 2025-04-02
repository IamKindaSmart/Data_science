import pandas as pd

dataframe=pd.DataFrame({
"Name": ['John', 'Anna', 'Peter', 'Linda'],
"Age": [28, 24, 35, 32],
'city': ['New York', 'Paris', 'Berlin', 'London']})

print(dataframe.head()) # Display the first 5 rows of the DataFrame
print(dataframe.shape)

print(dataframe["Name"])

print(dataframe["Age"].max())
print(type[dataframe["Age"]])
print(dataframe["Age"].shape)

print(dataframe.info())
print (dataframe.describe())

#load the data file
data = pd.read_csv("titanic.csv")
print(data.head())
print(data.info())
print(data.dtypes)

#selecting multiple columns together
NameAgeData = data[["Name", "Age"]]
print(NameAgeData.head())
print(NameAgeData.shape)