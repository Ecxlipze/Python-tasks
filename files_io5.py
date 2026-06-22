# Read a .txt file and show only the lines that contain a specific word. 

word = "file"

with open("my_file.txt", "r") as file:
    lines = file.readlines()
for line in lines:
    if word in line:
        print(line)
