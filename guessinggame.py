import random
actual = random.randint(1, 99)
guess = int(input("Guess a number between 1 and 99:"))
while actual != guess:
    print
    if guess < actual:
        print ("Your guess is too low!")
        guess = float(input("Enter an integer from 1 to 99:"))
    elif guess > actual:
        print ("Your guess is too high!")
        guess = float(input("Enter an integer from 1 to 99:"))
    else:
        print ("You guessed it!")
        break
    print

