# Department class

# Aggregation: A weak "has-a" relationship where objects can exist independently.
class Department:
    def __init__(self, name):
        self.name = name  # Store department name

# Employee class
class Employee:
    def __init__(self, name, department):
        self.name = name            # Store employee name
        self.department = department  # Aggregation: has-a Department

    def show_details(self):
        print(f"Employee Name: {self.name}")
        print(f"Department: {self.department.name}")

# Create a Department object
dept1 = Department("Artificial Intelligence\n")

# Create an Employee object and link to department
emp1 = Employee("Ayesha", dept1)
emp2 = Employee("Ali", dept1)
emp3 = Employee("Areeba", dept1)


# Show employee details
emp1.show_details()
emp2.show_details()
emp3.show_details()

