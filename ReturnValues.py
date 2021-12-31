"""
Return Values in Functions
"""
cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},

]

def calculate_mpg(car):
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg

    #whenever the function is called, the value of
    # car["mileage"] / car["fuel_consumed"] is assigned to
    #the variable mpg.

def car_name(car):
    name = f"{car['make']} {car['model']}"
    return name

# def print_car_info(car):
#     name = car_name(car)
#     mpg = calculate_mpg(car)
#     print(f'{name} does {mpg} miles per gallon.')

# for car in cars:
#     print_car_info(car)

def print_car_info(car):
    name = car_name(car)
    mpg = calculate_mpg(car)
    return f'{name} does {mpg} miles per gallon.'

for car in cars:
    print(print_car_info(car))

"""
Output:
Ford Fiesta does 50.0 miles per gallon.
Ford Focus does 48.57142857142857 miles per gallon.
Mazda MX-5 does 54.44444444444444 miles per gallon.
Mini Cooper does 131.91489361702128 miles per gallon.
"""

def divide(x,y):
    if y == 0:
       return "You tried to divide by zero!"
    else:
        return x/y

z = divide(10, 2)
print(z)
print(divide(6,0))