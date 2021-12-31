"""
if y is assigned a defualt value, if there 
is no second parameter add(5) instead of add(5,10)
then y will be 3 by default
"""
"""
default values must go at the end! 

def add(y, x=4)
    total = x + y
    return total
"""
from typing import DefaultDict


def add(x, y=3):
    total = x + y
    return total

# print(add(5,10)) #output: 15
# print(add(5)) #output: 8
# print(add(x=3)) #output: 6
# print(add(x=5, y=2)) #output: 7
# print(add(x=5, 2)) 
"""
error as the unamed argument 2 cannot be used 
#after an argument that has a name. The subsequent arguments must
have a name if the 1st argument is named.
"""
# print(add(5, y=2)) #output: 7
# print(add(y=2)) #TypeError: add() missing 1 required positional argument: 'x'
"""
a positional argument is just an argument that does
not have a name
named argument aka keyword argument: y=2
"""

print(1, 2, 3, 4, 5) #1 2 3 4 5
print(1, 2, 3, 4, 5, sep="-") #1-2-3-4-5
print(1, 2, 3, 4, 5, sep=" - ") #1 - 2 - 3 - 4 - 5



default_y = 3
def add(x, y=default_y):
    total = x + y
    print(total)

add(2) #output: 5

"""
This practice not recommended..highly discouraged
to use variables as default vaule..if you need
to change the value of default_y.
Output will be unchanged from the previous value
"""
default_y = 4
add(2)