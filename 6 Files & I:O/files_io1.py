# Write a few lines to a text file, then read it back and display it on screen. 

with open("my_file.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("This is my first file\n")
    file.write("File handling is useful\n")

with open("my_file.txt", "r") as file:
    content = file.read()

print(content)
