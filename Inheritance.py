"""
INHERITANCE:
Allows us to define us a class that inherits all the methods
and properties from another class

Use inheritance to avoid duplicates in class

Parent class: the class being inherited from, also called base class.

Child class: the class that inherits from another class, also called derived class.
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
    def weekly_salary(self):
        return self.salary * 37.5 

rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print(rolf.salary) #output: 15.50
rolf.marks.append(57)
rolf.marks.append(99)
print(rolf.average()) #output: 78.0
print(rolf.weekly_salary()) #output: 581.25

anna = Student('Anna','Oxford')
print(anna.weekly_salary()) #gives: AttributeError: 'Student' object has no attribute 'weekly_salary'

