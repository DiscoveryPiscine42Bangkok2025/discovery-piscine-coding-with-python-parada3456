#!/usr/bin/env python3
import sys
def downcase_it(str1):
    return str1.lower()

if len(sys.argv) > 1:
    print("none")
else:
    for i in sys.argv[1:]:
        print(downcase_it(i))