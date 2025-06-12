# 4 Pillar of OOP - Inheritance, Polymorphism, Abstraction, Encapsulation

# Abstraction - Hiding implementation details and showing only the essential features of an object.

# Encapsulation is the process of bundling data and methods together into a single unit and restricting direct access to some parts of the object.

#-----------------------------------

# Private attributes and Methods
# Private attr and methods are used within in the class and are not accessible outside the class

class Account:
    def __init__(self, accountNo, accountPass):
        self.__accountNo = accountNo # __ is used to make private
        self.__accountPass = accountPass

acc1 = Account("Tr001112", "Tr@123")
# print(acc1.accountNo) # Now its not accessible outside the class
# print(acc1.accountPass) # Same for this

class Person:
    
    def __hello(self): # Private method
        print("Hello Person")
    
    def welcome(self):
        self.__hello() # Private method called with in the class

p1 = Person()
p1.welcome()


# Inheritance - one class (child/derived) inherit the properties & method from another class (Parent/Base)

class Car:
    
    def start(self):
        print("Car started")

    def stop(self):
        print("Car stopped")

class Toyota(Car):
    
    def __init__(self, car):
        self.car = car

toyota = Toyota("Fortuner")
print(toyota.car)
toyota.start() # We can access parent class method into child class thorugh inheritance


# Types of Inheritance
# Single Inheritance - Above inheritance is the example of sinle inheritance.
# Multi Level Inheritance
# Multiple Inheritance


# Multi Level Inheritance

class Animal:
    def eat(self):
        print("This animal eats food.")

class Mammal(Animal):
    def walk(self):
        print("This mammal walks.")

class Dog(Mammal):
    def bark(self):
        print("This dog barks.")

dog = Dog()
dog.eat()    # Method from Animal class
dog.walk()   # Method from Mammal class
dog.bark()   # Method from Dog class


# Multiple Inheritance

class A:
    a = "Welcome to class A"

class B:
    b = "Welcome to class B"

class C(A,B):
    c = "Welcome to class C"

c1 = C()
print(c1.a)
print(c1.b)
print(c1.c)



