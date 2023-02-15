n=int(input("enter the size of list"))
print("enter the elements")
l=[]
for i in range (0,n):
    ele = int(input())
    if ele>100:
        l.append("over")
    else:
        l.append(ele)
print(l)