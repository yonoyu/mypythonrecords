friend_ages = {'Rolf': 25, 'Charlie': 31, 'Anne': 37, 'Bob': 22}
# print(friend_ages["Rolf"]) # gives 25

# for name in friend_ages:
#     print(name)
"""
This iterates over keys of the dictionary; ignoring the values

Output is: 
Rolf
Charlie
Anne
Bob
"""

# for age in friend_ages.values():
#     print(age)
"""
This iterates over values of dictionary

Output is:
25
31
37
22
"""

for name,age in friend_ages.items():
    print(f'{name} is {age} years old.')
"""
dict.items() allow you to iterate over both key and value

Output is:
Rolf is 25 years old.
Charlie is 31 years old.
Anne is 37 years old.
Bob is 22 years old.
"""
