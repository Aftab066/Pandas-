import pandas as pd

data = {
    "Name" : ['Aftab', 'Ismail','Parvej'],
    "Roll No": [9079,9080,9085],
    'Age' : [16,18,20],
    "Marks" :[100,90,80]
}

df = pd.DataFrame(data)
# print(df["Name"]) #Selecting Single Column
# print(df[['Name','Marks']]) #Selecting Multiple Columns

#Filtering Columns 

# print(df[df['Marks']>90]) #Filttering Columns By A Condition
print(df[(df['Marks']> 80) & (df['Age'] > 14)])