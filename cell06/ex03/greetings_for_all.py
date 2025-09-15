#!/usr/bin/env python3
def greetings(name = "noble stranger"):
    if type(name) == str:
        print("Hello,",name+".")
    else :
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
