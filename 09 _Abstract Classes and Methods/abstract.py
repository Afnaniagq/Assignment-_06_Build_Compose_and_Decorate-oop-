# Importing ABC and abstractmethod from the abc module to define abstract classes
from abc import ABC, abstractmethod

# Defining an abstract base class named Shape
class Shape(ABC):

    # Declaring an abstract method 'area' that must be implemented by subclasses
    @abstractmethod
    def area(self):
        pass  # Placeholder for the abstract method

# Defining a Rectangle class that inherits from Shape
class Rectangle(Shape):

    # Constructor to initialize width and height
    def __init__(self, width, height):
        self.width = width  # Assign width to the instance
        self.height = height  # Assign height to the instance

    # Implementing the abstract method 'area' from the Shape class
    def area(self):
        return self.width * self.height  # Calculating area of the rectangle

# Creating an instance of Rectangle with width 5 and height 3
rectangle = Rectangle(5, 3)

# Printing the area of the rectangle
print(rectangle.area())
   