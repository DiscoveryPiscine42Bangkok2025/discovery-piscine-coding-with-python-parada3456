#!/usr/bin/env python3
import sys

def shrink(str1):
    print(str1[:8])

def enlarge(str1):
    print(str1+"Z"*(8-len(str1)))

if len(sys.argv) < 2 :
    print("none")
else:
    for param in sys.argv[1:]:
        if len(param) > 8:
            shrink(param)
        elif len(param) < 8:
            enlarge(param)
        else :
            print(param)