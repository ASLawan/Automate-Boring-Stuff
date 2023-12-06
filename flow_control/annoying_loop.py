#!/usr/bin/python3

name = ''
count = 0
while name != 'your name':
    print("Please type your name: ")
    name = input()
    count += 1

print("Bingo!")
print("It took you " + str(count) + " trials!")
