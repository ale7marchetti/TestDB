#!/usr/bin/env python3

lst = []
rg = 0

with open("0199voci.csv", "r") as file:
    for line in file:
        rg += 1
        lst.insert(rg, line.split(";"))
        if rg == 50:
            break


print(lst[0])
print(lst[1])
