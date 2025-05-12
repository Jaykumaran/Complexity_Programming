# Simple implementation of finding the fibonacci of n 


def fibonacci(n):
    a,b = 0, 1
    sequence = []
    
    for _ in range(n):
      sequence.append(a)
      a, b = b, a + b
    return sequence

sequence = fibonacci(10)
print(sequence)
    
  
