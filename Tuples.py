""" 
Tuples are similar to Lists in that they are used to allows us to store multiple values in a single variable. 
To create/define a tuple, we use round brackets/ parentheses. Though round brackets are optional, but its good practice to use them
it's the commas which tell Python something is a tuple not the
parentheses...
Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.
"""
short_tuple = ("Rolf", "Bob")
can_be_tuple = "Rolf", # comma turns it into a tuple
""" 
Cannot add to an existing tuple; its not editable. To add new element or delete element, create a copy of the tuple with the updated element
"""
friends = ("Rolf", "Bob", "Anne")
friends = friends + ("Jen",)
print(friends)