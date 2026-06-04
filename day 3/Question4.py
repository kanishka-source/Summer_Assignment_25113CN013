num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Find GCD
a, b = num1, num2
while b != 0:
    a, b = b, a % b

gcd = a

# Calculate LCM
lcm = (num1 * num2) // gcd

print("LCM is:", lcm)