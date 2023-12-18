# 24	Write a function that checks whether a passed string is a palindrome or not.
def is_palindrome(s):
    return s == s[::-1]

word = input("Enter a string: ")
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
