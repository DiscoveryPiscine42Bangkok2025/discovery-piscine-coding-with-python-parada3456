#!/usr/bin/env python3

def array_of_names(dict1):
    arr= []
    for name in dict1:
        arr.append(name + " " + str(dict1[name]))
    return arr

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))
