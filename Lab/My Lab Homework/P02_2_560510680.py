# 204101 sec 002 
# Lab Homework 02 ข้อ 2
# Anurak Boonyaritpanit
# 560510680

# ฟังก์ชั่นสำหรับแปลงค่าอุณภูมิจากองศา เซลเซียส -> ฟาเรนไฮต์  
def convertTempCelsiusToFahrenheit( celsius ):
    fahrenheit = float((celsius * 9/5) + 32)
    return fahrenheit  

# ฟังก์ชั่นหลัก ทำงานที่นี่เป็นที่แรก
def main():
    celsius = float(input("Input temperature in Celsius: ")) 
    fahrenheit = convertTempCelsiusToFahrenheit(celsius)
    print("{:0.2f} Celsius = {:0.2f} Fahrenheit".format(celsius, fahrenheit))

if __name__ == "__main__":
    # execute only if run as a script
    main()