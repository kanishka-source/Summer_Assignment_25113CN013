words = input("Enter words separated by space: ").split()

words.sort(key=len)

print("Words Sorted by Length:")
for word in words:
    print(word)