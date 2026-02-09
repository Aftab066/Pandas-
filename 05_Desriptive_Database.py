import pandas as pd

data = {
    "Name" : ['Aftab', 'Ismail','Parvej'],
    "Roll No": [9079,9080,9085],
    "Marks" :[100,90,80]
}

df = pd.DataFrame(data)
print(df.describe()) #Data In Descriptive Statistics