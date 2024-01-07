#!/usr/bin/python3

FILE = input("Enter file to read from: ")

handle = open(FILE, 'r')

for line in handle.readlines():
    print(line)
