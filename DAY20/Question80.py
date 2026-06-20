matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

cols = len(matrix[0])

for j in range(cols):
    col_sum = 0
    for i in range(len(matrix)):
        col_sum += matrix[i][j]

    print("Sum of Column", j + 1, "=", col_sum)