"""
Using str.join() to join a list
"""

friends = ["Rolf", "Anne", "Charlie"]
print(f"My friends are {friends}.")
#output is My friends are ['Rolf', 'Anne', 'Charlie'].

comma_separated = ', '.join(friends)
print(f'My friends are {comma_separated}.')
#output is My friends are Rolf, Anne, Charlie.

