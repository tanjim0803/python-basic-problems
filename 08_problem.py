# Write a Python program to swap two variables without temp variable.

num1 = float(input("Enter the num1: "))
num2 = float(input("Enter the num2: "))

num1, num2 = num2, num1

print(f"After swapping: num1 = {num1} & num2 = {num2}.")