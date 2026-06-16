arr = [1, 2, 2, 3, 3, 3, 4]

freq = {}

for num in arr:
    freq[num] = freq.get(num, 0) + 1

max_element = max(freq, key=freq.get)

print("Element with Maximum Frequency =", max_element)
print("Frequency =", freq[max_element])