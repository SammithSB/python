""" 
Develop a python program to read an SRN and check if the SRN starts with "PES1" and ends with "0".
 The length of the SRN must be strictly 10. Display the appropriate results.
"""
import re


def find(text):
    pattern = re.compile(r'^(PES1).*0$')
    match = pattern.search(text)
    if match:
        print("Match found:", match.group())
    else:
        print("No match found")


def main():
    text = input("Enter a string: ")
    find(text)


main()
