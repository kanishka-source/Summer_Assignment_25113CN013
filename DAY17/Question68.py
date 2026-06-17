arr1 = [10, 20, 30, 40, 50]
arr2 = [30, 40, 50, 60, 70]

common = []

for i in arr1:
    if i in arr2:
        common.append(i)

print("Common Elements:", common)