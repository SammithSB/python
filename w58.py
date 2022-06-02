""" 
Develop a python program to find all three, four and five characters long word in a string.
"""
import re
text = "The quick brown fox jumps over the lazy dog"
# \b is used to match the word boundary \w is used to match any word character
pattern = re.compile(r'\b\w{3,5}\b')
match = pattern.findall(text)
print(match)
