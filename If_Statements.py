# friend = "Rolf"
# user_name = input('Enter your name: ')

""" This statement will always execute  """
# if True:
#     print("Hello, friend!")
"""
when condition is true, body of if statement 
or the print statement (in this case) 
will be executed
otherwise, the else statement will be
executed.
"""
# if user_name == friend:
#     print("Hello, friend!")
# else:
#     print("Hello, stranger!")

"""
condition in if statement can also be a 
boolean value
"""
# name = input("Enter your name: ")
# # name will always be true if its not empty
# if name:
#     print("We know your name!")

friends = ["Rolf", "Anne", "Bob"]
family = ["Jen", "Charlie"]

user_name = input('Enter your name: ')

"""
In this case, because friends and family are
of the data type List, whereas user_name is a
string hence we cannot use boolean comparsion
operators. Instead, we use the keyword 'in'.

The  'in' keyword checks for whether the 'user_name'
is a value contained within the 'friends' collection
"""
if user_name in friends:
    print("Hello, friend!")
elif user_name in family:
    print("Hello, family!")
else:
    print("I dont know you!")

"""
elif is keyword for else if 
"""