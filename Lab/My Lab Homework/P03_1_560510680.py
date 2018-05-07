# -*- coding: utf-8 -*-
# @Author: Anurak Boonyaritpanit 
# @Student ID: 560510680
# @Subject: 204101 sec 002
# @Lab: 03_1 (Circle or Square)
# @Date:   2018-02-08 15:02:24
# @Last Modified by:   CSB307
# @Last Modified time: 2018-02-08 15:48:47

PI = 3.14159

choice = input("Input c if you want to calculate the area of a circle, others for square : ")
choice = choice.lower()

if(choice == 'c' or choice == 'C' ):
    raduis = float(input("Radius : "))
    area = PI * raduis**2
    print("Area = {0:.5f}".format(area))
else:
    side = float(input("Side : "))
    area = side * side
    print("Area = ",area)
    
    
