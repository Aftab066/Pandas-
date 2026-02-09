import pandas as pd

data = {
    "Name" : ['Aftab', 'Ismail','Parvej'],
    "Roll No": [9079,9080,9085],
    "Marks" :[100,90,80]
}

df = pd.DataFrame(data)

print(f"Shape : {df.shape}") #Gives Total Rows And Columns (3,4) First one indicate row and second column
print(f"Column Names : {df.columns}") #Column Names

#It Gives Data In Form Of tuple
