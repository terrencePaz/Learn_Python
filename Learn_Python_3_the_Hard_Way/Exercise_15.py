# Terrence Paz
# Learn Python 3 the Hard Way
# Exercise 15
# December 4, 2021


# Getting a SyntaxError even though all the instructions are being followed.

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.readu())

