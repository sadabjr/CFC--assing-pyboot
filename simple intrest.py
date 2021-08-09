#Program to find the simple intrest based on the inputs
#amount
#rate
#time, provided by the user

amount = float(input("Enter the amount :"))
rate = float(input("Enter the rate : "))
time = float(input("Enter the time : "))

si = (amount * rate * time)/100
total = amount + si

print(si)
print(f"The total amount will be {total}")