# 204101 sec 002 
# Lab Homework 02 à¸‚à¹‰à¸­ 5
# Anurak Boonyaritpanit
# 560510680

ms = int(input("Input number of millisecond: ")) 
x = ms // 1000
seconds = x % 60
x = x // 60
minutes = x % 60
x = x // 60
hours = x % 24
x = x // 24
days = x

ms = ms%1000

print("Results = {} day(s), {} hours(s), {} minute(s), {} second(s), and {} millisec(s)".format(days, hours, minutes, seconds, ms))


