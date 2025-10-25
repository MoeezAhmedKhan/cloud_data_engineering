# ==============================
# PART 1 – PYTHON BASICS (VARIABLES)
# ==============================

# 1. Print Name, Father’s Name, and DOB using escape sequences
print("Name:\tMoeez Khan\nFather's Name:\tAhsan Khan\nDate of Birth:\t25-10-2002")

print("-------------")

# 2. Write your small bio using variables and print it
name = "Moeez Khan"
age = 22
education = "BS Computer Science"
hobby = "Coding and Football"
print(f"My name is {name}. I am {age} years old. I have completed my {education}. My hobby is {hobby}.")

print("-------------")

# 3. Program using all operators
a, b = 10, 3
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

# Comparison operators
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater:", a > b)
print("Less:", a < b)

# Logical operators
x, y = True, False
print("AND:", x and y)
print("OR:", x or y)
print("NOT:", not x)

# Assignment operators
a += 5
print("After += :", a)

# Identity and membership
list1 = [1, 2, 3]
print("2 in list:", 2 in list1)
print("4 not in list:", 4 not in list1)
print("a is b:", a is b)
print("a is not b:", a is not b)

print("-------------")

# 4. Calculate percentage of 3 subjects (English, Islamiat, Maths)
english = 85
islamiat = 90
maths = 80
total_marks = 300
obtained = english + islamiat + maths
percentage = (obtained / total_marks) * 100
print("Total Marks:", obtained)
print("Percentage:", round(percentage, 2), "%")

print("===================================")
print("PART 2 – PYTHON BASICS (CONDITIONAL STATEMENTS)")
print("===================================")

# 1. Bonus 5% if service > 5 years
salary = float(input("Enter your salary: "))
years = int(input("Enter years of service: "))
if years > 5:
    bonus = salary * 0.05
    print("Bonus Amount:", bonus)
else:
    print("No bonus")

print("-------------")

# 2. Check voting eligibility
age = int(input("Enter your age: "))
if age > 17:
    print("Eligible for voting")
else:
    print("Not eligible for voting")

print("-------------")

# 3. Even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

print("-------------")

# 4. Divisible by 7 or not
num = int(input("Enter a number: "))
if num % 7 == 0:
    print("Divisible by 7")
else:
    print("Not divisible by 7")

print("-------------")

# 5. Hello if multiple of 5, else Bye
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Hello")
else:
    print("Bye")

print("-------------")

# 6. Display last digit of a number
num = int(input("Enter a number: "))
print("Last digit:", num % 10)

print("-------------")

# 7. Check square or rectangle
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
if length == breadth:
    print("Square")
else:
    print("Rectangle")

print("-------------")

# 8. Greatest among two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Greatest is:", a)
elif b > a:
    print("Greatest is:", b)
else:
    print("Both are equal")

print("-------------")

# 9. Shop discount (10% if total cost > 1000)
quantity = int(input("Enter quantity: "))
cost = quantity * 100
if cost > 1000:
    cost = cost - (cost * 0.10)
print("Total cost:", cost)

print("-------------")

# 10. Grade system
marks = int(input("Enter marks: "))
if marks < 25:
    grade = "F"
elif marks < 45:
    grade = "E"
elif marks < 50:
    grade = "D"
elif marks < 60:
    grade = "C"
elif marks < 80:
    grade = "B"
else:
    grade = "A"
print("Grade:", grade)

print("-------------")

# 11. Attendance percentage and eligibility
classes_held = int(input("Classes held: "))
classes_attended = int(input("Classes attended: "))
percentage = (classes_attended / classes_held) * 100
print("Attendance:", round(percentage, 2), "%")
if percentage >= 75:
    print("Allowed in exam")
else:
    print("Not allowed in exam")

print("-------------")

# 12. Attendance with medical cause
classes_held = int(input("Classes held: "))
classes_attended = int(input("Classes attended: "))
percentage = (classes_attended / classes_held) * 100
medical = input("Medical cause (Y/N): ").upper()
if percentage >= 75 or medical == 'Y':
    print("Allowed in exam")
else:
    print("Not allowed in exam")

print("-------------")

# 13. Leap year check
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap year")
else:
    print("Not a leap year")

print("-------------")

# 14. Employee work location
age = int(input("Enter age: "))
gender = input("Enter gender (M/F): ").upper()
married = input("Married? (Y/N): ").upper()
if gender == 'F':
    print("She will work in urban areas only.")
elif gender == 'M':
    if 20 <= age <= 40:
        print("He may work anywhere.")
    elif 40 < age <= 60:
        print("He will work in urban areas only.")
    else:
        print("ERROR: Invalid age.")
else:
    print("ERROR: Invalid gender.")

print("-------------")

# 15. Electricity bill
units = int(input("Enter number of units: "))
if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 5
else:
    bill = (200 * 5) + (units - 300) * 10
print("Total bill: Rs.", bill)

print("-------------")

# 16. Oldest and youngest among three
a = int(input("Enter age of person 1: "))
b = int(input("Enter age of person 2: "))
c = int(input("Enter age of person 3: "))
print("Oldest age:", max(a, b, c))
print("Youngest age:", min(a, b, c))
