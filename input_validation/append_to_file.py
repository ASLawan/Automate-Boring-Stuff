#!/usr/bin/python3

FILE = input("Enter file to append to: ")

file_handle = open(FILE, "a")

file_handle.write("i just got appended here!")

file_handle.close()
