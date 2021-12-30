# Terrence Paz
# Learn Python 3 the Hard Way
# Exercise 29
# December 29, 2021

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! the world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The wolrd is drolled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5  # this is x = x + 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")