#  Instance Methods:

class Dog:
    def __init__(self, name, breed):  # Constructor
        self.name = name       # instance variable
        self.breed = breed     # instance variable

    def bark(self):            # instance method
        print(f"{self.name} is barking!")  # using instance variable

        
d1 =Dog("Max","Bulldog")      #creating an object  
d1.bark()