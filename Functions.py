"""
Creating our own Functions
Functions always start with the 'def' keyword
"""
# def greet():
#     name = input("Enter your name: ") 
#     print(f'Hello, {name}!')

"""
Python only reads the 1st line: def greet() 
and does not run the code in the body of the greet()
function. Hence when we run the code, nothing
happens as the code is never executed.
We've only created the function.
"""

"""
To run the function, we use
"""
# greet()


"""
Should make your functions short rather than long
as the longer the functions, the more jumping around
you are going to see in your programs, and its gonna
make it difficult to read
"""

"""
Functions can call other functions.
Calling is the same as executing.
You can only call the function ONLY after its 
been defined but not before.
"""

"""
Arguments and Parameters that we can use to make
our functions generic so that we can use them 
with mutiple different pieces of data.
"""

# def calculate_mpg():
#     """
#     Car Dictionary:
#     """
#     car = {
#         "make": "Ford",
#         "model": "Fiesta",
#         "mileage": 23000,
#         "fuel_consumed": 460
#     }

#     mpg = car ["mileage"]/car["fuel_consumed"]
#     name = f"{car['make']} {car['model']}"
#     print(f'{name} does {mpg} miles per gallon.')

# calculate_mpg()

# def calculate_mpg(car_to_calculate):
#     mpg = car_to_calculate ["mileage"] / car_to_calculate["fuel_consumed"]
#     name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
#     print(f'{name} does {mpg} miles per gallon.')

# calculate_mpg({
#     "make": "Ford",
#     "model": "Fiesta",
#     "mileage": 23000,
#     "fuel_consumed": 460
# })

cars = [
    {"make": "Ford", "model": "Fiesta", "mileage": 23000, "fuel_consumed": 460},
    {"make": "Ford", "model": "Focus", "mileage": 17000, "fuel_consumed": 350},
    {"make": "Mazda", "model": "MX-5", "mileage": 49000, "fuel_consumed": 900},
    {"make": "Mini", "model": "Cooper", "mileage": 31000, "fuel_consumed": 235},

]


# def calculate_mpg(car_to_calculate):
#     mpg = car_to_calculate ["mileage"] / car_to_calculate["fuel_consumed"]
#     name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
#     print(f'{name} does {mpg} miles per gallon.')

# calculate_mpg(cars[1])

#output is
# Ford Focus does 48.57142857142857 miles per gallon.

"""
To print out the whole list of cars data,
use for ___ in ___ cars
"""
# for car_to_calculate in cars:
#     calculate_mpg(car_to_calculate)

"""
Output is:
Ford Fiesta does 50.0 miles per gallon.
Ford Focus does 48.57142857142857 miles per gallon.
Mazda MX-5 does 54.44444444444444 miles per gallon.
Mini Cooper does 131.91489361702128 miles per gallon.
"""

def calculate_mpg(car_to_calculate, intro):
    print(intro)
    mpg = car_to_calculate ["mileage"] / car_to_calculate["fuel_consumed"]
    name = f"{car_to_calculate['make']} {car_to_calculate['model']}"
    print(f'{name} does {mpg} miles per gallon.')

for car_to_calculate in cars:
    calculate_mpg(car_to_calculate, "New car")

"""
New car
Ford Fiesta does 50.0 miles per gallon.
New car
Ford Focus does 48.57142857142857 miles per gallon.
New car
Mazda MX-5 does 54.44444444444444 miles per gallon.
New car
Mini Cooper does 131.91489361702128 miles per gallon.
"""