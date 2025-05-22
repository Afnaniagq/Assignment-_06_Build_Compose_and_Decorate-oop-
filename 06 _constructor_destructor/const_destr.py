# This is a class named Logger
class Logger:
    # Constructor: runs automatically when an object is created
    def __init__(self):
        print("Logger object has been created")

    # Destructor: runs automatically when the object is destroyed
    def __del__(self):
        print("Logger object is being destroyed.")

# Creating an object of the Logger class (calls constructor)
log = Logger()

# Deleting the object manually (calls destructor)
del log


