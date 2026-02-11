import pandas as pd

data = {
    "Name" : ['Aftab', 'Ismail','Parvej','Omkar'],
    "Roll No": [9079,9080,9085,9070],
    'Age' : [16,18,20,None],
    "Marks" :[100,90,80,23]
}

df = pd.DataFrame(data)
missing = df.isnull().sum() #Gives Count Of Missing Values In Every Column
missing = df.isnull() #Gives Boolean Data Of  Missing Values In Every Column
remove_nan = df.dropna() #Deletes The Row Which Have Missing Values 
fill = df.fillna(1) #Fills Missing values with specific number given
fill = df['Age'].fillna(df['Age'].mean()) #Fills With Mean Of That Column
print(fill)