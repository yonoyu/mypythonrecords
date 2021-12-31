""" 
Dictionaries allows you to store keys and values. iTS USEFFUL WHEN YOU KNOW THE KEY & YOU WANT TO GET THE VALUE

# Dictionary of a single element
friend_ages = {"Rolf": 24}

Rolf is the key and 24 is the value
"""

# friend_ages = {"Rolf": 24, "Adam":30, "Anne": 27}
# print(friend_ages["Rolf"]) # Output is 24

"""
Add keys to a Dictionary
"""
# You are accessing a key of the Dictionary and you are setting a value in it
# friend_ages["Bob": 20] is wrong because you are accessing both the key and value in one place
# friend_ages["Bob"] = 20
"""
Change/Update an existing key in a Dictionary
"""
# friend_ages["Rolf"] = 25
# print(friend_ages) # Output is {'Rolf': 25, 'Adam': 30, 'Anne': 27, 'Bob': 20}

"""
Storing information  - list or tuple of dictionaries
"""
# friends = (
#     {"name": "Rolf Smith", "age": 24 },
#     {"name": "Adam Wool", "age": 30 },
#     {"name": "Anne Pun", "age": 27 }
# )

# print(friends[0]["name"]) # Output is Rolf Smith
""" the above is same as 
friend = friends[0]
print(friend["name"])
"""

"""
Turning data into a Dictionary: dict() function
"""
# This is a list of Tuples
friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
friend_ages = dict(friends)
print(friend_ages)
# {'Rolf': 24, 'Adam': 30, 'Anne': 27}