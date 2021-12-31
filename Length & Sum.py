"""
Length & Sum
len(): length of collection
sum()
"""
grades = [80, 75, 90, 100]

total = sum(grades)
print(total)

length = len(grades)
print(length)

average = total/length
print(average)

grades = [80, 75, 90, 100]  #List
grades = (80, 75, 90, 100)  #Tuple
grades = {80, 75, 90, 100}  #Set
"""
In this case, using set as data structure for
grades is a bad idea since set does not allow
duplicate values..hence students' grades cannot
be stored in sets as there'll be duplicate values 
inevitably
"""