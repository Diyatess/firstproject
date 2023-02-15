class A:
    def __init__(self, a):
        self.a = a


class B(A):
    def __init__(self, b, a):
        self.b = b
        A.__init__(self, a)


class C(B):
    def __init__(self, c, b, a):
        self.c = c
        B.__init__(self, b, a)
class D(B):
    def __init__(self,c,b,a):
        C.__init__(self,c,b,a)
    def compare(self):
        if self.b > self.c:
            if self.a > self.b:
                print("a is greater", self.a)
            else:
                print("b is greater", self.b)
        else:
            if self.a > self.c:
                print("a is greater", self.a)
            else:
                print("c is greater", self.c)


d = D(3, 8, 1)
d.compare()