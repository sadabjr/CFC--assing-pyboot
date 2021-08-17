#Write a program that takes two number 'n1' & 'n2' and a character 'ch' as input
n1=int(input("Enter your first number: "))
n2=int(input("Enter your second number: "))
ch=input("Enter your opration: ")


if ch == "*":
    mul= n1 * n2
    print(f"Multiplication of {n1} and {n2} is", mul)
elif ch == "/":
    div = n1/n2
    print((f"Division of {n1} and {n2} is", div))
elif ch == "%":
    mod = n1 % n2
    print(f"Division of {n1}  and {n2} is", mod)
elif ch == "+":
    add = n1 + n2
    print(f"additioin of {n1} and {n2} is", add)
elif ch == "-":
    sub = n1 - n2
    print(f"addition of {n1} and {n2} is", sub)
else:
    print("invalad opration")