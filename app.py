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
     
    #if car was a string, {car.__class__.__name__} gives str else gives Car
    def add_car(self, car):
        #isinstance checks if car is an instance of type (Class) Car
        #if cat is an instance of Car, proceeds to self.cars.append
        if not isinstance(car, Car):
            raise TypeError(f'Tried to add a \'{car.__class__.__name__}\' to the garage but you can only add \'Car\' objects.')
        self.cars.append(car)
        #print('This method is a work in progress.')
        # raise NotImplementedError("We can't add cars to the garage yet.")
        

ford = Garage()
car = Car('Ford','Fiesta')
ford.add_car(car)
print(len(ford)) 



