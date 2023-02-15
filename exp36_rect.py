class rectangle:
    def __init__(self,l,b):
        self.__length=l
        self.__width=b

    def __lt__(self, other):
        if self.__length*self.__width< other.__length*other.__width:
            return True
        else:
            return False
o1=rectangle(2,4)
o2=rectangle(3,5)

if o1 < o2:
    print("1st obj area is les than 2nd")
else:
    print("2nd obj area is les than 1st")