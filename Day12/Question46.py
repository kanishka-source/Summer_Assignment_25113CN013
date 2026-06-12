def armstrong(n):
    temp = n
    digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit ** digits
        n = n // 10

    if temp == total:
        print("Armstrong Number")
    else:
        print("Not an Armstrong Number")

num = int(input("Enter a number: "))
armstrong(num)