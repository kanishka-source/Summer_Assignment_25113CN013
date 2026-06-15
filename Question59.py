arr = [1, 2, 3, 4, 5]

print("Original Array:", arr)

last = arr.pop()
arr.insert(0, last)

print("Right Rotated Array:", arr)