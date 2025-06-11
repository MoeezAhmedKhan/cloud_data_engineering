# Functions is a bloc of code thats used to perform a specific task.

# function definition
def cal_sum(a,b): # parameters
    print(a+b)

cal_sum(5,5) # fucntion call, arguments

def print_hello():
    print("Hello")

print_hello()
print_hello()
print_hello()

# Print the average of 3 numbers

def find_avg(a,b,c):
    sum = a+b+c
    avg = sum/3
    print(avg)

find_avg(77,90,83)

# Types of function 

# Built-in function 
# print()
# len()
# type()
# range()

#  Userdefined function - User-defined functions (UDFs) are custom functions created by programmers to perform specific tasks

# 1. Parameterized Without return type functions 
def name(n):
    print("My name is",n) 

name("Ahmed")

# 2. Parameterized With Return Type functions
def cal_prod(a,b):
    product = a * b
    return product

result = cal_prod(2,4)
print(result)

# 3. Non-Parameterized Without return type functions 
def greet():
    print("Hello World")

greet()

# 4. Non-Parameterized With return type functions 
def get_pi():
    return 3.14

print(get_pi())


# Default Parameter - assign a value to parameter. which is used when no argument is passed

def fruits(a = "Apple", b = "Banana", c = "Mango"):
    print(a,b,c)

fruits() # Default Arguments
fruits("Orange") # Positional Arguments
fruits(c="Graps") # Keyword Arguments

# Lets Practice

# Q1. WAP to find factorial of n. (n is the parameter)

def findFac(n):
    fact = 1
    for i in range(1,n+1):
        fact*=i
    return fact

print("Factorial is",findFac(5))

# Q2 WAP to convert usd to pkr

def convertion(usd):
    pkr = usd * 282.49
    print(usd,"usd converted in pkr",pkr)

convertion(10)

# Q3. WAP to check even and odd

def check(number):
    if(number%2==0):
        print(number,"is a even number")
    else:
        print(number,"is a odd number")

check(5)

# Q4. Write a function that takes a string as input and capitalizes it. If no string is provided, use the default value "hello".

def capitilized(st = "hello"):
    print(st.capitalize())

capitilized()
capitilized("world")


# Q5. WAP to find palindrome.
def palindromChecker(txt):
    tempStr = ""
    for i in range(len(txt)-1, -1, -1):
        tempStr+=txt[i]

    if(tempStr == txt):
        print(txt,"is Palindrome")
    else:
        print(txt,"is not a Palindrome")

palindromChecker("dsd")

# Q6. Write a function that takes a dictionary containing students' names as keys and their marks as values. The function should calculate and assign a grade for each student based on their marks.

def calculateGrade(student):
    phy = student["marks"]['phy']
    math = student["marks"]['math']
    chem = student["marks"]['chem']
    eng = student["marks"]['eng']
    urdu = student["marks"]['urdu']

    percentage = (phy+math+chem+eng+urdu) / 500 * 100

    grade = ''
    if(percentage > 90):
        grade = 'A+ with topper'
    elif(percentage > 80 and percentage <= 90):
        grade = 'A+'
    elif(percentage > 70 and percentage <= 80):
        grade = 'A'
    elif(percentage > 60 and percentage <= 70):
        grade = 'B'
    elif(percentage > 50 and percentage <= 60):
        grade = 'C'
    elif(percentage > 40 and percentage <= 50):
        grade = 'D'
    else:
        grade = 'F'

    print("Student",student["name"],"Got",percentage,"Grade",grade)

calculateGrade({"name":"Ali", "marks":{"phy":99,"math":91,"chem":93,"eng":96,"urdu":80}})


# Q7. Write a function that takes a range as input and returns all the prime numbers within that range.

def findPrime(start, end):
    for i in range(start, end):
        isPrime = True
        if(i < 2):
            continue

        for x in range(2, i):
            if(i % 2 == 0):
                isPrime = False
                break

        if(isPrime):
            print(i)
findPrime(1, 11)


# Real-Life Scenarios

# Write a function that checks whether a given password is strong or not.

# A password is considered strong if it meets the following criteria:

# Contains at least 8 characters.

# Includes at least one letter.

# Includes at least one numeric digit.

# Includes at least one special character (e.g., !, @, #, $, etc.).

# The function should return True if the password is strong and False otherwise.

def checkPassword(password = "a2@A9N*!"):
    letters = "qwertyuiopasdfghjklzxcvbnmQWETUIOPASDFGHJKLZXCVBNM"
    numbers = "0123456789"
    specialChars = "~!@#%^&*(|_-+*/?<:>[{}]);,"

    letterCount = 0
    numbersCount = 0
    speicalCount = 0

    for char in password:
        if char in letters:
            letterCount+=1
        elif char in numbers:
            numbersCount+=1
        elif char in specialChars:
            speicalCount+=1

    if(len(password) >= 8 and letterCount > 0 and numbersCount > 0 and speicalCount > 0):
        print(password, "is strong")
    else:
        print(password, "is week")

checkPassword()


# Recursion - when function call itself repeatedly

def show(n):
    if(n == 0):
        return
    print(n) 
    show(n-1)
show(5)

print("------------------")

def findFactorial(n):
    if(n == 0 or n == 1):
        return 1
    return findFactorial(n-1)*n

print(findFactorial(5))

print("------------------")

# WAP to print sum of all n natural number using recursion 

def cal(n):
    if(n == 0):
        return 0
    return cal(n-1) + n

print(cal(10))








