# Raise a custom error if an entered age is less than 0. 

age = int(input("Enter age: "))

if age < 0:
    raise ValueError("Age cannot be negative")

print("Age is valid")
