num = int(input("Enter a number: "))

product = 1

# Find product of digits
while num > 0:
    digit = num % 10
    product *= digit
    num //= 10

# Display result
print("Product of digits =", product)
