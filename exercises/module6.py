# Python Essential Training
# Module 6: Modules & Pacakges
# Author: Dr. Alfred Ang
# Update: 19 Jan 2017

#import math
#print(math.sin(math.pi/2))

#import math as m
#print(m.sin(m.pi/2))

# from math import *
# print(sin(pi/2))

# from math import sin,pi
# print(sin(pi/2))

# import time,math,random

# print(math.sin(math.pi/2))
# time.sleep(10)
# print(math.sin(math.pi/2))

# print(random.randint(1,6))


import module5
from module5 import grocery

order = 400
discount, tax = module5.grocery(order)
print("The discount is ${:0.2f}".format(discount))
print("The tax is ${:0.2f}".format(tax))
