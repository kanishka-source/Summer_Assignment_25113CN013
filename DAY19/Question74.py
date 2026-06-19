for i in range(r):
    A.append(list(map(int, input().split())))

print("Enter second matrix:")
for i in range(r):
    B.append(list(map(int, input().split())))

result = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] - B[i][j])
    result.append(row)

print("Subtracted Matrix:")
for row in result:
    print(row)