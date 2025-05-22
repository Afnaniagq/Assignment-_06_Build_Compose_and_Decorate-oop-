# Base class
class Person:
    def __init__(self, name):
        self.name = name

# Derived class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)   # Call the base class constructor
        self.subject = subject

# Creating an object of Teacher
per1 = Teacher("Hafsa", "Math")

# Accessing attributes
print(per1.name)   
print(per1.subject)   



        