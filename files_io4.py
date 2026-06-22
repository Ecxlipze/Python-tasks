# Save a dictionary to a JSON file, then load it back and print it. 

import json

student = {
    "name": "Ali",
    "age": 20,
    "marks": 85
}

with open("student.json", "w") as file:
    json.dump(student, file)

with open("student.json", "r") as file:
    data = json.load(file)

print(data)
