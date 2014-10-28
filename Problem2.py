
def Fibonacci():
  total = 0
  lastValue = 1
  value = 1
  while value < 4000000:
    print "Current Value: " + str(value)
    print "Last Value: " + str(lastValue)
    if value % 2 == 0:
      total += value
    tmpValue = value
    value = value + lastValue
    lastValue = tmpValue
  return total

print Fibonacci()

