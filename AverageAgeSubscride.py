import pandas as pd

# Load the dataset
df = pd.read_csv('bank_marketing.csv')

# Filter the dataset to include only clients who have subscribed to a deposit (assuming the deposit subscription information is in a column named 'y')
subscribed_clients = df[df['deposit'] == 'yes']

# Calculate the average age of subscribed clients
average_age_subscribed = subscribed_clients['age'].mean()

print(f"The average age of clients who have subscribed to a deposit is: {average_age_subscribed:.2f} years")
