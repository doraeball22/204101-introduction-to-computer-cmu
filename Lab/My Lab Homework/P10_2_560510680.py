# 204101 sec 002 
# Lab Homework 10 ข้อ 2
# Anurak Boonyaritpanit
# 560510680
import numpy as np

def calMySD(X):
    X.sort()
    print(X)
    # [13.75, 21.52, 32.32, 43.34, 43.47, 44.32, 55.63, 56.98]
    
    # Using NumPy's built-in functions to Find Mean, Median, SD and Variance
    mean = np.mean(X)
    median = np.median(X)
    sd = np.std(X)
    return sd

def main():
   # X is a Python List
    X = []
    n = int(input("N = "))
    for x in range(n):
        print("x{} = ".format(x), end="")
        number = float(input())  
        X.append(number)

    sd = calMySD(X)

    print("S.D.= {}".format(sd))


if __name__ == "__main__":
    main()