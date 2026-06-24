# Build a calculator that doesn't crash on divide-by-zero, but shows a message instead

try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("You cannot divide by zero")

finally:
    print("Program finished")
