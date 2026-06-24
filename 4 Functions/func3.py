# Write a function that takes a string and counts the vowels in it. 

def count(text):
    vowels = "aeiouAEIOU"
    count = 0
    for letter in text:
        if letter in vowels:
            count = count + 1
    return count

word = "Education"
vowel_count = count(word)

print("Vowels:", vowel_count)
