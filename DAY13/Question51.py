n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

largest = max(arr)
smallest = min(arr)

print("Largest element =", largest)
print("Smallest element =", smallest)