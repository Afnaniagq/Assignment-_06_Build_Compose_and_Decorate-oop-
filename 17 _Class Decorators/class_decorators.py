# Class decorator function that adds a greet method to the class
def add_greeting(cls):
    # Define a new greet method that uses the instance's name
    def greet(self):
        return  f"\nHello {self.name} from Decorator!" 
    
    cls.greet = greet  # Add the greet method to the class
    return cls         # Return the modified class
  
  
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name  # Initialize the name attribute

p1 = Person("Ali")
print(p1.greet())    

p2 = Person("Hamza")
print(p2.greet())    

p3 = Person("Ahmed")
print(p3.greet())    
