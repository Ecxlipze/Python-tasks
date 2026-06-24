# Use a default argument: greet(name, lang="urdu") that greets based on the language

def greet(name, lang="urdu"):
    if lang == "urdu":
        print(f"Assalam o Alaikum {name}")
    elif lang == "english":
        print(f"Hello {name}")
    else:
        print(f"Hi {name}")


greet("Ali")
greet("Sara", "english")
