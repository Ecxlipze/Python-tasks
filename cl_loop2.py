# FizzBuzz: 1 to 50 — "Fizz" for multiples of 3, "Buzz" for 5, "FizzBuzz" for both. 

for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

