# Text 
my_string = 'Hello, World!'
# Single Quotation Marks or Double Quotation Marks also can
print(my_string)
print('Hello, World!')

string_with_quotes = "Hello, it's me."
print(string_with_quotes)
# In this case, its better to use double quotation marks since there's a single quotation marks in it's. Using single quotation marks will cause the variable to contain only Hello, it which will return an error -- 'Hello, it's me.'

another_with_quotes = 'He said "You are amazing!" yesterday.'
print(another_with_quotes)

another_with_backslashes = "He said \"You are amazing!\" yesterday."
print(another_with_backslashes)
# another_again = "He said " You are amazing!" yesterday."
# print(another_again)  --. this gives syntax error

#Escaping (putting a backslash in front of a characrer) is used in Python to remove meaning from a character. In this case, we remove Python's meaning of "starting or ending a string"
#Python will no longer treat them as characters used to signal a string; now they are part of the string itself
#Not recommended practice

# Printing multi-line strings use 3 quotation marks 
multiline = """Hello, world.

My name is Yonoyu. Welcome to my program.
"""
print(multiline)



"""
This creates a string but you dont assign it to a variable so you can use this as comments in Python
"""

# Adding / Concatenate Strings, Numbers
name = 'Yonoyu'
greeting = "Hello," + name
print(greeting)

# Must convert the variable to a string using quotation marks or str() function
age = '35'
age1 = 30
age_as_str = str(age1)
print("You are " + age)
print("You are " + age_as_str)
