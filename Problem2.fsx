let upperBound = 4000000
let rec fib a b sum =
  if b > upperBound then
    sum
  else
    if b % 2 = 0 then
      fib (b) (a+b) (b+sum)
    else
      fib (b) (a+b) (sum)

fib 1 2 0
