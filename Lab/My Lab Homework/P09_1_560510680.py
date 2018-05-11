# 204101 sec 002 
# Lab Homework 9 ข้อ 1
# Anurak Boonyaritpanit
# 560510680
import numpy as np

# Define: u = (1,3,3), v = (-1,0,3) and w = (1,-2,3)
# Find x:  2u – v + x = 7x + w
u = np.array([1, 3, 3], dtype=float)
v = np.array([-1, 0, 3], dtype=float)
w = np.array([1, -2, 3], dtype=float)

A = (2*u-v-w)/6

print("x =", A)