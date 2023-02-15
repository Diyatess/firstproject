color1=[]
color2=[]
n=int(input("enter the limit:"))
print("enter the colors:")
for n in range(0,n):
  ele1=input()
  color1.append(ele1)
m = int(input("enter the limit:"))
print("enter the colors:")
for m in range(0,m):
  ele2=input()
  color2.append(ele2)
for color in color1:
  if color not in color2:
    print(color)
