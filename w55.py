"""
Develop a python program to search word in a string and display the location within the 
original string where the pattern occurs. If the pattern occurs multiple times, 
then display all the locations. Replace the pattern with another word.
"""
import re
text = "Kohli ran for a quick run while Rohit was busy looking at the ball, it was a disaster and Rohit did not see Kohli run at all and ended up running Kohli out"
pattern = re.compile(r'Kohli')
# finditer iterates over the matches makign it possible to access multiple matches location
print([[m.start(), m.end()] for m in re.finditer(r'(Kohli)', text)])
