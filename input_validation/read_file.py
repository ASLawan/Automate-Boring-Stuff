#!/usr/bin/python3

FILE = input("Enter file to read from: ")

handle = open(FILE, 'r')

for line in handle:
    for word in line.split():
        print(word)
    print()
