class Father:
    def skills(self):
        print("I am father class ")

class Mother:
    def skills(self):
        print("I am mother class")

class Child(Father, Mother):  
    def skills(self):
        super().skills()  
        print("Child: I have my own set of skills.")
        
child = Child()

child.skills()

