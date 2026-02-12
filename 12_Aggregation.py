import pandas as pd

data = {
    "Name" : ['Aftab', 'Ismail','Parvej','Aftab'],
    "Roll No": [9079,9080,9085,9070],
    'Age' : [16,18,20,None],
    "Marks" :[100,90,80,23],
    'Salary' :[10000,20000,30000,40000],
    'Bonus' :[20000,40000,60000,80000]
}

df = pd.DataFrame(data)

#Mean Of Rows
mn = df['Marks'].mean()
#Sum Of Rows
sn = df['Marks'].sum()
#Max/Min 
mx = df['Marks'].max()
sm = df['Marks'].min()

#Groupby : Means Group The Data And Perform Operations On it
gp = df.groupby('Name')['Salary'].sum()
print(gp)
#Groupby Data Ko Same Data Ko Group Karta Hai Aur unme operations karta hai!!