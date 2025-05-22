# Using self:

class Student:
    def __init__(self, name, marks):
        self.name = name       # 'self.name' assigns the name to the instance variable
        self.marks = marks     # 'self.marks' assigns the marks to the instance variable

    def display(self):
        print(f"Student Name: {self.name}")  # Accessing instance variable 'name' using self
        print(f"Marks: {self.marks}")        # Accessing instance variable 'marks' using self

s1 = Student("Hiba", 95)  # Creating an instance of Student and passing name and marks
s1.display()              # Calling display method using the instance