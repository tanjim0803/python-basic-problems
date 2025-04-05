# Write a Python program to do arithmetical operations addition and division.

# addition
num1 = float(input("Enter the first number for addition: "))
num2 = float(input("Enter the second number for addition: "))

addition = num1 + num2

print(f"Sum: {num1} + {num2} = {addition}")

# division
num3 = float(input("Enter the first number for division: "))
num4 = float(input("Enter the second number for division: "))

if num3 == 0 or num4 == 0:
    print("Error: Division zero is not allowed.")
else:
    division = num3 / num4
    print(f"Division: {num3} + {num4} = {division}")