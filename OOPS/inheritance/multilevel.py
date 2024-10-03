class Animal:
    def sound(self):
        print("This animal makes a sound.")

class Mammal(Animal):  # Mammal class inherits from Animal
    def walk(self):
        print("This mammal walks.")

class Dog(Mammal):  # Dog class inherits from Mammal
    def bark(self):
        print("The dog barks.")

# Create an instance of Dog
dog = Dog()
dog.sound()  # Output: This animal makes a sound.
dog.walk()   # Output: This mammal walks.
dog.bark()   # Output: The dog barks.
