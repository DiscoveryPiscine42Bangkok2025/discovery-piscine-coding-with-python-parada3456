#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("none")
else:
    flag = -1
    for i in sys.argv[1]:
        if i == "z":
            flag = 1
            print(i,end="")
    
    if flag == -1:
        print("none")
    elif flag == 1:
        print()