# import math
# print(f"The GCD of {num1} & {num2} is :", end =" "  )
# print(math.gcd(num1, num2))

#This program is for find the gcd of two numbers
num1 = int(input("Inter the first number :"))
num2 = int(input("Inter the second number :"))

if num2>num1:
    mn = num1
else:
    mn = num2

for i in range(1, mn+1):
    if num1 % i == 0 and num2 % i == 0:
        hcf = i

print(f"The hcf/GCD of {num1} and {num2} is {hcf}")