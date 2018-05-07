# 204101 sec 002 
# Lab Homework 7 assignment 1
# Anurak Boonyaritpanit
# 560510680

symbol = '*'
newLine = '\n'
whiteSpace = ' '

choice = int(input("Select Type[1-4]: ")) 
# num = 4
num = int(input("Input Number: "))

if(choice==1):
    # choice 1
    for row in range(num):
        for col in range(row+1):
            print(symbol,end='')
        print(newLine,end='')
elif(choice==2):
    # choice 2
    for row in range(num):
        for col in range(num):
            if(col < (num-row-1)): #if num = 4: 4-0-1 = 3
                print(whiteSpace,end='')
            else:
                print(symbol,end='')
        print(newLine,end='')
elif(choice==3):
    # choice 3
    for row in range(num):
        for col in range(num):
            if(col < (num-row)): #if num = 4: 4-0 = 4
                print(symbol,end='')
            else:
                print(whiteSpace,end='')
        print(newLine,end='')

elif(choice==4):
    # choice 4
    for row in range(num):
        for col in range(num):
            if(col < row): 
                print(whiteSpace,end='')
            else:
                print(symbol,end='')
        print(newLine,end='')
else:
    print("Error! Please Input Type in range [1-4]")


# Type 1
# *
# **
# ***
# ****

# Type 2
#    *
#   **
#  ***
# ****

# Type 3
# ****
# ***
# **
# *

# Type 4
# ****
#  ***
#   **
#    *