#!/usr/bin/python3

birthdays = {'Lawan': 'June 7', 'Laiven': 'June 14', 'Echo': 'Dec 23', 'Muchop': 'Dec 16',
             'Game': 'May 23'
            }

while True:
    print("Enter a name or blank to quit: ")
    name = input()
    if name == "":
        break

    if name in birthdays:
        print("{}'s birthday is on {}".format(name, birthdays[name]))
    else:
        print("I do not have  informat for {}".format(name))
        print("Would you like to add their birthday: (y/n)")
        add = input()
        if add == 'y':
            print("What is their birthday: ")
            bday = input()
            birthdays[name] = bday
            print("Birthdays database updated!")
        else:
            quit()
