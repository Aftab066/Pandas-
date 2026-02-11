import pandas as pd

data = {
    "Name" : ['Aftab', 'Ismail','Parvej','Omkar'],
    "Roll No": [9079,9080,9085,9070],
    'Age' : [16,18,20,None],
    "Marks" :[100,90,80,23]
}

df = pd.DataFrame(data)
# sr = df.sort_values(by='Name') # Sorts The Data In Given Column By Default Order In Ascending
sr = df.sort_values(by='Name',ascending = False) # Sorts The Data In Given Column In Descending Order
print(sr)