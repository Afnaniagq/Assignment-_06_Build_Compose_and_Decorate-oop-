# Property Decorators: @property, @setter, and @deleter

class Product:
    def __init__(self, _price):
        self._price = _price  # Initialize private price variable

    @property
    def price(self):
        # Getter method - runs when you access p.price
        return self._price

    @price.setter
    def price(self, value):
        # Setter method - runs when you assign a new value like p.price = 700
        print("\nSetting the Price")
        if not isinstance(value, (int, float)):
            raise ValueError("Price must be in number")
        self._price = value

    @price.deleter
    def price(self):
        # Deleter method - runs when you delete the price using del p.price
        print("Deleting the Price")
        del self._price


# Create an object of Product with initial price 600
p = Product(600)

# Access the price using getter
print(f"\nActual Price is {p.price}")  # Output: 600

# Update the price using setter
p.price = 700  # Output: Setting the Price

# Access new updated price
print(f"New Price {p.price}\n")  # Output: 700

# Delete the price using deleter
del p.price  # Output: Deleting the Price



