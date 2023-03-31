# read excel/csv data
import pandas as pd
df = pd.read_excel('Book1.xlsx')
print(df)

#write excel/csv data
df.to_excel("copy.xlsm", sheet_name="Book1")