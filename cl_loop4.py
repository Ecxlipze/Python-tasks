# Guess-the-number game: the program picks a number, the user keeps guessing

secret_number = 7
guess = 0

while guess != secret_number:
    guess = int(input("Guess the number: "))

    if guess == secret_number:
        print("Correct!")
    elif guess > secret_number:
        print("Too high")
    else:
        print("Too low")

    