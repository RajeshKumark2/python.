import pandas as pd 
data  = {'Name': ['Rajesh','Kumar'], 'Age': [24, 23]}
df = pd.DataFrame(data)
print(df[df['Age'] > 20 ])
