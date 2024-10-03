class Animal:
    def sound(self):
        print("This animal makes a sound.")

class Dog(Animal):  # Dog class inherits from Animal
    def bark(self):
        print("The dog barks.")

# Create an instance of Dog
dog = Dog()
dog.sound()  # Output: This animal makes a sound.
dog.bark()   # Output: The dog barks.
