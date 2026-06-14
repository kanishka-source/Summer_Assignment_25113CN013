arr = [12, 45, 23, 67, 89, 54]

largest = second = -999999

for num in arr:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second Largest Element =", second)