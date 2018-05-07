# -*- coding: utf-8 -*-
# @Author: Anurak Boonyaritpanit 
# @Student ID: 560510680
# @Subject: 204101 sec 002
# @Lab: 03_2 (What Counter)
# @Date:   2018-02-08 15:02:24
# @Last Modified by:   CSB307
# @Last Modified time: 2018-02-08 16:26:05


# Check the string that user input is "what"?
def isSayWhat(message):
    # determine the right word
    SAY_WHAT = "what"
    # convert string to lowercase
    message = message.lower()

    # campare 
    if(message == SAY_WHAT):
        return True
    else:
        return False

# i = 0
times = 0

# 1
message = input("Say what : ")
if(isSayWhat(message)):
        times += 1

# 2
message = input("Say what : ")
if(isSayWhat(message)):
        times += 1

# 3
message = input("Say what : ")
if(isSayWhat(message)):
        times += 1

# 4
message = input("Say what : ")
if(isSayWhat(message)):
        times += 1

# Print the result.
if(times > 0):
    print("You said what",times,"times." )
else:
    print("You haven't said what once." )

# if you can use use do while loop, it is equa above
# while True:

#     if(isSayWhat(message)):
#         times += 1 

#     if(i > 4):
#         break

#     i += 1


