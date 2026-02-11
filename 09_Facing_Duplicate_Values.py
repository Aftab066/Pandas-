import pandas as pd

data = {
    "Name" : ['Aftab', 'Omkar','Parvej','Omkar'],
    "Roll No": [9079,9079,9085,9079],
    'Age' : [16,18,20,18],
    "Marks" :[100,100,80,100]
}

df = pd.DataFrame(data)
# print(df)
# dup = df.duplicated().sum() #If Whole  Row Is Duplicated Then It Will Show True
# dup = df.drop_duplicates() #Deletes Duplicated Rows 
print(dup)
