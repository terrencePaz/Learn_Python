# Terrence Paz
# Learn Python 3 the Hard Way
# Exercise 17
# December 4, 2021
# Updated 12/27/2021

# This program copies the data from one file and paste it into another file.
# To run in the cmd window type python Exercise_17.py text.py text2.py

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done. ")

out_file.close()
in_file.close()
