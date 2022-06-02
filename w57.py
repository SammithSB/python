""" 
Develop a python program to read convert a date of yyyy-mm-dd format to dd-mm- yyyy format.
"""
import re


def change_format(date):
    return re.sub(r'(\d{4})-(\d{2})-(\d{2})', r'\3-\2-\1', date)
    # re.sub is used to replace the matched string with the new string.


date = input("Enter a date in yyyy-mm-dd format: ")
print(change_format(date))
