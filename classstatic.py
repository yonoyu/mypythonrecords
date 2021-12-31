"""
instance method: one that takes the (caller) object as the first argument aka self 

takes the caller's class (Student) as first argument 
takes nothing as first argument 

you do not need an init method on every class so you wont define any property to begin with
@classmethod - wants access to a class

@staticmethod

"""
class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

rolf = Student('Rolf', 'MIT')

rolf.marks.append(78)
rolf.marks.append(99)

#The caller is rolf. When we call the average, it takes in rolf as the first argument.
#Instance method
print(rolf.average())

#cls is the name of parameter, refers to class in this case
#cls.__name__ is the name of the class - Foo
class Foo:
    @classmethod
    def hi(cls):
        print(cls.__name__)

my_object = Foo()
my_object.hi() #output: Foo

class Bar:
    @staticmethod
    def hi():
        print('Hello, I don\'t take parameters.')

another_object = Bar()
another_object.hi()


class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    #:.2f means to 2 decimal places
    def __repr__(self):
        return f'<FixedFloat {self.amount:.2f}>'

    #static method
    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)

number = FixedFloat(18.5746) #FixedFloat object
print(number) #output: <FixedFloat 18.57>

new_number = FixedFloat.from_sum(19.575, 0.789)
print(new_number) #output: <FixedFloat 20.36>

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self):
        return f'<Euro {self.symbol}{self.amount:.2f}>'

money = Euro(18.786)
print(money) #output: <Euro €18.79>

#if from_sum() method is a static method
# money2 = Euro.from_sum(16.758, 9.999)
# print(money2) #output: <FixedFloat 26.76>

#if from_sum() method is a class method
money3 = Euro.from_sum(16.758, 9.999)
print(money3) #output: <Euro €26.76>




