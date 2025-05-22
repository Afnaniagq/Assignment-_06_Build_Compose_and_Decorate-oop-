# static variable and method:

class MathUtils:

    # Defining a static method that adds two numbers
    @staticmethod
    def add(a , b):
        return a + b  # Returning the sum of a and b

# Calling the static add method without creating an object
sum = MathUtils.add(3 ,6)    

# Printing the result
print("Total sum = ", sum)
