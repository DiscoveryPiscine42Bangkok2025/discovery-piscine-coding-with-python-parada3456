#!/usr/bin/env python3
num1 = int(input("Enter the first number:\n"))
num2 = int(input("Enter the second number:\n"))
mult = num2*num1
print(num1, "x", num2, "=",mult)
if mult > 0 :
    print("The result is positive.")
elif mult < 0 :
    print("The result is negative.")
else:
    print("The result is positive and negative.")