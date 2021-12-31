""" 
Lists allow us to store multiple values in a single variable.
To create a list, we use square brackets
"""
friends  = ["Rolf", "Bob", "Anne"]
""" 
Accessing the value of a single friend (element) in the list
"""
print(friends[0])
""" 
len() gives the length / size (no. of elements inside) of list
"""
print(len(friends))
""" 
Accessing Nested Lists: [outer_list][inner_list]
"""
friends  = [["Rolf", 24], ["Bob", 30], ["Anne", 27]]
print(friends[0][0]) # Gives Rolf
print(friends[1][0]) # Gives Bob

# Best Practices
# friends = [
#   ["Rolf", 24],
#   ["Bob", 30], 
#   ["Anne", 27],
#   ["Bob", 30], 
#   ["Anne", 27],
#   ["Charlie", 37],
#   ["Jen", 25],
#   ["Adam", 29]
# ]
""" 
Add an element to end of a list: list.append()
"""
friends  = ["Rolf", "Bob", "Anne"]
friends.append("John")
print(friends)
""" 
Remove an element from a list: list.remove()
"""
friends  = ["Rolf", "Bob", "Anne", "John"]
friends.remove("Bob")
print(friends)
""" 
Remove an element from a sublist: list.remove()
"""
friends  = [["Rolf", 24], ["Bob", 30], ["Anne", 27]]
friends.remove(["Anne", 27]) # friends.remove("Anne") not applicable
print(friends)
