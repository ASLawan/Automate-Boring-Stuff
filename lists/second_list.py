#!/usr/bin/python3
import random


def generate_list():
    outcomes = []

    for outcome in range(100):
        if outcome == 0:
            outcomes.append('H')
        else:
            outcomes.append('T')
    return outcomes

def check_streak(outcomes):
    heads = 0
    tails = 0
    streak_6 = 0

    for outcome in outcomes:
        if outcome == 'H':
            heads += 1
            tails = 0
        else:
            tails += 1
            heads = 0

        if heads == 6 or tails == 6:
            streak_6 += 1
    
    return streak_6

def main():
    
    for _ in range(100000):
        outcomes = generate_list()

        streak = check_streak(outcomes)

    print("Chance of streak: {}%".format(streak/100))
   


main()
