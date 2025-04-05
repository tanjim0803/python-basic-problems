# Write a Python Program to Check if a Number is Odd or Even.

num = int(input("Enter a number: "))

flag = True

i = 2

while i <= num/2:
    if num % i == 0:
        flag = False
        break
    i = i+1
    
if (num == 0 or num == 1) or flag == False:
    print(f"The number {num} is not a prime number.")
else: 
    print(f"The number {num} is a prime number.")