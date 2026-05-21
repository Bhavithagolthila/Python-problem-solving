# Constructor Example using Inheritance and super()

class Animal:
    # Parent class constructor
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"Animal Name: {self.name}")


class Human(Animal):
    # Child class constructor
    def __init__(self, name, age):

        # Calling parent class constructor
        super().__init__(name)

        # Initializing child class attribute
        self.age = age

    # Method overriding
    def show(self):
        print(f"Human Name: {self.name}")
        print(f"Age: {self.age}")


# Creating objects
animal1 = Animal("Lion")
person1 = Human("Raksha", 23)

# Calling methods
animal1.show()

print("--------")

person1.show()
