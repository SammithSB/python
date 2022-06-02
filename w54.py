""" 
Develop a python program to read 20 random numbers. Display all the odd numbers from 
this list which are of length 2 and 4.
"""
import random
import re
for i in range(20):
    num = random.randint(0, 9999)
    pattern = re.compile(r'^[0-9][13579]$|^[0-9]{3}[13579]$')
    match = pattern.search(str(num))
    if match:
        print(num)
