num = int(input("Enter a number: "))

# Initialize sum
digit_sum = 0

# Find sum of digits
while num > 0:
    digit_sum += num % 10
    num //= 10
