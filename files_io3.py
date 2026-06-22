# Take a name from the user and append it to a file (like a contact list). 

name = input("Enter name: ")

with open("contacts.txt", "a") as file:
    file.write(name + "\n")
print("Name added to contacts.")
