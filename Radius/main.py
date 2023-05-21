import math

def circle_area(radius):
    area = math.pi * radius **2
    return area

radius = float(input("Enter the radius of the circle: "))

area = circle_area(radius)
print("The area of the circle is:" , area)