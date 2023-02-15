def longest(words):
    longest = 0
    for i in words:
        if len(i) > longest:
            longest = len(i)
    print(longest)
string1=[]
n=int(input("enter the limit:"))
print("enter the string:")
for n in range(0,n):
  ele1=input()
  string1.append(ele1)
longest(string1)