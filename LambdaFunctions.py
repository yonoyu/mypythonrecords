"""
Lambda Functions:
Are used to get inputs,
do a small amount of processing and return outputs.
Lambda not used for performing actions.
Functions can do two things, they can perform an action or
they can return an output or they can do both
""" 

"""
def divide(x, y):
    return x/y
To rewrite the above normal function into a Lambda function:
"""
#here we are creating a lambda function and we are
#assigning it to the 'divide' variable
#here we got to inputs x and y, after lamda keyword.
#returns division value of x/y
# divide = lambda x, y: x / y
# print(divide(15, 3))

"""
if you create a lamda function without assigning it
to a variable, Python will create this function &
immediately destroy it.
Python realises that you cant use this function elsewhere
because you have no way of referring it.
"""
# lambda x, y: x / y
# This is same as divide = lambda x, y: x / y
# print(divide(15, 3))
# CRAP code
# print((lambda x, y: x / y)(15, 3))

"""
Lambda functions can at times provide more simplicity to code.
"""

# def average(sequence):
#     return sum(sequence) / len(sequence)

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]

# for student in students:
#     print(average(student["grades"]))

"""
Output is:
88.0
76.0
95.5
98.75
"""

"""
To make the program simpler with lambda functions
but there are better scenarios to use it
"""
average = lambda sequence: sum(sequence) / len(sequence)

for student in students:
    print(average(student["grades"]))

"""
Output:
88.0
76.0
95.5
98.75
"""