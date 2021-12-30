# Terrence Paz
# Learn Python 3 the Hard Way
# Exercise 31
# December 29, 2021

print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats ytour face off.  Good Job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good Job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    instanity = input("> ")

    if instanity == "1" or instanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else: 
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die.  Good Job!")





