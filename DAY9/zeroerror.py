try:
    a = float(input("Enter the numerator: "))
    b = float(input("Enter the denominator: "))
    r= a/ b
    print("Result:", r)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
