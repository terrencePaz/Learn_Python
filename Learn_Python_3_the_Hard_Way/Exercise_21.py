# Terrence Paz
# Learn Python 3 the Hard Way
# Exercise 21
# December 29, 2021

def add(a, b):
    print(f"ADDING {a} + {b}") # Print f allows for formatted strings
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, IQ: {iq}")

# A puzzel for the extra credit, type it in anyway.
print("Here is a puzzle.")
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "can you do it by hand?")

