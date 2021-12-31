"""
    Types of Error:
    1. IndexError

index out of range; index that doesnt exist or incorrect
Found in lists, dictionary etc etc


    2. KeyError
    3. NameError

undefined variables
check quotation marks 

    4. AttributeError
    5. NotImplementedError
    6. RuntimeError
    7. SyntaxError
    8. IndentationError
    9. TabError
    10. TypeError
    11. ValueError
    12. ImportError

    13. DepreciationWarning

    no longer the best way of doing sth

Really good to catch errors on your user interface

"""
#NotImplementedError
# class User:
#     def __init__ (self, username, password):
#         self.username = username
#         self.password = password

#     def login(self):
#         raise NotImplementedError('This feature has not been implemented yet.')

# Error = User('user', 1234)
# print(Error.login())


class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __repr__(self):
        return f'<Car {self.make} {self.model}>'

class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
     
    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a \'{car.__class__.__name__}\' to the garage but you can only add \'Car\' objects.')
        self.cars.append(car)

ford = Garage()
fiesta = Car('Ford', 'Fiesta')


try:
    ford.add_car('Fiesta')
except TypeError: #only gonna catch this error
    print('Your car was not a Car!')
except ValueError:
    print('Something weird happen...')
finally: #this will run every time whether or not an error happened
    print(f'The garage now has {len(ford)} cars.')