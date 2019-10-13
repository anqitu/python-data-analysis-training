# Q1
#
# Write a program which will find all such
# numbers which are divisible by 7 but are
# not a multiple of 5, between 2000 and
# 3200 (inclusive).
#
# Hint:
# Consider using range() method


# method 1
ans = []
for num in range(2000, 3201):
    if (num%7 == 0 and num%5 != 0):
        ans.append(num)
ans

# method 2
[num for num in range(2000, 3201) if not num%7 and num%5]

# method 3
[num for num in range(2000, 3201) if (num%7 == 0 and num%5 != 0)]

# method 4
list(filter(lambda num : (num%7 == 0 and num%5 != 0), range(2000, 3201)))
