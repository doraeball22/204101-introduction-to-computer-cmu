# 204101 sec 002 
# Lab Homework 7 assignment 3
# Anurak Boonyaritpanit
# 560510680

# ex1. In this case to show use "for" loop ============================================================================================================================
# START HERE!! uncomment code below to show 

# n = int(input("n: "))

# for x in range(n):
#     num = int(input("Input number: ")) # Input number
#     # DEFINE initial value
#     if( x == 0):
#         firstMin = num
#         secondMin = num
#     # Compare value of number
#     if(num < firstMin):
#         firstMin = num
#     if(num > firstMin and num < secondMin):
#         secondMin = num

# # Display value in terminal/cmd/console
# print("firstMin =",firstMin)
# print("secondMin =",secondMin)

# ex2. ===========================================================================================================================================================

# ทำแบบเหมือนในตัวอย่าง ที่ input ใส่เลขได้หลายค่าในบรรทัดเดียว แล้วค่อยกด enter 
# START HERE!! uncomment code below to show 

# If floating point(กรณีเลขทศนิยม) use below
# numbers = list(map(float, input (). split ())) # input like this: 2.1 5.24 4 5 8 71 10.9 (พิมพ์ตัวเลขแต่ละตัวแล้วคั่นด้วยช่องว่าง เหมือนในโจทย์ โดยค่าจะใส่ไว้ในตัวแปรที่เป็น list)

# If integer(กรณีเลขจำนวนเต็ม) use below
numbers = list(map(int, input (). split ())) # input like this: 2 5 4 5 8 71 10 (พิมพ์ตัวเลขแต่ละตัวแล้วคั่นด้วยช่องว่าง เหมือนในโจทย์ โดยค่าจะใส่ไว้ในตัวแปรที่เป็น list) 
# print(numbers) # [2, 5, 4, 5, 8, 71, 10] display for debug

# DEFINE initial value with value is equal to first number of list
firstMin = numbers[0]
secondMin = numbers[0]

for number in numbers:
    # Compare value of number
    if(number < firstMin):
        firstMin = number
    if(number > firstMin and number < secondMin):
        secondMin = number

# Display value in terminal/cmd/console
print(firstMin)
print(secondMin)

# ex2. Output
# python '.\P07_3_560510680.py'
# 4 5 6 7 -1 0 <-- numbers as you want to input
# -1
# 0