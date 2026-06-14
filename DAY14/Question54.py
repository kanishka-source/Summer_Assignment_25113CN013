arr = [10, 20, 10, 30, 10, 40]
x = int(input("Enter element: "))

count = 0

for i in arr:
    if i == x:
        count += 1

print("Frequency of", x, "=", count)