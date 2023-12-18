import pandas as pd

# Load the dataset
# Assuming the dataset is named 'Bankmarketing.csv'
df = pd.read_csv('bank_marketing.csv')

# Drop the "Unnamed: 0" column
df = df.drop(columns=['Unnamed: 0'], errors='ignore')

# Drop missing values
df = df.dropna()

# Remove duplicated rows
df = df.drop_duplicates()

# Display the shape of the resulting dataframe
print("Shape of the dataframe after preprocessing:", df.shape)
