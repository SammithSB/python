"""Develop a python program to find all the urls in given string."""
import re
text = "Visit http://www.google.com for more information"
pattern = re.compile(
    r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
match = pattern.findall(text)
print(match)
