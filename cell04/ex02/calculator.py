#!/usr/bin/env python3
num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))
print("Thank you!")
operator = ["+","-","/","*"]
for i in operator:
    if i == "+":
        result = num1 + num2
    elif i == "-":
        result = num1 - num2
    elif i == "/":
        result = num1 / num2
    elif i == "*":
        result = num1 * num2
    print(num1, i, num2, "=", result)