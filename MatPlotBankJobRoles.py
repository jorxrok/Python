import pandas as pd
import matplotlib.pyplot as plt

# Create a bar chart using Matplotlib that displays the distribution of different job roles in the bank marketing dataset.
df = pd.read_csv('bank_marketing.csv')


job_distribution = df['job'].value_counts()
plt.figure(figsize=(10, 6))
job_distribution.plot(kind='bar', color='skyblue')
plt.title('Distribution of Job Roles in Bank Marketing Dataset')
plt.xlabel('Job Roles')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
plt.tight_layout()

# Show the plot
plt.show()