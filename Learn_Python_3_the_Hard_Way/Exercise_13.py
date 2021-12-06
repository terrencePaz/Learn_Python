# Terrence Paz
# Learn Python 3 the Hard Way
# Exercise 13
# December 4, 2021

# Run this program using the cmd prompt and type in python Exercise_13.py Uno Dos Tres
# the Uno Dos Tres can be replaced with anything but it needs to be three separate items.

from sys import argv
# read the WYSS section for how to run this
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
