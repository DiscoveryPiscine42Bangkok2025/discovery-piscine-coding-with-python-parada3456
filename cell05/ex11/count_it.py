#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("none")
else:
    n = len(sys.argv)
    print("parameters:",n)
    for i in sys.argv[1:]:
        print(i+":",len(i))