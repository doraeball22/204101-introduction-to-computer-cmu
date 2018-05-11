# 204101 sec 002 
# Lab Homework 10 no. 3
# Anurak Boonyaritpanit
# 560510680

def convertGradeToDigit(charGrade):
    if(charGrade == "A"):
        return 4.0
    elif(charGrade == "B"):
        return 3.0
    elif(charGrade == "C"):
        return 2.0
    elif(charGrade == "D"):
        return 1.0
    elif(charGrade == "F"):
        return 0.0
    else:
        return "error Input grade with [A B C D F]"

def calGPA():
    numberOfSubject = int(input("Number: "))
    sumOfweightXgrade = 0.0
    myGPA = 0.0
    sumOfWeight = 0.0

    for x in range(numberOfSubject):
        myGrade = input("Grade: ")
        myGrade = myGrade.upper()
        digitGrade = convertGradeToDigit(myGrade)

        weightOfGrade = float(input("Credit: "))

        weightXgrade = digitGrade * weightOfGrade
        sumOfweightXgrade += weightXgrade
        sumOfWeight += weightOfGrade

    myGPA = sumOfweightXgrade/sumOfWeight
    print("GPA: {:0.2f}".format(myGPA))

def main():
    calGPA()


if __name__ == "__main__":
    main()