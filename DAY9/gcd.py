def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

n1 = int(input("Enter the first integer: "))
n2 = int(input("Enter the second integer: "))
print("The GCD of", n1, "and", n2, "is:", gcd(n1, n2))
