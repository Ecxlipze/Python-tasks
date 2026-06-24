# Write a function is_prime(n) that returns whether a number is prime. 

def is_prime(n):
    if n <= 1:
        return False
    for number in range(2, n):
        if n % number == 0:
            return False
    return True

print(is_prime(7))
print(is_prime(4))
