# 5	Write a program that takes a sentence as input, replaces each blank with a hyphen, and prints the modified sentence.
sentence = input("Enter a sentence withsome blank spaces: ")
modified_sentence = sentence.replace(" ","-")
print(f"Modified Sentence is {modified_sentence}")