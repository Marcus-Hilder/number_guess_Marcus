import random
tries = 0
def callint():
    x = random.randrange(0, 200)
    print(x)  # reveal the number
    return x   
"""
genrates the random number 
""" 
def run():
    b = input("Please enter a number: ")
    try:
        b = int(b)
    except ValueError:
        print("Enter a number, not a string :(") 
        return run()
    return b
"""runs the input part of the game"""
output = callint()
print("Welcome to random Number Guessing Game please enter your guess \nYou have 3 guses \nGood luck")
while tries < 3:
    b = run()
    if output == b:
        print("You win!")
        tries = 10
        # ends the game a

    else:
        print("Try again!")     
    tries += 1 
    

if tries == 3:
    print("You're out of luck!")
