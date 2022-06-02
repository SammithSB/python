# Develop a python program to count all the occurrences of vowels, consonants and digits from the given text using Regular expressions.
import re


def count_vowels(text):
    vowels = re.findall('[aeiou]', text)
    return len(vowels)


def count_consonants(text):
    consonants = re.findall('[bcdfghjklmnpqrstvwxyz]', text)
    return len(consonants)


def count_digits(text):
    digits = re.findall('\d', text)
    return len(digits)


def main():
    text = input("Enter a string: ")
    print("The number of vowels is:", count_vowels(text))
    print("The number of consonants is:", count_consonants(text))
    print("The number of digits is:", count_digits(text))


main()
