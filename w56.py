""" 
Develop a python program to read a C-program and display all the keywords. 
Display the keywords and their locations. Search for the "int, float, while, for, if, if else, 
else, switch, printf and scanf" keywords in the program.
"""
import re
text = "for (i=1;i<=10;++i){ if (i==3)continue; if (i==7) break; printf ('%d ',i);} switch(expression) {case '1':break;case '5':break; default;}"
# finditer iterates over the matches makign it possible to access multiple matches location
print([[m.group(), m.start(), m.end()] for m in re.finditer(
    r'(int)|(float)|(while)|(if else)|(if)|(else)|(switch)|(printf)|(scanf)', text)])
