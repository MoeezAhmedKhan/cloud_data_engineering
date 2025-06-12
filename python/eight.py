# OOP in Python
# OOP is a way of programming where we use objects to organize data, just like real-world things.

# Procedural Programming - we started from here
# Functional Programming - after that we shift into function for organized and maintain reusebility.
# Object Oriented Programming - Now we start OOP

# Class and Object in Python
# Class is a blueprint for creating objects

# creating a class
class Student:
    name = "Ali"

# creating object
s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)


# _init()_ function
# init() is a constructor
# All class have a function called _init()_ which is alway execute when the class is being initialized

class Person:
    # def __init__(self): # self is a refrence of its object and point itself.
    #     print(self)
    #     print("Hello Contructor Called")

     def __init__(self, name):  # Constructor can accept multiple parameters.
        self.name = name # we initializing the name variable in this instance. self is used to declare as the variable will be a part of this object.
        print("Hello Contructor Called")

# Person()
p1 = Person("Ahad")
print(p1.name)


# Class and Instance Attributes
# A variable that is the same for all objects is called a class attribute and is declared directly in the class.
# A variable that is different for each object is called an instance attribute and is declared using self.variable_name.

class Car:
    carName = "Annonymous" # class attr
    def __init__(self, carName):
        self.carName = carName # obj attr

car1 = Car("Civic")
print(car1.carName) # The object attribute is retrieved because it has higher precedence, and since we are accessing it through an object, only the object attribute is accessed.


# Methods - methods are function thats belongs to object

class Student:
    college = "Jinnah Gov College"
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("Welcome", self.name)

    def getMarks(self):
        print(self.name,"Got",self.marks)

s1 = Student(name="Ahmed", marks=897)
s1.welcome()
s1.getMarks()


# Q1. Create a class `Student` to calculate and display the percentage of marks for a given student.

class Student:
    def __init__(self, studentName, subjectMarks):
        self.studentName = studentName
        self.subjectMark = subjectMarks

    def calculate_percentage(self):
        obtainMakrs = 0
        for i in self.subjectMark:
            obtainMakrs+=i

        percentage = obtainMakrs/(len(self.subjectMark) * 100) * 100
        print(self.studentName,"Got",percentage,"%")

s1 = Student(studentName="Bilal", subjectMarks=[60,89,78,54])
# s1.studentName = "Saad" # we can change student name for its instance
s1.calculate_percentage()


# Static Method - method that dont use the self parameter (work at class level)

class Student:

    @staticmethod # Decorator to define a static method
    def college(): # Static methods don't require 'self' as they are not tied to any specific object and Its a class level method
        print("Jinnah Gov College..")

Student.college()


# Q2. Write a Python program to implement a class Account with methods for crediting, debiting, and checking account balance.

class Account:
    def __init__(self, accountNo, balance):
        self.accountNo = accountNo
        self.balance = balance
    
    def credit(self,amount):
        self.balance+=amount
        print("Rs.",amount,"was credit")

    def debit(self, amount):
        self.balance-=amount
        print("Rs.",amount,"was debit")

    def acct_balance(self):
        print("You account no is",self.accountNo,"and balance is",self.balance)

account = Account(accountNo="Qw1111119", balance=1000)
account.credit(500)
account.acct_balance()
account.debit(400)
account.acct_balance()