import pandas as pd

data={
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'percentage':[90, 85, 88, 92],
}

#create a DataFrame - tabular information
dataframe=pd.DataFrame(data)
print(dataframe)

#conditional selection of elements from DataFrame
high_scores=dataframe[dataframe['percentage']>90]
print(high_scores)

#get people with age greater than 30
age_30=dataframe.loc[dataframe['Age']>30,'Name']
print(age_30)