import math

def rect(a,b):
    print("Rectangle area=",a*b)
    print("Rectangle perimrter=",2*(a+b))

def cir(r):
    print("Circle area=",math.pi*r*r)
    print("Circle perimrter=",2*(math.pi*r))

def cuboid(l,b,h):
    print("Cuboid area=",2*((l*b)+(b*h)+(h+l)))
    print("Cuboid perimeter=",4*(l+b+h+l))

def sphere(r):
    print("Sphere area=",4*(math.pi*r*r))
    print("Sphere perimrter=",2*(math.pi*r))