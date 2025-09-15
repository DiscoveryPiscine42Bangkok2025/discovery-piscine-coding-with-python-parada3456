#!/usr/bin/env python3
arr = [2,8,9,48,8,22,-12,2]
new_arr = [a + 2 for a in arr if a > 5]
print("Original array:",arr)
print("New array:",new_arr)
