"""
First Order Functions:
Functions are first class functions;
They behave in exactly the same way as an integer
or string would when you assign them to a 
variable or you pass them into a function
as an argument
When you have a first class
function, you can assign it to
other variables, as shown below
"""
# def greet():
#     print("Hello")

# hello = greet
# hello() #output: Hello

"""
Pass a function into other function.
Assume the value of this parameter func
will be a function.
"""
# def before_and_after(func):
#     print("Before...")
#     func()
#     print("After...")

# def greet():
#     print("Hello")

#Passing through the greet function
#Using greet() as a parameter will
#result in null value as there is no
#return value
# before_and_after(greet)

"""
Output:

Before...
Hello
After...
"""



"""
Higher Order Functions:
Function that accepts another function
as an argument
"before_and_after" is a higher-order
function
"""
#Dictionary
#seq represents an iterable:tuple, list
operations = {
    "average": lambda seq:sum(seq)/len(seq),
    "total": lambda seq: sum(seq),
    "top": lambda seq: max(seq)
}

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Bob", "grades": (56, 78, 80, 90)},
    {"name": "Jen", "grades": (98, 90, 95, 99)},
    {"name": "Anne", "grades": (100, 100, 95, 100)},
]
#iterate over them
for student in students:
    name = student["name"]
    grade = student["grades"]

    print(f'Student: {name}')
    operation = input("Enter 'average', 'total', or 'top': ")

    #We are accessing the 'average' key of the 'operations' dictionary
    result = operations[operation](grade)
    print(result)