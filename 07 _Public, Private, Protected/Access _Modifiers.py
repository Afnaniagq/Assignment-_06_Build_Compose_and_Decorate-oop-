# Access Modifiers (public,private ,protected):

class Employee:
   
    def __init__(self, name, salary, ssn):
        self.name = name         # Public variable (accessible from anywhere)
        self._salary = salary    # Protected variable (by convention, accessible in the class or subclass)
        self.__ssn = ssn         # Private variable (only accessible inside the class)

    def get_private(self):
        return self.__ssn        # Getter method for the private variable
    
    def set_private(self,new_ssn):  # Setter method to modify the private variable
        self.__ssn = new_ssn


# Creating an object of Employee class
emp1 = Employee("hamza", 10000, 7864)

# Accessing the public variable
print(emp1.name)             

# Accessing the protected variable (works, but not recommended)
print(emp1._salary)          

# Accessing the private variable through the getter method
print(emp1.get_private())    

# Modifying private variable using setter method
emp1.set_private("987-65-4321")  #  It safely changes the private variable.

# Accessing the modified private variable again using getter method
print(emp1.get_private())  # ✅ Now it shows the updated SSN: 987-65-4321
