__author__ = 'Daniel'

# 2250 is the smallest number that is divisible by 1-10
# brute force implementation

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def FindSmallest():
    isdivisiblebyall = False
    divisibleNumber = 2520
    while isdivisiblebyall is False:
        for num in nums:
            print divisibleNumber
            if divisibleNumber % num == 0:
                isdivisiblebyall = True
            else:
                isdivisiblebyall = False
                break
        if isdivisiblebyall is True:
            return divisibleNumber
        divisibleNumber += 2520
print FindSmallest()