# Create a Python program to catch multiple exceptions in a single block.
try:
    x = int(input("Enter a number: "))
    y = 0
    result = x / y
except (ValueError, ZeroDivisionError) as e:
    print(f"Error: {e}")
