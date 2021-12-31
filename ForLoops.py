"""
Used to repeat something a defined number of times
Similar to 'for each loop' in non-Python Language
Iterables: sets, lists, tuples, dictionaries 
"""
# friends = ["Rolf", "Anne", "Jen"]

# for friend in friends:
#     print(friend)
"""
One iteration through the body of for loop 
for every element in the 
list - friends

Output is:
Rolf
Anne
Jen
"""

# elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# for index in elements:
#     print(index)
# for index in elements:
#     print("Hello, world!")

# for index in range(10):
#     print("Hi")
# # output is Hi 10 times

# for index in range(5,10):
#     print(index)
# # output is 5,6,7,8,9

# for index in range(2, 20, 3):
#     print(index)
# output is 2,5,8,11,14,17 

# students = [
#     {"name": "Rolf", "grade": 90},
#     {"name": "Bob", "grade": 78},
#     {"name": "Jen", "grade": 100},
#     {"name": "Anne", "grade": 80}
# ]

# for student in students:
#     name = student["name"]
#     grade = student["grade"]
#     print(f"{name} has a grade of {grade}.")

"""
Output: 
Rolf has a grade of 90.
Bob has a grade of 78.
Jen has a grade of 100.
Anne has a grade of 80.
"""

"""Finding prime numbers with For Loops using range()"""
"""if n is divisible by any number from 2 to n-1, it is
   not a prime number """
for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(f'{n} equals {x} * {n//x}')
            break # break is inside 2 for loops, but it only
                  # affects the closest for loop
    else:
        print(f'{n} is a prime number.')