__author__ = 'Daniel'
import math

def FindNthPrime(position):
    # skip 2 since it's the only prime that's even
    counter = 2
    possiblePrime = 3
    while counter < position:
        possiblePrime += 2

        isPrimeFlag = IsPrime(possiblePrime)

        if isPrimeFlag:
            counter += 1

    return possiblePrime

def IsPrime(num):
    maxNum = int(math.ceil(math.sqrt(num)))
    for i in range(2, maxNum+1):
        if num % i == 0:
            return False
    return True

print FindNthPrime(10001)