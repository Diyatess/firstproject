temp=float(input("Enter your temperature:"))
unit=input("Enter your unit as C or F: ")
if unit=="c" or unit=="C":
    f=(temp*1.8)+32
    print("The temperature in Fahrenheit is: ",f)
elif unit=="f" or unit=="F":
    c=(temp-32)/1.8
    print("The temperature in celsius is: ",c)
else:
    print("wrong input...")