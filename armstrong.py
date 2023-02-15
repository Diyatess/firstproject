min=int(input("Enter the starting limit:"))
max=int(input("Enter the ending limit:"))
print("Armstrong numbers are:")
i=min;
while i<=max:
    temp=i
    sum=0
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if(i==sum):
        print(i)
    i += 1