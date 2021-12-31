"""
Dunder/Magic Methods
In a class, not all methods are the same.
Python sometimes makes a distinction depending on the 
method name
init is a special method because Python calls it
automatically for you
"""
class Student:
    def __init__(self, name):
        self.name = name

"""
List is somehow an object. Everything in Python is 
an object.
Anything we can do with our list, we can do in classes
"""      
movies = ['Matrix', 'Finding Nemo']
print(movies.__class__) #output: <class 'list'>
print('hi'.__class__) #output: <class 'str'>

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    # used to return a string representing an object
    def __repr__(self):
        return f'<Garage {self.cars}>'
    
    #RETURNS some useful insights about the item itself
    def __str__(self):
        return f'Garage with {len(self)} cars.'
        
ford = Garage()
print(ford.cars) #output: [] empty list
#list operations
ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(ford.cars) #output: ['Fiesta', 'Focus']
# print(len(ford.cars)) #output: 2
print(len(ford)) #output: 2
print(ford[0]) #Garage.__getitem__(ford, 0) #output: Fiesta

#need to define __getitem__ before you can for loop it
for car in ford:
    print(car)

print(repr(ford)) #<Garage ['Fiesta', 'Focus']>
print(str(ford)) #Garage with 2 cars.