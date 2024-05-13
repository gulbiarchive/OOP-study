class Parent:
    def __init__(self, name):
        self.name = name
    
    def greet(self):
        print(f"Hello, I'm {self.name}")

class Child(Parent):
    def new_method(self):
        print("This is a new method for Child class")

child = Child("Alice")
child.greet()
child.new_method()