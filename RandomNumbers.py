# Write a program to randomly select 10 integer elements from the range 100 to 200 and find the smallest among all.
import random
random_numbers = [random.randint(100,200) for _ in range(10)]
print(random_numbers)
smallest_number = min(random_numbers)
print('The smalles number in this list of random numbers is :' , smallest_number)