
# •	Plot a histogram using Matplotlib to show the age distribution of the individuals in the dataset.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bank_marketing.csv')


ages = df['age']

# Create a histogram using Matplotlib
plt.figure(figsize=(10, 6))
plt.hist(ages, bins=20, color='skyblue', edgecolor='black')  # Adjust the number of bins as needed
plt.title('Age Distribution of Individuals in Bank Marketing Dataset')
plt.xlabel('Age')
plt.ylabel('Count')
plt.grid(axis='y', alpha=0.75)
plt.tight_layout()

# Show the plot
plt.show()