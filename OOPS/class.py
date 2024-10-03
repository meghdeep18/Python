# Define a simple class
class Car:
    def __init__(self, brand, model):
        # Attributes (Properties)
        self.brand = brand
        self.model = model

    # Method (Function inside a class)
    def display_info(self):
        print(f"This car is a {self.brand} {self.model}")

# Create an object (instance of the class)
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

# Access attributes and call methods
car1.display_info()  # Output: This car is a Toyota Corolla
car2.display_info()  # Output: This car is a Honda Civic
