# 4 Pillar of OOP - Inheritance, Polymorphism, Abstraction, Encapsulation


# Abstraction - Hiding implementation details and showing only the essential features of an object.

# The abc module in Python provides tools for creating Abstract Base Classes (ABC).
# ABCs are classes that act as templates for other classes, ensuring that all derived classes
# implement certain methods or properties.
from abc import ABC, abstractmethod

# Abstract class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass  # Abstract method has no implementation

# Concrete class implementing abstract method
class Dog(Animal):
    # overridden method
    def sound(self):
        return "Bark"

class Cat(Animal):
    # overridden method
    def sound(self):
        return "Meow"

dog = Dog()
cat = Cat()
print(dog.sound())  # Output: Bark
print(cat.sound())  # Output: Meow

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


#-----------------------------------


# Encapsulation: Bundling data and methods together and restricting direct access.

class Account:
    def __init__(self, accountNo, balance):
        self.__accountNo = accountNo  # Private attribute
        self.__balance = balance      # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: {amount}. New Balance: {self.__balance}")
        else:
            print("Invalid amount or insufficient balance.")

    def get_balance(self):  # Public method to access private attribute
        return self.__balance


account = Account("12345", 1000)
account.deposit(500)      # Depositing amount
account.withdraw(300)     # Withdrawing amount
print("Balance:", account.get_balance())  # Accessing balance using public method


#-----------------------------------


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

# Super keyward is used to access method/properties of the parent class

class Car:
    def __init__(self, carType):
        self.carType = carType
    
    def starts(self):
        print("Car is started.")

class Honda(Car):
    def __init__(self, carName, carType): # Step 2: carType is taken as a parameter
        super().__init__(carType) # carType is passed to the parent class constructor
        self.carName = carName
        
        super().starts() # Parent class method called in child class contructor
        
        
car1 = Honda("Civic", "Hybrid") # Step 1: carName and carType are passed as arguments to the Honda class constructor
print(car1.carType)


#-----------------------------------


# Class Method
# A class method is a method that operates on the class itself rather than an instance, and is defined using the `@classmethod` decorator.

class Person:
    name = "Annonymous"
    
    @classmethod
    def changeClassLevelName(cls, name):
        cls.name = name

p1 = Person()
p1.changeClassLevelName("Saad")
print(p1.name)

# 1. Static Method: A method that doesn't access or modify class or instance attributes and is defined using the `@staticmethod` decorator.
# 2. Class Method: A method that operates on the class itself and is defined using the `@classmethod` decorator.
# 3. Instance Method: A method that operates on an instance of the class, accessing or modifying instance attributes.


# The @property keyword: is used to define a method as a read-only attribute, allowing controlled access to a class property.The @property keyword is used to define a method as a read-only attribute, allowing controlled access to a class property.

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        # self.full_name = f"{self.first_name} {self.last_name}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

person = Person("Ali", "Khan")
person.first_name = "Ahmed" # Here we change name but when i print full_name i get previous full_name thats why we use @Property keyward
print(person.full_name)



#-----------------------------------



# Polymorphism - Poli (many), morphism (forms)
# In OOP, it allows the same function or operator to behave differently based on the object.

# Examples of polymorphism in Python:
a = 1 + 4  # Integers: addition (result: 5)
b = "Hello" + "World"  # Strings: concatenation (result: "HelloWorld")
c = [1, 2, 3] + [4, 5, 6]  # Lists: merging (result: [1, 2, 3, 4, 5, 6])

# Now we have another type of number like a complex number, which is based on something like 3i + 4j 
# (i refers to the real part, and j refers to the imaginary part).

# If we have two complex numbers, we can add them like this:
# 3i + 4j
# 6i + 8j
# -------
# 9i + 12j

# In programming, we don't have a built-in class to create complex numbers,
# so we make a user-defined class and can perform add, sub, mul, div, mod, etc.

# Operators & Dunder (Double Underscore) functions:
# a + b  # addition    --> a.__add__(b)
# a - b  # subtraction --> a.__sub__(b)
# a * b  # multiplication --> a.__mul__(b)
# a / b  # division    --> a.__div__(b)
# a % b  # modulus     --> a.__mod__(b)


class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
        
    # def add(self, num2):
    #     newReal = self.real + num2.real
    #     newImg = self.img + num2.img
    #     return Complex(newReal, newImg)
    
    def __add__(self, num2): # if i want to use only + operator between oprands so we should use dunder function
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal, newImg)
    
    def __sub__(self, num2):
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal, newImg)
        
        
num1 = Complex(3, 8)
num1.showNumber()

num2 = Complex(6, 4)
num2.showNumber()

# num3 = num1.add(num2)
# num3.showNumber()

# addition
# num3 = num1 + num2
# num3.showNumber()

# subtract
num3 = num1 - num2
num3.showNumber()


#-----------------------------------


# Let's Practice

# Q. Define a Circle class to create a circle with radius r using the constructor.
# Define an Area() method of the class which calculates the area of the circle.
# Define a Perimeter() method of the class which allows you to calculate the perimeter of the circle.

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.142 * (self.radius ** 2)
        
    def perimeter(self):
        return 2 * 3.142 * self.radius
        
c1 = Circle(13)
print(c1.area())
print(c1.perimeter())


# Q. Define an Employee class with attributes role, department & salary. This class should have a showDetails() method.
# Create an Engineer class that inherits properties from Employee & has additional attributes: name & age.

class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        print(f"Role: {self.role}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.salary}")


class Engineer(Employee):
    def __init__(self, role, department, salary, name, age):
        super().__init__(role, department, salary)
        self.name = name
        self.age = age

    # Overridden method
    def showDetails(self):
        super().showDetails()
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")


emp1 = Engineer("Software Engineer", "IT", 85000, "John Doe", 28)
emp1.showDetails()


# Q. Create a class called order which store item and its price
# Use Dunder function_ _ get_ _() to convey that:
# order1 > order2 if price of order1 > price of order2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
        
    # def gt(self, order2):
    #     if(self.price > order2.price):
    #         order1IsGreater = True
    #         print("Order 1 Price is Greater")
    #     else:
    #         print("Order 2 Price is Greater")
    
    
    def __gt__(self, order2): # With dunder function
        if(self.price > order2.price):
            print("Order 1 Price is Greater")
        else:
            print("Order 2 Price is Greater")
            
        
order1 = Order("Chips", 40)
order2 = Order("Drink", 80)
order1 > order2

        