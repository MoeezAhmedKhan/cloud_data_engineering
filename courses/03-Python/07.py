# OOP

# An OOP (Object-Oriented Programming) language is a programming style where you organize your code around "objects" (which represent real-world things with data and actions) rather than just functions and logic.
# It provice reusablity
# What Is a Class?
# A class is a blueprint. It describes what a thing holds (like attributes / methods).

# A Class:
class BankAccount:
    # __init__ is a constructor is a special method which run when object of class created.
    def __init__(self, owner, balance=0): # these are parameter
        self.owner = owner
        self.balance = balance
    # The self parameter is a reference to the current
    # instance of the class, and is used to access variables
    # that belongs to the class.
    
    def deposit(self, amount = 0):
        self.balance += amount
        print(f"{self.owner} your deposited amount {amount}, new balance is: {self.balance}")
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f"Withdraw amount {amount}")
        
    def  balanceCheck(self):
        print(f"Current Balance {self.balance}")
# Now Creating Object/Instance
ali = BankAccount("Ali", 5000) # A class object
bilal = BankAccount("Bilal", 5000) # A class object

print(ali.balance)
ali.deposit(100)
ali.withdraw(50)
ali.balanceCheck()



# Static Method - Its doesnt use self parameter (Work at class level)

class Student:
    
    @staticmethod # Decorator
    def greeting():
        print("Hey there ...")
        
# Student().greeting() # It doent need a instance because it is static.
Student.greeting()



# Now Pillar Of OOP 
# 4 Types of pillar
# 1. Inheritance
# 2. Polymorphism
# 3. Abstraction
# 4. Encapsulation


# 1. Inheritance:
# Inheritance is a feature that lets child class use the properties and methods of its parent class.

# Types Of Inheritance
# Single Inheritance : One Parent -> One Child
# Multilevel Inheritance : Parent -> Child -> Sub Child
# Multiple Inheritance, Two Parent -> One Child
# Hirarical Inheritance : One Parent => Two or more child
# Hybrid Inheritance, Multiple Types Of Inheritance at a time

# 1. Single Inheritance
class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        return f"{self.name} is eating."

    def speak(self):
        return f"{self.name} makes a sound."


class Dog(Animal): # Inheritance
    def speak(self): # overrides the parent method
        return f"{self.name} says: Woof!"
    
    


dog = Dog("Bruno")
print(dog.name)
print(dog.eat())      # inherited from Animal
print(dog.speak())    # overridden in Dog


# 2.Hirarical Inheritance

class Vehicle:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed
    
    def info(self):
        print(f"{self.brand} - {self.model} - {self.speed}")
        

class Car(Vehicle):
    def __init__(self, brand, model, speed, door):
        # First call parent contructor and pass arguments via init contructor because parent contructor need some arguments.
        super().__init__(brand, model, speed)
        self.door = door


class Truck(Vehicle):
    def __init__(self, brand, speed, model, Tyre):
        super().__init__(brand, speed, model)
        self.Tyre = Tyre
       
        
civic = Car("Honda", "2019", 1800, 4)
civic.info()
print(civic.door)


# 3.Multilevel Inheritance

class Animal:
    def breathe(self):
        return "Breathing air."

class Mammal(Animal):
    def feed_young(self):
        return "Feeding young with milk."

class Dog(Mammal):
    def speak(self):
        return "Woof!"


dog = Dog()
print(dog.breathe())      # from Animal
print(dog.feed_young())   # from Mammal
print(dog.speak())        # from Dog



# 4.Multiple Inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def breathe(self):
        return f"{self.name} breathes air."
    
    def speed(self):
        return f"{self.name} run's fast"


class Swimmer:
    def swim(self):
        return "Swimming through water."

    def speed(self):
        return f"{self.name} swim's fast"


class Duck(Animal, Swimmer):          # inherits from both
    def speak(self):
        return f"{self.name} says: Quack!"


duck = Duck("Donald")
print(duck.breathe())   # from Animal
print(duck.swim())      # from Swimmer
print(duck.speak())     # Duck's own method

# Python resolves methods using Method Resolution Order (MRO). 
# If multiple parent classes have the same method, 
# Python uses the method from the first parent class listed in the inheritance declaration.
print(duck.speed())


# 5. Hybrid Inheritance

# A combination of two or more of the above types. 
# For example, hierarchical inheritance where one of the children also has multiple parents.

class Animal:
    def breathe(self):
        return "Breathing."

class Mammal(Animal):
    def feed_young(self):
        return "Feeding young."

class Swimmer(Animal):
    def swim(self):
        return "Swimming."

class Dolphin(Mammal, Swimmer):
    def speak(self):
        return "Click click!"


d = Dolphin()
print(d.breathe())      # Animal
print(d.feed_young())   # Mammal
print(d.swim())         # Swimmer
print(d.speak())        # Dolphin    



# 2 Encapsulation
# Encapsulation hides data using access modifiers.

# Access Modifiers
# 1. Public - Can be use outside the class
# 2. Protected - Can use inside the class and in child class
# 3. Private - Cannot use outside the class

class Person:
    def __init__(self, name, age, password):
        self.name      = name       # public   — anyone can read or change
        self._age      = age        # protected — intended for internal use
        self.__password = password  # private   — name mangled by Python

    def get_age(self):
        return self._age            # controlled access through a method

    def check_password(self, attempt):
        return attempt == self.__password
    
    # setter
    def update_password(self, oldPassword, newPassword):
        if oldPassword == self.__password:
            self.__password = newPassword
            print("Password Updated!")
        else:
            print("Your old password is incorrect")
            
            
     # getter   
    def get_detail(self):
        print(f"Name: {self.name} , Password: {self.__password}")
    
    


p = Person("Alice", 30, "secret123")

print(p.name)          # ✓ Public — works fine
print(p._age)          # ✓ Works, but you shouldn't do this outside the class
print(p.get_age())     # ✓ Correct way to access protected data
print(p.check_password("secret123"))

# It gives an error because this is private
# print(p.__password)

print(f"Passsword show: {p._Person__password}")
# Python store private variable like _Person__password not like _password

# We have to create getter and setter for getting and update this.
p.update_password("secret123","hello123")
p.get_detail()




# Polymorphism - (Poly = Multiple) , (Morphism = Forms)

# Polymorphism means the same method name produces different behavior depending on which class is calling it.

# Example 1:
print(1)
print("Hello")
print(True)


# Example 2

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Bird:
    def speak(self):
        return "Tweet!"

class Cow:
    def speak(self):
        return "Moo!"


animals = [Dog(), Cat(), Bird(), Cow()]

for animal in animals:
    print(f"{animal.__class__.__name__}: {animal.speak()}")




# Abstraction
# Abstraction means hiding implementation details and showing only the necessary features to the user.

from abc import ABC, abstractmethod


class Animal(ABC): # Abstract Class

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog says: Bark")


dog = Dog()
dog.sound()
