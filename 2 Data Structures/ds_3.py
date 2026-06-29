# Build a dictionary of student names and marks, then calculate the average. 

students = {
    "Ali": 80,
    "Sara": 90,
    "Ahmed": 70
}

total_marks = 0
for marks in students.values():
    total_marks = total_marks + marks
average_marks = total_marks / len(students)

# print("Student marks:", students)
print("Average marks:", average_marks)

for name, marks in students.items():
    print(name, ":", marks)

