#!/usr/bin/python3

def print_picnic(picnic_items, lwidth, rwidth):
    print("PICNIC ITEMS".center(lwidth + rwidth, '-'))
    for k, v in picnic_items.items():
        print(k.ljust(lwidth, '.') + str(v).rjust(rwidth))


picnic_items = {"Pancakes": 10, "Apples": 20, "Cups": 10, "Cookies": 8000, "Heineken": 20, "Juice": 10}
print_picnic(picnic_items, 12, 5)
print_picnic(picnic_items, 20, 6)
