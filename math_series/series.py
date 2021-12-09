def fibonacci(n):
  '''
  This will be the fibonacci function
  it will take a number as an input 
  with that number it will tell you what the number in the fibonacci sequence that is
  it will set the base case for n == 0 = 0 and n == 0 = 1
  data type should be a number 
  fibonacci(0) = 0
  fibonacci(1) = 1
  fibonacci(2) = 1
  
  '''
  """
  line 14 is the base case for this function"""
  if n == 0 or n == 1:
    return n
  else:
    return fibonacci(n-1) + fibonacci(n-2)

def lucas(n):
  '''
  This will be the lucas function
  it will take a number as an input 
  with that number it will tell you what the number in the lucas sequence that is
  it will set the base case for n == 0 = 2 and n == 0 = 1
  data type should be a number 
  lucas(0) = 2
  lucas(1) = 1
  lucas(2) = 3
  
  '''
  if n == 0:
    return 2
  elif n == 1:
    return 1
  else:
    return lucas(n-1) + lucas(n-2)
