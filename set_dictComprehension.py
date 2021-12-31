"""
Set & Dictionary Comprehensions
"""
# friends = ["Rolf", "ruth", "Jen", "charlie"]
# guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

# friends_lower = {friend.lower() for friend in friends}
# guests_lower = {g.lower() for g in guests}

# friends_intersection = friends_lower.intersection(guests_lower)

# present_friends = { 
#     name.title() 
#     for name in friends_lower.intersection(guests_lower)
# }
# print(present_friends) # output is {'Charlie', 'Rolf'}

# print(friends_lower.intersection(guests_lower)) # output is {'rolf', 'charlie'}

friends = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]
"""
Creating a dictionary
friends[i]: time_since_seen[i] access the i-th
element of the 'friends' list.
if  'i' was 0, it would access
friends[0] which is 'Rolf' and would associate
that with the value time_since_seen[0] aka 3.
"""
long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
}

print(long_timers) 
# {'Rolf': 3, 'Bob': 7, 'Jen': 15, 'Anne': 11}




long_timers = {
    friends[i]: time_since_seen[i]
    for i in range(len(friends))
    if time_since_seen[i] > 5 #not seen for greater than 5
}

print(long_timers) 
# {'Bob': 7, 'Jen': 15, 'Anne': 11}