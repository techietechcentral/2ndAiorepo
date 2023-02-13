# The print() function displays the contents of the parenthesis 
# and displays the string without quotations e.g
from turtle import clear


x = "Hello World"
print("x")
print('x')
print('-------------------------------------------') 
# this will print x on both occasions and not Hello World because the x 
# is put in parenthesis.
print(x) # NOTE x has no parenthesis
print('-------------------------------------------')
# The backslash (\) character is utilised 
# to escape apostrophes or other special characters in strings
print('What\'s the problem here?')
# we can use double quotations
print("What's the problem here?")
# or backslash if we have single and double quotes
print("What\'s the \"problem\" here?")
print('-------------------------------------------')
# The .upper() method transforms string characters into UPPERCASE 
# (not in place).
print(x)
print(x.upper())
print('-------------------------------------------')
# To change x itself, we must reassign it.
print(x)
x = x.upper()
print(x)
print('-------------------------------------------')
# The .lower() method transforms string characters into LOWERCASE (not in place).
print(x.lower())
print('-------------------------------------------')
# The .capitalize() method makes the first character in the string 
# UPPERCASE.
z = "how are you?"
print(z.capitalize())
w = "i am fine"
print(w.capitalize())
print('-------------------------------------------')
# How to use the round command
y = 1.5343566454
print(round(y,4))
v = 2.9669876908698
print(round(v,6))
s = .0987876565453
print(round(s,3))
print('-------------------------------------------')
# The .split() method splits on space as the default or desired separator.
x ="Hello World"
print(x.split())
print(x.split("o"))
print('-------------------------------------------')
# The .format method is employed to insert data into a string. 
# e.g. default prints in order
print("The {} {} {}".format("fox", "brown", "quick"))
# The .format can index
print("The {2} {1} {0}".format("fox", "brown", "quick"))
print('-------------------------------------------')
# The .format can use variable keys for readability
print("The {q} {b} {f}".format(f="fox", b="brown", q="quick"))
print('-------------------------------------------')

# The .format can create long decimal
result = 100/777
# \n adds line spaces
print(result, end = "\n\n\n\n")
print('-------------------------------------------')
# use value:width.precision f for formatting
# width is minimum length of string, padded with whitespace if necessary
# precision is decimal places
print("The result was {:1.3f}".format(result))
print("The result was {r:1.3f}".format(r=result))
print("The result was {r:1.9f}".format(r=result))
print("The result was {r:.3f}".format(r=result))
print('-------------------------------------------')
## String Indexing and Slicing ##
# Strings are iterable, meaning that they can return their elements one at a time.
# Strings are also immutable, meaning that their elements cannot be changed once assigned.
# They must be REASSIGNED to change them.
# Each character in a string is one element; this includes spaces and punctuation marks.
# Indexing enables us to call back one element.
# Slicing enables us to call back a range of elements.
print("\n\n")
# In Python, indexing starts at 0 (zero).
# slicing is inclusive at the lower bound (including).
# slicing is exclusive at the upper bound (up to, but not including the upper bound).
print ("\n")
my_first_string = "Hello World"
print(my_first_string[0])
print(my_first_string[1])
print(my_first_string[2])
print(my_first_string[3])
print(my_first_string[4])
print(my_first_string[5])
print(my_first_string[6])
print(my_first_string[7])
print(my_first_string[8])
print(my_first_string[9])
print(my_first_string[10])
print('-------------------------------------------')
# Use a colon to indicate a slicing operation; for example, 1:4 returns the 2nd (index 1), 
# 3rd (index 2) and 4th (index 3) elements, but not the 5th (index 4):
my_first_string = "Hello World"
# print(my_first_string[lower bound:upper bound]) --illustration
print(my_first_string[1:4])
print(my_first_string[1:6])
print(my_first_string[1:8])
print(my_first_string[0:8])
print(my_first_string[4:6])
print(my_first_string[6:10])
print(my_first_string[6:7])
print(my_first_string[6:8])
print('-------------------------------------------')
# In the absence of the upper bound, the slicing starts with the 1st index 
# indicated and displays everything beyond:
my_first_string = "Hello World"
print(my_first_string[1:])
print(my_first_string[6:])
print(my_first_string[5:])
print(my_first_string[9:])
print('-------------------------------------------')
# In the absence of the lower bound, the slicing starts from index 0 up to, but not including, the upper bound:
my_first_string = "Hello World"
print(my_first_string[:3])
print(my_first_string[:9])
print(my_first_string[:10])
print(my_first_string[:6])
print(my_first_string[:7])
print(my_first_string[:2])
