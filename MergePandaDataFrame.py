# Develop a program to merge two Pandas DataFrames.
import pandas as pd

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})

merged_df = pd.concat([df1, df2], ignore_index=True)
print("Merged DataFrame:\n", merged_df)
