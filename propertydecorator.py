"""
The @property decorator

methods: functions inside a class that perform an action
we want to turn the weekly_salary method into a property

if you are doing an action like connecting to a database or opening a file
or communicating with web service or interacting with other object or any 
action, please dont use the property decorator.

Use it only when you are calculating values from the object's property themselves
"""

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


#WorkingStudent is an extension of class Student or rather a child of parent class Student
#WorkingStudent has directly inherited from Student the 'average' method

#super() refers(is) to the parent class: Student

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

#37.5 hrs is the weekly working duration in the UK
#the weekly_salary function doesnt perform any action; just calculates a value
# if the function only takes a self argument, and only calculates a value based on self property
    @property
    def weekly_salary(self):
        return self.salary * 37.5 

rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(rolf.weekly_salary) #output: 581.25




