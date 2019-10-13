# Python Essential Training
# Module 4: Control Structures
# Author: Dr. Alfred Ang
# Update: 19 Jan 2017

# a = 7
# b = 7

# if (a<b):
# 	print("a is smaller than b")
# elif (a>b):
# 	print("a is larger than b")
# else:
# 	print("a is same as b")

# order = 100
# discount = 25 if order > 200 else 0
# print(discount)

# Exercise
# balance = 0
# while (True):
#     transaction = input("Enter transaction log > ");
#
#     # guard clause
#     if (transaction == "exit"):
#         break
#
#     t = transaction.split()
#     # type = t_split[0]
#     # amount = t_split[1]
#     type, amount = t
#
#     if not (len(t) == 2 and type in ["D", "W"] and amount.isdigit()):
#         print("Invalid log, try again")
#         continue
#
#     amount = float(amount)
#
#     if (type == "D"):
#         balance += amount
#     elif (type == "W"):
#         balance -= amount
#
#     # balance += amount * (-1 if type == "W" else 1)
#
# print("balance: {}".format(balance))



# Loop

# a = 1
# while (a<10):
# 	print(a)
	#a += 1

# a = 1
# b = 1
# while (b<100):
# 	a,b = b,a+b
# 	print(a)

# For Loop

# a = (3,4,7,9)
# for i in a:
# 	print(i)

# for i in range(1,11):
	#if i==4:continue
	# if i==4:break
	# print(i)

# a = []
# for i in range(1,11):
# 	a.append(i*i)
# print(a)

# Enumerate
# person = ['Ally','Belinda','Jane']
# height = [168,155,170]
# weight = [60,68,55]

# for index, name in enumerate(person):
# 	#print(index, name)
# 	print("{} height is {}cm and weight is {}kg".format(name,height[index],weight[index]))

# Zip
# person = ['Alfred','Ally','Belinda']
# height = [170,160,155]

# c = zip(person,height)
# for i,j in c:
#     print(i,j)

# Exercise: Zip
# name = ['Ally','Belinda','Jane']
# height = [170,159,161]
# weight = [60,55,45]

# c = zip(name,height,weight)
#print(list(c))

# for name, h, w in c:
# 	print("{} height is {}cm and weight is {}kg".format(name,h,w))

# Else in Loop
# for i in range(1,11):
# 	if i==4:break
# 	print(i)
# else:
# 	print("no break")

# Exercise
# primes = []
# for n in range(1,101):
# 	for divisor in range(2, n):
# 		if n%divisor == 0:break
# 	else:
# 		primes.append(n)

# print(primes)
