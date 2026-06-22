# Try to open a file that doesn't exist and handle the error gracefully. 

try:
    with open("file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")
