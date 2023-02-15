l1=[1,2,3,4,5,6]
l2=[7,8,9,10,11,12]
a= len(l1)==len(l2)
print(a)
b=sum(l1)==sum(l2)
print(b)
cout=0
for x in l1:
    for y in l2:
        if x==y:
            cout=1
if cout==1:
    print("there is common elements")
else:
    print("there is no common element")
