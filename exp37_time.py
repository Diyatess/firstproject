class time:
    def __init__(self, hr, min,sec):
        self.__hr = hr
        self.__min = min
        self.__sec = sec

    def __add__(self, other):
        return self.__hr + other.__hr,self.__min + other.__min,self.__sec + other.__sec


t1 = time(1,22,34)
t2= time(2,5,24)
print(t1 + t2)