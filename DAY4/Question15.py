num = int(input("Enter a number: "))

# Number of digits
n = len(str(num))

# Calculate sum of digits raised to the power n
temp = num
sum_of_powers = 0

while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** n
    temp //= 10

# Check Armstrong number
if num == sum_of_powers:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")