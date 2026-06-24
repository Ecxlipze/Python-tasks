# Build a dictionary of student names and marks, then calculate the average. 

students = {
    "Ali": 80,
    "Sara": 90,
    "Ahmed": 70
}

total_marks = students["Ali"] + students["Sara"] + students["Ahmed"] 
average_marks = total_marks / len(students)

print("Student marks:", students)
print("Average marks:", average_marks)
