# 1. Bonus 5% if service > 5 years
salary = float(input("Enter your salary: "))
years = int(input("Enter years of service: "))
if years > 5:
    bonus = salary * 0.05
    print("Bonus Amount:", bonus)
else:
    print("No bonus")

print("-------------")

# 2. Check voting eligibility (age >= 18)
age = int(input("Enter your age: "))
if age > 17:
    print("Eligible for voting")
else:
    print("Not eligible for voting")

print("-------------")

# 3. Check even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even number")
else:
    print("Odd number")

print("-------------")

# 4. Check divisibility by 7
num = int(input("Enter a number: "))
if num % 7 == 0:
    print("Number is divisible by 7")
else:
    print("Number is not divisible by 7")

print("-------------")

# 5. Print Hello if multiple of 5, else Bye
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("Hello")
else:
    print("Bye")

print("-------------")

# 6. Display last digit of a number
num = int(input("Enter a number: "))
print("Last digit is:", num % 10)

print("-------------")

# 7. Check if rectangle or square
length = int(input("Enter length: "))
breadth = int(input("Enter breadth: "))
if length == breadth:
    print("It is a Square")
else:
    print("It is a Rectangle")

print("-------------")

# 8. Greatest among two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Greatest number is:", a)
elif b > a:
    print("Greatest number is:", b)
else:
    print("Both are equal")

print("-------------")

# 9. Shop discount 10% if total cost > 1000 (cost per item = 100)
quantity = int(input("Enter quantity: "))
cost = quantity * 100
if cost > 1000:
    cost = cost - (cost * 0.10)
print("Total cost:", cost)

print("-------------")

# 10. Grading system
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

# 11. Check exam eligibility based on attendance
classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))
percentage = (classes_attended / classes_held) * 100
print("Attendance percentage:", round(percentage, 2), "%")
if percentage >= 75:
    print("Allowed to sit in exam")
else:
    print("Not allowed to sit in exam")

print("-------------")

# 12. Attendance with medical cause option
classes_held = int(input("Enter number of classes held: "))
classes_attended = int(input("Enter number of classes attended: "))
percentage = (classes_attended / classes_held) * 100
medical = input("Do you have a medical cause? (Y/N): ")
print("Attendance percentage:", round(percentage, 2), "%")
if percentage >= 75 or medical.upper() == 'Y':
    print("Allowed to sit in exam")
else:
    print("Not allowed to sit in exam")

print("-------------")

# 13. Check leap year
year = int(input("Enter a year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

print("-------------")

# 14. Determine work location based on age, gender, marital status
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
        print("ERROR: Invalid age range.")
else:
    print("ERROR: Invalid gender input.")

print("-------------")

# 15. Electricity bill calculation
units = int(input("Enter number of units: "))
if units <= 100:
    bill = 0
elif units <= 300:
    bill = (units - 100) * 5
else:
    bill = (200 * 5) + (units - 300) * 10
print("Total bill amount: Rs.", bill)

print("-------------")

# 16. Find oldest and youngest among three people
a = int(input("Enter age of person 1: "))
b = int(input("Enter age of person 2: "))
c = int(input("Enter age of person 3: "))

oldest = max(a, b, c)
youngest = min(a, b, c)

print("Oldest age:", oldest)
print("Youngest age:", youngest)
