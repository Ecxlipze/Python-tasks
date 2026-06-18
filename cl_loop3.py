# Print the multiplication table of a given number. 

number = int(input("Enter a number: "))

for count in range(1, 11):
    answer = number * count
    print(f"{number} x {count} = {answer}")

