import re

phoneNumRegex = re.compile(r'\d{3,3,4}') #compiles to make a regex object
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found:', mo.group())  