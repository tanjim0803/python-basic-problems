# Write a Python program to swap two variables.

num1 = float(input("Enter the num1: "))
num2 = float(input("Enter the num2: "))

temp = num1
num1 = num2
num2 = temp

print(f"After swaping: num1 = {num1} & num2 = {num2}")