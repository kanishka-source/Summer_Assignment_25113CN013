n = int(input("Enter size of square matrix: "))

matrix = []

print("Enter matrix:")
for i in range(n):
    matrix.append(list(map(int, input().split())))

diagonal_sum = 0

for i in range(n):
    diagonal_sum += matrix[i][i]

print("Diagonal Sum =", diagonal_sum)