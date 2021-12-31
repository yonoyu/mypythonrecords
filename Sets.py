""" 
Sets are another collection like Lists and Tuples, it allows us to store multiple values in a single variable.
Sets are unordered and dont contain duplicate elements
To create a list, we use curly braces
"""
# art_friends = {"Rolf", "Anne"}
# science_friends = {"Jen", "Charlie"}
# """ 
# Add an element to a set : set.add()
# we dont know at which postioning of the set Jen will be added to
# """
# art_friends.add("Jen")
# print(art_friends)
# """ 
# Remove an element from a set: set.remove()
# """
# art_friends.remove("Anne")
# print(art_friends)

""" 
Main useful functon of Sets: Easy to compare one set against another --> Set Theory
"""
art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

""" 
Eradicates elements that are found in both sets; takes away the elements from science_friends in art_friends
Difference does elements in one set but not the other
"""
# art_but_not_science = art_friends.difference(science_friends)
# print(art_but_not_science) # {"Rolf", "Anne"}
# """ 
# Eradicates elements that are found in both sets; Takes away the elements from art_friends in science_friends
# """
# science_but_not_art = science_friends.difference(art_friends)
# print(science_but_not_art) # {'Charlie'}

""" 
Symmetric Difference: takes all the elements that are not in both sets.
"""
# not_in_both = art_friends.symmetric_difference(science_friends)
# print(not_in_both) #removes Jen and combines the rest in this case
# {'Anne', 'Charlie', 'Rolf'}

""" 
Interesection: takes all the elements that are IN BOTH sets.
"""
# art_and_science = art_friends.intersection(science_friends)
# print(art_and_science) # Output is {'Jen'}

""" 
Union: Combines all the elements IN BOTH sets.
"""
# all_friends = art_friends.union(science_friends)
# print(all_friends) # Output : {'Charlie', 'Anne', 'Rolf', 'Jen'}

