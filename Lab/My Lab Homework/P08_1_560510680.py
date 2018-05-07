# -*- coding: utf-8 -*-
# @Author: Anurak Boonyaritpanit 560510680
 #@Lab:   Lab08_1 sec 002
# @Date:   2018-03-29 16:14:54
# @Last Modified by:   CSB307
# @Last Modified time: 2018-03-29 16:28:20
def left_justify(str_in):
    if(len(str_in)<=50):
        print(str_in.ljust(50))
    else:
        print("Error string over characters")

def right_justify(str_in):
    if(len(str_in)<=50):
        print(str_in.rjust(50))
    else:
        print("Error string over characters")

def center_justify(str_in):
    if(len(str_in)<=50):
        print(str_in.center(50))
    else:
        print("Error string over characters")

def main():
    str_in = input("Enter string to justify: ")
    option = int(input("Enter option [1-3] (1=left, 2=right, 3=center): "))
    print('\n')

    if(option == 1):
        left_justify(str_in)
    elif(option == 2):
        right_justify(str_in)
    elif(option == 3):
        center_justify(str_in)

if __name__ == "__main__":
    # execute only if run as a script
    main()