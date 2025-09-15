#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("none")
else:
    flag = -1
    for i in sys.argv[1:]:
        if "ism" not in i:
            flag = 1
            print(i+"ism")
    
    if flag == -1:
        print("none")