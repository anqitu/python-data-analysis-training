# Q2
#
# With a given integral number n, write a
# function to generate a dictionary that contains
# (i, i*i) such that i is an integral number
# between 1 and n (inclusive). The function
# should return the dictionary.
#
# Example:
# given the input is 8, the output should be
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#
# Hint:
# Consider using dict comprehension

# method 1
def solve(n):
    return {i:i*i for i in range(1, n+1)}

# method 2
solve = lambda n: {i:i*i for i in range(1, n+1)}

# method 3
def solve(n):
    ans = {}
    for num in range(1, n+1):
        ans[num] = num*num
    return ans
