# Terrence Paz
# Learn Python 3 the Hard Way
# Exercise 14
# December 4, 2021

# Run this program using the cmd prompt and type in python Exercise_14.py Zed
# the Zed can be replaced with anything.

# Getting a SyntaxError even though all the instructions are being followed.

from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}, I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}.  Not sure where that is.
And you avhe a {computer} computer.  Nice.
""")