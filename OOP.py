"""
Dictionaries and Objects
When we call a class that creates a blank object
and that gets passed to the Dunder 'init' method as self.
Then we can modify that by creating new variables inside
the self object.

When we define a variable inside an object, its no longer
a variable, its a property of the object.

when we define a function like the 'average' function
inside a class, that's no longer called a function its
a METHOD

student_one and student_two are of type Student
"""
my_students = {
    'name': 'Rolf Smith',
    'grades': [70, 88, 90, 99]
}

# print(my_students['name']) #output: Rolf Smith
# print(my_students['grades'][0]) #output: 70

# def average_grades(students):
#     return sum(students['grades'])/len(students['grades'])
# print(average_grades(my_students))

"""
these functions with 2 underscores in front and back are
special functions aka Dunder functions
 __init__() takes 3 parameters
"""
#define object structure
#define the data we are performing on and the functions
# performing the actions
class Student:
    def __init__(self, new_name, new_grade):
        self.name = new_name #self is blank object
        self.grades = new_grade #self is not blank object now
    
    def average(self):
        return sum(self.grades) / len(self.grades)
"""
we use a dot(.) to access sth inside of the self
object 
because self is a blank object, it does not have a variable
called 'name' inside it
self.name = new_name creates a new variable called name that
lives inside the self object.
#creates a new object of type 'student' by calling the class 
"""
"""
What is an object?
an empty thing that can allows us to store data
or store actions
We're going to tell it what data to store
"""
# When the object is first created, it immediately calls
# Dunder 'init' function
"""
Student is creating an empty object called self.
The new empty object that was just created gets passed
to 'self' as the first parameter.
#self is a blank object that has essentially nothing in it
ThEN 'Rolf Smith' is given as new_name (second parameter)
and the list as third parameter
IMPT: self object was created before we call Dunder function
"""
student_one = Student('Rolf Smith', [70, 88, 90, 99])
print(student_one.name) #Rolf Smith
print(student_one.grades) #[70, 88, 90, 99]
print(student_one.__class__) #<class '__main__.Student'>
print(student_one.average())

#student_one & student_two are objects calling the function
#of class 
#automatically populates 'self' as the object that called the function
#     def average(self):
        # return sum(self.grades) / len(self.grades)

student_two = Student('Jose', [50, 60, 99, 100])

print(Student.average(student_one)) #86.75


def average_grades(students):
    return sum(students.grades)/len(students.grades)

print(average_grades(student_one))


