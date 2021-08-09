credit = int(input("Input the credits of the Code for campus leader: "))
if credit >= 7500:
    print("Tera leader")
elif credit >= 6000 and credit < 7500:
    print("Gega leader")
elif credit >= 4500 and credit < 6000:
    print("Mega leader")
elif credit < 4500:
    print("Rising Star")