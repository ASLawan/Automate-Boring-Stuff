#!/usr/bin/python3
from random import randint
import sys

print("Welcome to Rock, Paper, Scissors Game!")
wins = 0
losses = 0
ties = 0

while True:
    print("{} Wins {} Losses {} Ties".format(wins, losses, ties))
    while True:
        print("Enter your move: (r)ock, (p)aper, (s)cissor or (q)iut")
        p_choice = input()
        if p_choice == 'q':
            print("Thank for playing!")
            sys.exit()
        if p_choice == 'r' or p_choice == 'p' or p_choice == 's':
            break
        print("Enter r, p, s or q")

    if p_choice == 'r':
        print("ROCK versus...")
    elif p_choice == 'p':
        print("PAPER versus...")
    elif p_choice == 's':
        print("SCISSORS versus...")

    num = randint(1, 3)
    if num == 1:
        c_choice = 'r'
        print("ROCK")
    elif num == 2:
        c_choice = 'p'
        print("PAPER")
    elif num == 3:
        c_choice = 's'
        print("SCISSORS")

    if p_choice == c_choice:
        print("It is a tie!")
        ties += 1
    elif p_choice == 'r' and c_choice == 's':
        print("You win!")
        wins += 1
    elif p_choice ==  'p' and c_choice == 'r':
        print("You win!")
        wins += 1
    elif p_choice == 's' and c_choice == 'p':
        print("You win!")
        wins += 1
    elif p_choice == 'r' and c_choice == 'p':
        print("You lose!")
        losses += 1
    elif p_choice ==  'p' and c_choice == 's':
        print("You lose!")
        losses += 1
    elif p_choice == 's' and c_choice == 'r':
        print("You lose!")
        losses += 1


