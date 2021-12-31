"""
Loops are used to repeat things a number of times

2 types of Loops in Python: While and For Loops
"""

"""
Each time after the body of while loop is executed,
the while loop will be exited and return to evaluate
whether the while condition is true. If true, body of while
loop is executed.. Else, the program will move on
to the next statement...

While Loop will run as long as condition is
true
to prevent infinite while loop,
we add is_learning = False to the end of
while loop so 'You're Learning' will only
be printed once...
"""
# is_learning = True # Boolean
# while  is_learning:
#     print("You're learning!")
#     is_learning = False

# is_learning = True # Boolean

# while is_learning:
#     print("You're learning!")
#     user_input = input("Are you still learning? ")
#     is_learning = user_input == "yes"
    
# while is_learning:
#     print("You're learning!")
#     is_learning = input("Are you still learning? ")

user_input = input("Do you wish to run the proogram? (yes/no): ")
while user_input == "yes":
    print('We are running!')
    user_input =  input("Do you wish to run the program? (yes/no): ")

print("We stopped running!")
