a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter your choice(1.Add 2.Sub 3.Mul 4.Div):"))
if(c==1):
    sum=a+b
    print(sum)
elif(c==2):
    sub=a-b
    print(sub)
elif(c==3):
    pro=a*b
    print(pro)
elif(c==4):
    div=a/b
    print(div)
else:
    print("error")