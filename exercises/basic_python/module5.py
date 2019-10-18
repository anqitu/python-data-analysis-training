# Python Essential Training
# Module 5: Functions
# Author: Dr. Alfred Ang
# Update: 19 Jan 2017

# Functions
# def f(x):
# 	return x*x
#
# print(f(7))

def calculate_PIT(salary):
    payable_tax = 0

    # <200000
    if salary < 20000:
        return payable_tax
    # payable_tax += 0

    # 200000 - 400000
    salary -= 20000
    if salary < 20000:
        payable_tax += salary *0.02
        return payable_tax

    payable_tax += 20000 *0.02

    # 400000 - 700000
    salary -= 20000
    if salary < 30000:
        payable_tax += salary *0.05
        return payable_tax

    payable_tax += 30000 *0.05

    #  >70000
    salary -= 30000
    payable_tax += salary *0.10
    return payable_tax

calculate_PIT(70001)

distance = 38
(fare,tax) = taxifare(distance)
print("Taxi fare is ${} and tax is ${:0.1f}".format(fare,tax))

# Multiple Outputs
# def f(x):
# 	return x, 2*x

# Multiple Inputs
# def f(x=2,y=0):
# 	return 2*x+3*y
#
# print(f(1,6))
#

# Multiple Inputs/Ouputs
RATE = 0.02
def loan_balance(balance, years, partial_payment):
    charge = balance * (1+RATE)**years - balance
    balance = balance + charge - partial_payment
    return charge, balance
loan_balance(10000, 5, 5000)


# Variable Inputs
# def sum(a,b,*c):
# 	s = 0
# 	s = a+b
# 	for i in c:
# 		s = s+i
# 	return s
# print(sum(3,4,5,6,7,8,9,10,11,12))

# Variable Arguments
# def find_highest_net_worth(a, *b):
#     name, highest_net_worth = a
#     for person, net_worth in b:
#         if net_worth > highest_net_worth:
#             name, highest_net_worth = person, net_worth
#     return name
#
# find_highest_net_worth(('Bill Gates', 100), ('Jack Ma', 200), ('Warren Buffet', 50))

# def sum2(a,b):
# 	s = 0
# 	for i in range(a,b+1):
# 		s = s+i
# 	return s
#
# print(sum2(1,100))
#
# Loop through dictionary
# def f(**a):
# 	for i,j in a.items():
# 		print(i,j)
#
# a = {'a':3,'b':5}
# f(a=3,b=5)
#
# Lambda Function
#
# def f(x):
# 	return x*x
# a = lambda x:x*x
#
# print(a(4))
#
# def f(x,y): return 10*x+y
# print(f(3,4))
#
# a = lambda x,y:10*x+y
# print(a(3,4))
#
# Map
# a = [2,3,4,5]
# b = map(lambda x:10*x+4,a)
# print(list(b))
#
# Exercise: Map
# x = [0,1,2,3]
# y = [2,4,6,8]
#
# a = map(lambda x,y:10*x+y,x,y)
# print(list(a))
#
# Filter
# a = filter(lambda x:x>4,[5,6,3,2,7])
# print(list(a))
