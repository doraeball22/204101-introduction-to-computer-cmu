# -*- coding: utf-8 -*-
# @Name: Anurak Boonyaritpanit
# @Student ID: 560510680
# @Section: 002
# @Author: CSB307
# @Date:   2018-02-22 15:36:03
# @Last Modified by:   CSB307
# @Last Modified time: 2018-02-22 16:30:44
   
def isValidEmail(email):
    # split name and domain name from email 
    email_name = email.split('@')[0]
    email_domain = email.split('@')[1]

    # convert domain name to lowercase 
    email_domain = email_domain.lower()

    isValid = True
    cmu_email_domain_name = "cmu.ac.th"

    if(email.count('@') != 1):
        isValid = False

    if(email[0] == '@'):
        isValid = False

    if(email_domain != cmu_email_domain_name):
        isValid = False

    # Print Result
    if(isValid):
        return True
    else:
        return False

def main():
    # anurak_b@cmu.ac.th
    # jakramate@cmu.ac.th
    email = input("Please input email: ") 
    # Print Result
    if(isValidEmail(email)):
        print("Valid")
    else:
        print("Invalid")

       
    
if __name__=='__main__':
    main()