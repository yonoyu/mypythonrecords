"""
ListComprehension2 with conditionals 
"""
ages = [22, 35, 27, 21, 20]
""" Get only the odd ages given a list of ages"""
""" 
Puts the value age for age(new variable you're creating
in the ages list; its gonna put every 'age' in the ages list
into the new list: odds.
To get only the odd ages, add an if statement: age % 2 == 1

Big picture: puts the value (contained in aged) when if condition
is true into the new list: odds
"""
# odds = [aged for aged in ages if aged % 2 == 1]
# print(odds) # output is [35, 27, 21]

""" The two codes have the same meaning """
odds = []
for aged in ages:
    if aged % 2 == 1:
        odds.append(aged)
print(odds)

friends = ["Rolf", "ruth", "Jen", "charlie"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

"""
First Approach: set function
we want a final list of those 'friends' that have come
to the party.
Finding who are both guests and friends of yours truly 
AKA intersection
To do so, convert each element in both lists 
to lowercase for easy comparison
To find intersection, convert the lists into sets
"""
# friends_lower = set([friend.lower() for friend in friends])
# guests_lower = set([g.lower() for g in guests])
# similarity = friends_lower.intersection(guests_lower)
# print(similarity) # output is {'charlie', 'rolf'}
"""
But we want output of the first letter of names to be capitalised
so we are not using set functions..onto 2nd approach
"""
"""
Turn every friend in our friends list into a lower case
so that we can compare with the guests list
we want a final list of those 'friends' that have come
to the party.
Second Approach: List comprehension
"""
""" 
put each of the names of the 'guests' inside 
new list: present_friends, if that name turned to lowercase 
(name.lower) is in 'friends_lower' list
"""
friends_lower = [friend.lower() for friend in friends]
present_list = [
    name.title() #new thing you want to put in your list
    for name in guests #iteration over an existing iterable 'guests'
    if name.lower() in friends_lower # list comprehensions
]
print(present_list)

"""
newlist = [expression for item in iterable if condition == True]
The return value is a new list, leaving the old list unchanged.
The condition is like a filter that only accepts the items that valuate to True.
"""