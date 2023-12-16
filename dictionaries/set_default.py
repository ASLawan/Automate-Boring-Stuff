#!/usr/bin/python3
import pprint

message = "It was a bright cold day in June, and the clocks were striking thirteen."

count = {}

for xter in message:
    count.setdefault(xter, 0)
    count[xter] += 1 

pprint.pprint(count)
