"""
Handling User Errors:
"""
# def power_of_two():
#     user_input = input('Please enter a number: ')
#     try:
#        n = float(user_input)
#     except ValueError:
#         print('Your input is invalid!')
#         n = 0 #no return statement and thus the function returns None
#     else: #only runs if there was no error aka try block was successful
#         n_square = n ** 2
#     finally: #if input was invalid, n_square never gets its value assigned thus will raise an error when we try to
#         #access in the finally block
#         return n_square

# print(power_of_two()) 

# def power_of_two():
#     user_input = input('Please enter a number: ')
#     try:
#        n = float(user_input)
#     except ValueError:
#         print('Your input is invalid!')
#         return 0 #no return statement and thus the function returns None
#     finally: #if input was invalid, n_square never gets its value assigned thus will raise an error when we try to
#         #access in the finally block
#         #return in finally block takes precedence over anything except block
#         n_square = n ** 2
#         return n_square

# print(power_of_two()) 


def power_of_two():
    user_input = input('Please enter a number: ')
    try:
       n = float(user_input)
       n_square = n ** 2
       return n_square
    except ValueError:
        print('Your input is invalid!')
        return 0 

print(power_of_two()) 
print(power_of_two()) 