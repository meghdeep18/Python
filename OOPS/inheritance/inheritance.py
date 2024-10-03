# Base class (Parent)
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        print(f"The engine of {self.brand} {self.model} is starting...")

# Derived class (Child)
class Motorcycle(Vehicle):
    def __init__(self, brand, model, type_of_bike):
        # Inherit brand and model from Vehicle
        super().__init__(brand, model)
        self.type_of_bike = type_of_bike

    def bike_info(self):
        print(f"This is a {self.type_of_bike} bike: {self.brand} {self.model}")

# Create a Motorcycle object
bike = Motorcycle("Yamaha", "MT-15", "Sport")
bike.start_engine()  # Output: The engine of Yamaha MT-15 is starting...
bike.bike_info()     # Output: This is a Sport bike: Yamaha MT-15
