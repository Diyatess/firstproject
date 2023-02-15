class mathoperation:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print("Sum:",self.x+self.y)
        print("Substract:", self.x - self.y)
        print("Multiplication:", self.x * self.y)
        print("Division:", self.x / self.y)


o=mathoperation(20,5)
o.show()
