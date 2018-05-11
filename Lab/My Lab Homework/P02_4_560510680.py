# 204101 sec 002 
# Lab Homework 02 à¸‚à¹‰à¸­ 4
# Anurak Boonyaritpanit
# 560510680

def calPointOfIntersection(m1, b1, m2, b2):
    # à¸ªà¸¡à¸à¸²à¸£à¹€à¸ªà¸™à¸•à¸£à¸‡ y = mx+b

    # find value of x
    x = (b2-b1)/(m1-m2)
    # find value of y à¹‚à¸”à¸¢à¹à¸—à¸™à¸„à¹ˆà¸² x à¸¥à¸‡à¹ƒà¸™à¸ªà¸¡à¸à¸²à¸£à¹€à¸ªà¹‰à¸™à¸•à¸£à¸‡ 1 à¸«à¸£à¸·à¸­ 2 à¸à¹‡à¹„à¸”à¹‰ (y = mx+b) 
    y = (m1*x)+b1
    #à¹à¸ªà¸”à¸‡à¸„à¹ˆà¸² .2f à¹à¸—à¸™à¸—à¸¨à¸™à¸´à¸¢à¸¡ 2 à¸•à¸³à¹à¸«à¸™à¹ˆà¸‡
    print("The point of intersection is at = {:0.2f} and y = {:0.2f}".format(x, y))


# à¸Ÿà¸±à¸‡à¸à¹Œà¸Šà¸±à¹ˆà¸™à¸«à¸¥à¸±à¸ à¸—à¸³à¸‡à¸²à¸™à¸—à¸µà¹ˆà¸™à¸µà¹ˆà¹€à¸›à¹‡à¸™à¸—à¸µà¹ˆà¹à¸£à¸
def main():
    print("First Equation")
    m1 = float(input("Input m1: ")) 
    b1 = float(input("Input b1: ")) 
    
    print("Second Equation")
    m2 = float(input("Input m2: ")) 
    b2 = float(input("Input b2: ")) 

    calPointOfIntersection(m1, b1, m2, b2)

    
if __name__ == "__main__":
    # execute only if run as a script
    main()