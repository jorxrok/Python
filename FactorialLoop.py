# Write a program to calculate the factorial of a number using loops.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

number = int(input("Enter a number: "))
print(f"The factorial of {number} is: {factorial(number)}")
