class Father:
    def skills(self):
        print("Father: I am good at driving.")

class Mother:
    def skills(self):
        print("Mother: I am good at cooking.")

class Child(Father, Mother):  # Child inherits from both Father and Mother
    def skills(self):
        super().skills()  # Calls the 'skills' method from the first inherited parent class
        print("Child: I have my own set of skills.")

# Create an instance of Child
child = Child()
child.skills()
# Output:
# Father: I am good at driving.
# Child: I have my own set of skills.
