# 204101 sec 002 
# Lab Homework 6 ข้อ 2
# Anurak Boonyaritpanit
# 560510680

num = int(input("num = "))
factorial = 1
if( num == 0):
    factorial = 0
else:
    for n in range(1,num+1):    
        factorial = factorial*n


print("{}!={}".format(num,factorial))