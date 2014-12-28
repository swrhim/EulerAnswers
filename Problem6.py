__author__ = 'Daniel'
import math

def FindSumSquareDifference(upperBound):
    counter = 1
    sumOfSquares = 0
    squareOfSums = 0
    while counter <= upperBound:
        sumOfSquares += math.pow(counter, 2)
        squareOfSums += counter
        counter += 1
    return math.pow(squareOfSums, 2) - sumOfSquares

print FindSumSquareDifference(100)