# 204101 sec 002 
# Lab Homework 10 ข้อ 1
# Anurak Boonyaritpanit
# 560510680
import numpy as np

def findQuadrant(angles_in_radians):
    quadrant = angles_in_radians
    if angles_in_radians == 0 or angles_in_radians == np.pi*2:
        quadrant = "Origin"
    elif angles_in_radians > 0 and angles_in_radians <= np.pi/2:
        quadrant = 1
    elif angles_in_radians > np.pi/2 and angles_in_radians <= np.pi:
        quadrant = 2
    elif angles_in_radians > np.pi and angles_in_radians <= np.pi*3/4:
        quadrant = 3
    elif angles_in_radians > np.pi*3/4 and angles_in_radians < np.pi*2:
        quadrant = 4
    return quadrant

def findQuadrantSimple(x, y):
    if x > 0 and y > 0:
        quadrant = 1
    elif x < 0 and y > 0:
        quadrant = 2
    elif x < 0 and y < 0:
        quadrant = 3
    elif x > 0 and y < 0:
        quadrant = 4
    else:
        quadrant = "Origin"
    return quadrant


def input1():
    n = int(input("N = "))
    for x in range(n):
        x0 = float(input("Input X: "))
        y0 = float(input("Input Y: "))
    
        x = np.array([x0])
        y = np.array([y0])
        # Use arctan for find quadrant of (x0, y0)
        # https://docs.scipy.org/doc/numpy-1.14.0/reference/generated/numpy.arctan2.html
        array_of_angles_in_radians = np.sin(y, x) * 180 / np.pi                 
    
        angles_in_radians = array_of_angles_in_radians[0]
        # ยังทำผิดอยู่
        print(angles_in_radians)
    
        quadrant = findQuadrant(angles_in_radians)
    
        print("Point ({}, {}) is in Quadrant {}".format(x0, y0, quadrant))

def input2():
    n = int(input("N = "))
    for x in range(n):
        x0 = float(input("Input X: "))
        y0 = float(input("Input Y: "))

        quadrant = findQuadrantSimple(x0, y0)
        print("Point ({}, {}) is in Quadrant {}".format(x0, y0, quadrant))


def main():
    # input1()
    input2()


if __name__ == "__main__":
    main()

 


