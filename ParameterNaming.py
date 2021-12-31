"""
OOP - Parameter Naming
OOP is used to help conceptualise the 
interactions between objects
You can put objects inside lists, tuples or dictionaries
"""

class Movie:
    def __init__(self, name, year):
        self.name = name
        self.year = year

# print(Movie('The Matrix', 1994).name)
matrix = Movie('The Matrix', 1994)
print(matrix.name)