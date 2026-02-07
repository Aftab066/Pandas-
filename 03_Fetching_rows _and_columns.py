import pandas as pd

df = pd.read_excel("Demo.xlsx") #Path Of file

print(df.head(2)) #Shows n No Of First Rows
print(df.tail(2)) #Shows n No Of Last Rows
