#!/usr/bin/env python3
import sys
import re

if len(sys.argv) != 3:
    print("none")
else:
    count = sys.argv[2].count(sys.argv[1])
    # matches = re.findall(sys.argv[1],sys.argv[2])
    # count = len(matches)
    if count == 0:
        print("none")
    else :
        print(count)
    