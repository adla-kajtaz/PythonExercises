def factorial(x):
  result = 1
  while x > 0:
    result *= x
    x -= 1
  return result  

print (factorial(4))
