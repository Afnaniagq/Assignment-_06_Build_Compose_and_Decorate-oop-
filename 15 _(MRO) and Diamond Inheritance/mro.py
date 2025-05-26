# Method Resolution Order (MRO) and Diamond Inheritance example

# MRO: The order in which Python looks for methods in a hierarchy of classes.
# Diamond Inheritance: A multiple inheritance scenario where a class inherits from two classes that share a common base class, forming a diamond shape.

class A:
    def show(self):
        print("This is method A")  # Method in base class A

class B(A):
    def show(self):
       print("This is method B")  # Method overridden in class B

class C(A):
    def show(self):
       print("This is method C")  # Method overridden in class C

class D(B,C):
    pass  # Class D inherits from both B and C (diamond inheritance)

d = D()  # Create instance of class D
d.show()  # Calls method based on MRO, here from class B

print(D.mro())  # Print Method Resolution Order for class D

