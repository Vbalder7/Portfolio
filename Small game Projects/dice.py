import random

d4 = str(random.randint(1, 4))
d6 = str(random.randint(1, 6))
d8 = str(random.randint(1, 8))
d10 = str(random.randint(1, 10))
d12 = str(random.randint(1, 12))
d20= str(random.randint(1, 20))
d100 = str(random.randint(1, 100))

def Roller():
    roll = input("Which dice would you like to roll: ")
    if roll == "d4":
        print("You rolled a " + d4)
    elif roll == "d6":
        print("You rolled a " + d6)
    elif roll == "d8":
        print("You rolled a " + d8)
    elif roll == "d10":
        print("You rolled a " + d10)
    elif roll == "d12":
        print("You rolled a " + d12)
    elif roll == "d20":
        print("You rolled a " + d20)
    elif roll == "d100":
        print("You rolled a " + d100)
    else:
        print("That was an invalid Input.")
        roll = input("Which dice would you like to roll: ")
        return

Roller()