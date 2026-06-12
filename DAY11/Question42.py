def maximum(a, b):
    if a > b:
        return a
    else:
        return b

# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Function call
result = maximum(num1, num2)

# Display result
print("Maximum number =", result)