lower = int(input("Enter the lower limit: "))
upper = int(input("Enter the upper limit: "))

print("Armstrong numbers in the given range are:")

for num in range(lower, upper + 1):
    power = len(str(num))
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** power
        temp //= 10

    if num == total:
        print(num)