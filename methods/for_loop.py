"""
File with a collection of for-loop methods 
(while and do-while loops are a corollary)
Author: Abhishek Roushan abhishek.roushan12@gmail.com
"""

# simple for loop performing addition
# (subtraction execution time would be similar)
def forLoopAddition():
    result = 0
    for i in range(10000):
        result += i
    return result


# simple for loop performing multiplication
# (division execution time would be similar)
def forLoopMultiplication():
    result = 1
    for i in range(10000):
        result *= i
    return result
