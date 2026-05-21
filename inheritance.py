# Inheritance Example 1

class FactoryMumbai:
    def location(self):
        print("We are from Mumbai")


class FactoryPune(FactoryMumbai):
    pass


loc = FactoryMumbai()
loc2 = FactoryPune()

loc.location()
loc2.location()


# Inheritance Example 2

class Vehicle:
    brand = "Toyota"


class Car(Vehicle):
    pass


b2 = Car()
print(b2.brand)


# Inheritance Example 3

class Animal:
    def eat(self):
        print("Eat")


class Dog(Animal):
    def bark(self):
        print("Bark")


A2 = Dog()

A2.eat()
A2.bark()


# Inheritance Example 4

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    pass


obj2 = Student("Bhavitha", 21)

print(obj2.name)
print(obj2.age)


# Inheritance Example 5

class School:
    def info(self):
        print("Method calling")


class Student(School):
    pass


class Teacher(School):
    pass


b1 = Student()
c1 = Teacher()

b1.info()
c1.info()
