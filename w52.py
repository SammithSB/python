"""
Develop a python program to match all the occurrences of a word which has an "A/a" followed by
i. Zero or more b's 
ii. Zero or one b
iii. One and more b's
iv. Four consecutive b's followed by a “c”
"""
import re


def main():
    text = input("Enter a string: ")
    pattern = re.compile(r'ab*|Ab*|ab?|Ab?|ab+|Ab+|abbbbc|Abbbbc')
    match = pattern.search(text)
    if match:
        print("Match found:", match.group())
    else:
        print("No match found")


main()
