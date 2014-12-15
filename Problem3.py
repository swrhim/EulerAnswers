import math

def LargestPrime(num):
  d = 2
  factors = []
  while num > 1:
    while num%d==0:
      factors.append(d)
      num /= d
    d = d+1
  return factors

primes = LargestPrime(600851475143)
print max(primes)
