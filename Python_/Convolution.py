# 5x5 image
image = [
    [1, 2, 3, 0, 1],
    [4, 5, 6, 1, 0],
    [7, 8, 9, 2, 3],
    [1, 3, 5, 7, 9],
    [0, 2, 4, 6, 8]
]

# Horizontal edge
# 3x3 kernel
kernel = [
    [1, 0, -1],
    [1, 0, -1],
    [1, 0, -1]
]

# Empty 3x3 output
output = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for i in range(len(image)):
  for j in range(len(image)):
      sum = 0
      for ki in range(len(kernel)):
        for kj in range(len(kernel)):
            sum += image[i + ki][j+kj] * kernel[i][j]
      output[ki][kj] = sum
    
print(output)

