# 204101 sec 002 
# Lab Homework 9 ข้อ 2
# Anurak Boonyaritpanit
# 560510680
import numpy as np

a = np.array([[4, 2, 0], [9,3,7], [1,2,1]], dtype=float)

y = np.linalg.inv(a)
z = np.dot(a, y)

print("z = ", z)
print("y = ", y)