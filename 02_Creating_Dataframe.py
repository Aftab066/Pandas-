import pandas as pd

data = {
    "Name" : ['Aftab', 'Ismail','Parvej'],
    "Roll No": [9079,9080,9085],
    "Marks" :[100,90,80]
}

df = pd.DataFrame(data) # Creating Dataframe
df.to_excel("Demo.xlsx",index=False) #Saves File In Given Format
print(df)