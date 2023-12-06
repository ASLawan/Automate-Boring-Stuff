#!/usr/bin/python3
from random import randint

print("Welcome to number guessing game!")

secret_num = randint(1, 20)
print("I've thought of a number between 1 and 20")

for guesses in range(1, 6):
    print("Guess my number: ")
    guess = int(input())

    if guess > secret_num:
        print("Your guess is higher")
    elif guess < secret_num:
        print("Your guess is lower")
    else:
        break

if guess == secret_num:
    print("Good job!")
    print("You did it in {} guesses".format(guesses))
else:
    print("Oopse!")
    print("My number is {}". format(secret_num))

