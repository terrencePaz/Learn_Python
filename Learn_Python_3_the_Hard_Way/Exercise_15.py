# Terrence Paz
# Learn Python 3 the Hard Way
# Exercise 15
# December 4, 2021
# Updated 12/27/2021


# to run this program within the cmd window type in python Exercise_15.py ex15_sample.txt
# When the program asks you to retype in the filename type in ex15_sample.txt

from sys import argv

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again: ")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

