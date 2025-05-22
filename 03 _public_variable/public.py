# public variable:

class Car:

    def __init__(self, brand): 
        self.brand = brand  # Public instance variable to store the car's brand
      
    def start(self):  # Public method 
        print(self.brand, "car start")  # Prints which brand car has started

car1 = Car("Toyota")  # Creating the first Car object with brand "Toyota"
car1.start() 

car2 = Car("Honda")
car2.start()  # Calling the start method for Honda
