# 204101 sec 002 
# Lab Homework 7 assignment 2
# Anurak Boonyaritpanit
# 560510680

# In this case to show use "for" loop ============================================================================================================================
# uncomment code below to show

# DEFINE initial value
mySum = 0

n = int(input("n: "))

for x in range(n):
    num = float(input("Input number: ")) # Input number
    # DEFINE initial value
    if( x == 0):
        myMax = num
        myMin = num
    # Compare value of number
    if(num < myMin):
        myMin = num
    if(num > myMax):
        myMax = num
    mySum = mySum + num # Find sum: x=0-> mySum= 0+num

myMean = mySum/n # Find x bar
# myMean is floating point. And You want convert 2 digits ex. 11.2345687 -> 11.23 use round(number, ndigits) ปัดเศษนั่นเอง
# myMean = round(myMean, 2)

# Display value in terminal/cmd/console
# print("mySum =",mySum)
print("min =",myMin)
print("max =",myMax)
# If you use round() function. The .format() unnessessary -> print("myMean =",myMean)
print("mean = {:0.2f}".format(myMean))




# In this case to show use "while" loop And define initial min max mean sum to first number of input====================================================================================================================================
# uncomment code below to show

# n = int(input("n: "))
# num = float(input("Input number: "))

# # DEFINE initial value
# myMax = num
# myMin = num
# mySum = num

# x=0 # dont forget to start point value
# while(x < n-1):
#     # Input number
#     num = float(input("Input number: "))
#     # Compare value of number
#     if(num < myMin):
#         myMin = num
#     if(num > myMax):
#         myMax = num
#     mySum = mySum + num # Find sum: x=0-> mySum= 0+num
#     x = x+1 # increment x +1 for control loop

# myMean = mySum/n # Find x bar

# # Display value in terminal/cmd/console
# # print("mySum =",mySum)
# print("min =",myMin)
# print("max =",myMax)
# print("mean = {:0.2f}".format(myMean))