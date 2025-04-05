# Write a Python Program to Check if a Number is Positive, Negative or Zero.

num = float(input("Enter a number: "))

if num == 0:
    print("The input number is Zero.")
elif num > 0:
    print(f"The input number {num} is a Positive number.")
else:
    print(f"The input number {num} is a Negative number.")