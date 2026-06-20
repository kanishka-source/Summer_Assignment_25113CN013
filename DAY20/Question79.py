matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for i in range(len(matrix)):
    row_sum = sum(matrix[i])
    print("Sum of Row", i + 1, "=", row_sum)