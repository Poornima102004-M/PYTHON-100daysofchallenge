import math
def area(r):
    area_circle=math.pi*r*r
    return area_circle
r=int(input('Radius'))
print("Area of a circle",area(r))
