class Animal:
    def sound(self):
        print("This animal makes a sound.")

class Dog(Animal):  # Dog inherits from Animal
    def bark(self):
        print("The dog barks.")

class Cat(Animal):  # Cat inherits from Animal
    def meow(self):
        print("The cat meows.")

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

dog.sound()  # Output: This animal makes a sound.
dog.bark()   # Output: The dog barks.

cat.sound()  # Output: This animal makes a sound.
cat.meow()   # Output: The cat meows.
