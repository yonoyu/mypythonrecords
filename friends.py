"""
# Ask the user for a list of 3 friends
# For each friend, we'll tell the user whether they are nearby
# For each nearby friend, we'll save their name to 'nearby_friends.txt'

# hint: readlines()
# copying people.txt to nearby_friends.txt selectively
@ which people who are friends who are also nearby
"""
#friends = input('Enter 3 friend names, separated by commas (no spaces, please): ').split(',')
friends = input('Enter 3 friend names, separated by commas: ') #string
friend_list = friends.split(',') #list

people = open('people.txt', 'r')
people_nearby = people.readlines() #read the file line by line and outputs them in a list [Line1, line2, line3]

people.close()

friends_set = set(friend_list)
people_nearby_set = set(people_nearby)

friends_nearby_set = friends_set.intersection(people_nearby_set)

nearby_friends = open('nearby_friends.txt', 'w')

for friend in friends_nearby_set:
    print(f'{friend} is nearby!')
    nearby_friends.write(friend)

nearby_friends.close()


