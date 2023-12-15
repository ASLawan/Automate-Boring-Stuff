#!/usr/bin/python3

def display_list(items):
    if items == "[]":
        return "[]"
    else:
        for i in range(len(items)):
            if i == len(items) - 1:
                print("and {}".format(items[i]))
            else:
                print("{}, ".format(items[i]), end='')


names = ['Lawan', 'Austin', 'Sewoyebaa', 'Nawal', 'Nitsua']

display_list(names)
