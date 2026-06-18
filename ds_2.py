# Find the largest and smallest number in a list — first with max()/min(), then without them

numbers = [10, 5, 25, 3, 18]

print("Using max() and min():")
print("Largest number:", max(numbers))
print("Smallest number:", min(numbers))

largest = numbers[0]
smallest = numbers[0]

if numbers[1] > largest:
    largest = numbers[1]
if numbers[1] < smallest:
    smallest = numbers[1]

if numbers[2] > largest:
    largest = numbers[2]
if numbers[2] < smallest:
    smallest = numbers[2]

if numbers[3] > largest:
    largest = numbers[3]
if numbers[3] < smallest:
    smallest = numbers[3]

if numbers[4] > largest:
    largest = numbers[4]
if numbers[4] < smallest:
    smallest = numbers[4]

print("Without max() and min():")
print("Largest number:", largest)
print("Smallest number:", smallest)
