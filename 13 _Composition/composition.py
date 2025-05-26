# Composition Method: A Car "has-an" Engine (using one class inside another)

# Composition: A strong "has-a" relationship where one object owns another completely.

class Engine:  
    def __init__(self, power):  # Constructor to initialize engine with power
        self.power = power  # Store the power in the engine object

    def start(self):  # Define a method to start the engine
        print(f"Engine with power {self.power} started.")  # Print engine start message with its power

class Car: 
    def __init__(self, color, engine):  # Constructor to initialize car with color and engine
        self.color = color  # Store the color of the car
        self.engine = engine  # Store the engine object inside the car (Composition)

    def car_start(self):  # Define a method to start the car
        print(f"The {self.color} car is starting.")  # Print car start message with its color
        self.engine.start()  # Call the engine's start method (composition in action)

# Create  engine object with power 
engine1 = Engine(100)

engine2 = Engine(200)

# Create  car object with color and engine
car1 = Car("red", engine1)

car2 = Car("blue", engine2)

# Start the  car (which will also start its engine)
car1.car_start()

car2.car_start()






       