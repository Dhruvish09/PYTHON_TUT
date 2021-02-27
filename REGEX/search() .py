#The search() function searches the string for a match, and returns a Match object if there is a match.


import re

txt = "The rain in Spain"
x = re.search("Portugal", txt)
print(x)