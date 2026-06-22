# Write a function that returns both the sum and average of a list. 

def sum_avg(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

marks = [80, 90, 70, 85]
total_marks, average_marks = sum_avg(marks)

print("Sum:", total_marks)
print("Average:", average_marks)
