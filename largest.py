a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
c=int(input("Enter the 3rd number:"))
if(b>c):
    if(a>b):
        print(a,"is larger")
    else:
        print(b,"is larger")
else:
    if(a>c):
        print(a,"is larger")
    else:
        print(c,"is larger")