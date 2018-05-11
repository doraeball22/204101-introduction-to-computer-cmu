# 204101 sec 002 
# Lab Homework 02 ข้อ 3
# Anurak Boonyaritpanit
# 560510680 

# แปลงเซนเป็นเมตร
def convertCentimeterToMeter(cm):
    newCm = cm / 100;
    return newCm

# คำนวณค่า bmi
def calculateBMI(weight_in_km, height_in_meter):
    bmi = weight_in_km/(height_in_meter*height_in_meter)
    return bmi

# ฟังก์ชั่นหลัก ทำงานที่นี่เป็นที่แรก
def main():
    weight_in_km = float(input("Input weight in kg: "))
    height_in_centimeter = float(input("Input height in cm: ")) 

    height_in_meter = convertCentimeterToMeter(height_in_centimeter)

    bmi = calculateBMI(weight_in_km, height_in_meter)

    print("Weight = {:0.2f} kg., Height = {:0.2f}, BMI = {:0.2f}".format(weight_in_km, height_in_centimeter, bmi))

if __name__ == "__main__":
    # execute only if run as a script
    main()