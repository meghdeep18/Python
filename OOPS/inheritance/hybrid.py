class Vehicle:
    def display(self):
        print("This is a vehicle.")

class Car(Vehicle):
    def car_info(self):
        print("This is a car.")

class Truck(Vehicle):
    def truck_info(self):
        print("This is a truck.")

class HybridCar(Car, Truck):  # HybridCar inherits from both Car and Truck
    def hybrid_info(self):
        print("This is a hybrid car, which is a combination of car and truck.")

# Create an instance of HybridCar
hybrid = HybridCar()
hybrid.display()     # Output: This is a vehicle.
hybrid.car_info()    # Output: This is a car.
hybrid.truck_info()  # Output: This is a truck.
hybrid.hybrid_info() # Output: This is a hybrid car, which is a combination of car and truck.
