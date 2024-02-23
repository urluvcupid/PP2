import math
import numpy as np

#1. Write a Python program to convert degree to radian.
def ConvRad(degrees):
    radians = degrees * math.pi / 180
    return radians
print("%.6f" % ConvRad(15.0))

#2. Write a Python program to calculate the area of a trapezoid.
def trapezoid():
    #Area = (base1 + base2) * height / 2
    Base1 = int(input('input base1: '))
    Base2 = int(input('input base2: '))
    Height = int(input('input height: '))
    return (Base1 + Base2) * Height/2
print(trapezoid())

#3. Write a Python program to calculate the area of regular polygon.
def RegPolygon():
    sides = int(input('input number of sides: '))
    length = int(input('input length of each side: '))
    cot = 1 / np.tan(math.pi/sides)
    area = sides/4 * length**2 * cot
    area = round(area)
    return area
print(RegPolygon())

#4.Write a Python program to calculate the area of a parallelogram.
def paralel():
   b = int(input('input base: '))
   h = int(input('input height: '))
   return b * h
print(paralel())












