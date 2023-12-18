# Write a Python function to find the sum of digits of a number using recursion
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

number = int(input("Enter a number: "))
print(f"Sum of digits: {sum_of_digits(number)}")
