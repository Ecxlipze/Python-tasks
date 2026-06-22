# Use *args to build a function that totals any number of numbers passed to it. 

def total_numbers(*args):
    total = 0

    for number in args:
        total = total + number

    return total


print(total_numbers(10, 20, 30))
print(total_numbers(5, 15, 25, 35))
