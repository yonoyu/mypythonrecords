# age = int(input('Enter your age: '))
# can_learn_programming = age > 0 and age < 150
# print(f'You can learn programming: {can_learn_programming}')


# age = int(input('Enter your age: '))
# usually_not_working = age < 18 or age > 65
# # negatives might get confusing so we changed to:
# usually_working = age >= 18 and age <= 65
# print(f'At {age}, you are usually not working: {usually_not_working}')
# print(f'At {age}, you are usually working: {usually_working}')

# print(bool(35))
# """ bool() function takes in a value and converts it to a boolean """
# print(bool("Rolf"))
# """ Both returns True """
# print(bool(0))
# print(bool(""))
# """ Both returns False """

"""
AND operator
True AND False: AND operator looks at the first value: True (in this case). If first value is True, AND gives u the second value
"""
# x = True and False
# print(x)
""" x returns False """
# x = 0 and 35
# print(x) # gives 0
""" AND gives you the first value if it's False otherwise it gives you the second value """
# x = 35 and 0
# print(x) # gives 0

""" 
OR operator
gives you the first value if it is True otherwise gives you the second value
"""
# x = 35 or 34
# print(x) # output is 35

# x = 0 or 23
# print(x) # output is 23

# name = ""
# surname = "Smith"
# greeting = name or f'Mr. {surname}'
# print(greeting)

# name = input('Enter your name: ')
# surname = input('Enter your surname: ') 
# greeting = name or f'Mr. {surname}'
# print(greeting)

""" negation operator NOT, sth u use with a Boolean """
print(not True) # False
print(not bool(35)) # False
print(not 35) # False
"""Python turns 35 into a boolean before applying 'not' """
