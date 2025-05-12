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


# op_size = (n-f+2p/s) + 1

op_size = len(image) - len(kernel) + 1 # 5-3+1 = 3
for i in range(op_size):
  for j in range(op_size):
      sum = 0
      for ki in range(len(kernel)):
        for kj in range(len(kernel[0])):
            sum += image[i + ki][j+kj] * kernel[ki][kj]
      output[i][j] = sum
    
print(output)
# [[-6, 12, 14], [-8, 6, 8], [-10, -2, -2]]
