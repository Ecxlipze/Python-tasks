# Count how many lines and words are in a file. 

with open("my_file.txt", "r") as file:
    content = file.read()

lines = content.splitlines()
words = content.split()

print("Lines:", len(lines))
print("Words:", len(words))
