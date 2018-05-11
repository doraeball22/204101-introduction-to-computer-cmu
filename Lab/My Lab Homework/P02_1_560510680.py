# 204101 sec 002 
# Lab Homework 02 ข้อ 1
# Anurak Boonyaritpanit
# 560510680

# ฟังก์ชั่นสำหรับแปลงค่าอุณภูมิจากองศา ฟาเรนไฮต์ -> เซลเซียส
def convertTempFahrenheitToCelsius( fahrenheit ):
    celsius = float((fahrenheit - 32) * 5/9)
    return celsius  

# ฟังก์ชั่นหลัก ทำงานที่นี่เป็นที่แรก
def main():
    fahrenheit = float(input("Input temperature in Fahrenheit: ")) 
    celsius = convertTempFahrenheitToCelsius(fahrenheit)
    print("{:0.2f} Fahrenheit = {:0.2f} Celsius".format(fahrenheit, celsius))

if __name__ == "__main__":
    # execute only if run as a script
    main()