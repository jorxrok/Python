# /Create a scatter plot using Matplotlib to examine the relationship between account balance and the last contact duration.   Use Bankmarketing.csv
import pandas as pd
import matplotlib.pyplot as plt

# Create a bar chart using Matplotlib that displays the distribution of different job roles in the bank marketing dataset.
df = pd.read_csv('bank_marketing.csv')

account_balance = df['balance']
last_contact_duration = df['duration']


plt.figure(figsize=(10, 6))
plt.scatter(account_balance, last_contact_duration, color='green', alpha=0.5)
plt.title('Scatter Plot: Account Balance vs. Last Contact Duration')
plt.xlabel('Account Balance')
plt.ylabel('Last Contact Duration (seconds)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()

# Show the plot
plt.show()