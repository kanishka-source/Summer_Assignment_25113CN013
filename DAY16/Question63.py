arr = [2, 4, 3, 5, 7, 8]
target = 9

found = False

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == target:
            print("Pair:", arr[i], arr[j])
            found = True

if not found:
    print("No pair found")