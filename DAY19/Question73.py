A.append(row)

print("Enter second matrix:")
for i in range(r):
    row = list(map(int, input().split()))
    B.append(row)

result = []

for i in range(r):
    row = []
    for j in range(c):
        row.append(A[i][j] + B[i][j])
    result.append(row)

print("Sum Matrix:")
for row in result:
    print(row)