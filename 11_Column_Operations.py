import pandas as pd

data = {
    "Name" : ['Aftab', 'Ismail','Parvej','Omkar'],
    "Roll No": [9079,9080,9085,9070],
    'Age' : [16,18,20,None],
    "Marks" :[100,90,80,23]
}

df = pd.DataFrame(data)
#Creating A Column
new = df['Salary'] = [10000,20000,30000,40000] #Creating A Column 
new = df['Bonus'] = df['Salary'] * 2  #Creating A Column 
new = df['Total'] = df['Salary'] + df['Bonus'] #Creating A Column 
find = df[df['Total'] > 100000]

#Rename A Column
name = df.rename(columns={'Marks': 'Grade'}, inplace = True)
#Rename Multiple Columns
name = df.rename(columns={'Marks': 'Grade',
                          'Salary': 'Big One'}, inplace = True)
#inplace Is Used To Change it in OG Directory 

#  Delete A Column
dell = df.drop('Grade', axis=1)
print(dell) # Deletes The Column And Returns A Copy Of Dataframe

# print(new)
# print(df)