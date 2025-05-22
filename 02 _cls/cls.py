# using cls:

class Counter():
    count = 0  # Class variable to keep track of number of objects

    def __init__(self):  # Constructor method that runs when a new object is created
        Counter.count += 1  # Increase the count each time a new object is made

    @classmethod  # Decorator to define a method that works with the class, not instances
    def get_count(cls):  # Class method to print total number of objects created
        print(f"Total objects created: {cls.count}")  # Display the value of the count

obj1 = Counter()  
obj2 = Counter() 
obj3 = Counter()  
obj4 = Counter()  

Counter.get_count() 



        