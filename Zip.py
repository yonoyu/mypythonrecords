"""
the zip function
enables you to combine 2 separate lists
into one
friend = ["Rolf", "Adam", "Anne"]
age = [24, 30, 27]

output:
friends = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]
"""

"""
runs a zipper through each of these lists,
closing them up and combining them into one
list where each element of the new list is a tuple
of elements
"""
friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = dict(zip(friends, time_since_seen))
print(long_timers)
# output: {'Rolf': 3, 'Bob': 7, 'Jen': 15, 'Anne': 11}
list_long_timers = list(zip(friends, time_since_seen))
print(list_long_timers)
# output: [('Rolf', 3), ('Bob', 7), ('Jen', 15), ('Anne', 11)]
# list of tuples

"""
zip will just ignore other elements in the list that 
dont match the length of the other lists.
"""