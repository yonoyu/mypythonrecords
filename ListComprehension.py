numbers = [0, 1, 2, 3, 4]
# doubled_numbers = []

# for number in numbers:
#     doubled_numbers.append(number * 2)

# print(doubled_numbers) #output is [0, 2, 4, 6, 8]

# doubled_numbers = [number * 2 for number in numbers] #similar to for loop above
# print(doubled_numbers) # output: [0, 2, 4, 6, 8]

# doubled_numbers = [number * 2 for number in range(5)] 
# print(doubled_numbers) # output: [0, 2, 4, 6, 8]

#repetitive numbers; output is [5, 5, 5, 5, 5]
# doubled_numbers = [5 for number in range(5)]
# print(doubled_numbers)

# friend_ages = [22, 31, 35, 37]
# age_strings = [f'My friend is {_} years old.' for _ in friend_ages]
# print(age_strings)
""" output:
 ['My friend is 22 years old.', 
 'My friend is 31 years old.', 
 'My friend is 35 years old.', 
 'My friend is 37 years old.']
"""
# names = ["Rolf", "Bob", "Jen"]
# lower = [name.lower() for name in names]
# print(lower) #output is ['rolf', 'bob', 'jen']

friendd = input("Enter your friend's name: ")
friends = ["Rolf", "Bob", "Jen", "Charlie", "Anne"]
friends_lower = [name.lower() for name in friends]

#To check if the input matches one of the element in the list
# if friendd.lower() in friends_lower:
#     print(f'{friendd} is one of your friends.')
# Using .lower() will allow matching unless of whether input is
# capitalised or not e.g inputting BOB, bob or Bob will still match.

""" title casing:  .title()
Every word in the string will have the first letter as 
uppercase and the remaining letters as lowercase """

if friendd.lower() in friends_lower:
    print(f'{friendd.title()} is one of your friends.')