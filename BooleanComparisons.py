age = 20
is_over_age = age >= 18
""" age >= 18 is a boolean comparison & evaluates to True """
is_under_age = age < 18
is_twenty = age == 20
""" = is an assignment operator
    == exactly equal to 
"""
my_number = 5
user_number = int(input('Enter a number: '))
matches = my_number == user_number
print(my_number == user_number)
print(f'You got it right: {matches}')
""" If user enters 5, output prints True else False """