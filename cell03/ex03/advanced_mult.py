#!/usr/bin/env python3
import sys
try:
    i = 0
    j = 0
    while i <= 10:
        print("Table de",i,end=": ")
        while j <= 10:
            print(i*j,end=" ")
            j += 1
        print()
        j = 0
        i += 1
except (IndexError, ValueError):
    print("none")