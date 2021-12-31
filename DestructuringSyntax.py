"""
Destructuring (also called unpacking) is where we take a 
collection, like a list or a tuple, and we break it up 
into individual values. This is quite useful, as it 
enables us to do things like destructuring assignments, 
where we assign values to several variables at once 
from a single collection.
"""

"""
Takes the first value of tuple and puts it into a new variable 
called 'eur'
"""
currencies = 0.8, 1.2 # Tuple
usd, eur = currencies

friends = [("Rolf", 25), ("Anne", 37), ("Charlie", 31), ("Bob", 22)]
for name, age in friends:
    print(name, age)
    print(f'{name} is {age} years old.')