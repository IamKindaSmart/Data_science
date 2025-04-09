import pandas as pd
data = pd.read_csv("titanic.csv")

#Get specific columns out of condition
adult_name = data.loc[data["Age"] > 18, "Name"]
print(adult_name)

#slicing - same as numpy 2D slicing
#first data is for rows and second is for columns, follows the same syntax as range function
print(data.iloc[9:19, 0:4])

#changing the value in the dataset
#specify the number of rows and the particular column to change
data.iloc[0:3, 2] = "Rishab Naidu"
print(data["Name"])

#save the data to local file
data.to_csv("titanic_updated.csv")

#creating a new column in dataframe
data["test"] = data["Fare"] + 2
data["test2"] = data["Fare"] * data["Pclass"]

print(data.head())


#renaming the column
data_renamed = data.rename(
    columns={
        "Pclass": "Passenger Class",
        "SibSp": "Sibling"
    }
)
print(data_renamed.info())

#performing mathematical operation on multiple columns
print(data["Age"].mean())
print(data[["Age","Fare"]].mean())

print(data.agg({
    "Age": ["min", "max", "median"],
    "Fare": ["min", "max", "median"]
}))

#group the data categorically
print(data[["Sex", "Age"]].groupby("Sex").mean())
print(data.groupby("Sex")["Age"].mean())

#task - get the mean ticket price for each of sex and cabin class combination
# average_ticket = print(data.agg({
#     "Pclass": ["min", "max", "mean"],
#     "Sex": ["min", "max", "mean"]
# }))

print(data.groupby(["Sex", "Pclass"])["Fare"].mean())