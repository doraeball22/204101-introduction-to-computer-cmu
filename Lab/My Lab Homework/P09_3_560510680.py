# 204101 sec 002 
# Lab Homework 9 ข้อ 3
# Anurak Boonyaritpanit
# 560510680
from pylab import *

# x is t (time lines)
t = arange(10000)
t_half = 5730
# y is n(t)
y = 100/(2**(t/t_half))

# plot graph
plot(t, y)
xlabel('time (Years)')
ylabel('Amount (%)')
ylim(0, 100)
grid(True)
show()