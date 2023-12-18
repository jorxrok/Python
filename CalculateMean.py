# Write a function to calculate the arithmetic mean of a variable number of values:
def calculate_mean(*values):
    return sum(values) / len(values)

result = calculate_mean(10, 20, 30, 40, 50)
print("Arithmetic mean:", result)
