#!/usr/bin/python3

table = [
        ['apples', 'oranges', 'cherries', 'banana'],
        ['Alice', 'Bob', 'Carol', 'David'],
        ['dogs', 'cats', 'moose', 'goose']
        ]

def print_table(table):
    colwidths = []
    for list in table:
        largest = len(list[0]);
        for item in list:
            if len(item) > largest:
                largest = len(item)
        colwidths.append(largest)
    
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(colwidths[j]), end='  ')
        print()


print_table(table)
            

