# 1. Check current time and display appropriate greeting

import datetime as dt
import pytz

pk_time  = dt.datetime.now(pytz.timezone("Asia/Karachi"))
currentHour = pk_time.hour
print(f"Current Hour {currentHour}")

if(5 <= currentHour < 12): # if currentHour is greater then 5 means morning start and currentHour is less then 12. Morning end before 12
    print("Good Morning")
elif(12 <= currentHour < 17): # 12 to 5 - Afternoon
    print("Good Afternoon")
elif(17 <= currentHour <= 20): # 5 to 8 - Evening
    print("Good Evening")
else:
    print("Good Night")


# 2. Change order into reverse (Reverse number) - 1234 into 4321

num = int(input("Enter a number: "))
rev = 0

while num > 0: # Its mean any number end before zero in the reverse order.
    digit = num % 10       # Get the last digit of num
    rev = rev * 10 + digit # Append the digit to the reversed number
    num = num // 10        # Remove the last digit from num

print(rev)


# 3. Check if a number is a palindrome or not.
# Reverse the number and compare it with the original.
# If both are the same, then it is a palindrome.

num = int(input("Enter a number: "))
orignalNum = num
rev = 0
while(num > 0):
    digit = num % 10
    rev = rev * 10 + digit
    num = num // 10

if orignalNum == rev:
    print(orignalNum, "Its is orignal ",rev, "Its is reversed and its is paindrom")
else:
    print(orignalNum, "Its is orignal ",rev, "Its is reversed and its is not paindrom")


# 4. Check number is even or odd

num = int(input("Enter a anumber: "))
while(num != 0):
    if(num % 2 == 0):
        print(num, "is even")
    else:
        print(num, "is odd")
    num = int(input("Enter a anumber: "))
else:
    print(num, "is zero")
    

# 5. Print a table

num = int(input("Enter a anumber: "))
i = 1
while(i <= 10):
    print(num, "*", i, "=", (num * i))
    i = i + 1
else:
    print("Table Printed Successful")


# 6. Lets Start Develop a Small Game

questionList = [
    {
        "question": "Which planet is known as the Red Planet?",
        "answer": "Mars",
        "amount": 10,
        "isUserRight": False
    },
    {
        "question": "What is the chemical symbol for water?",
        "answer": "H2O",
        "amount": 20,
        "isUserRight": False
    },
    {
        "question": "Which language is used to create Android Apps?",
        "answer": "Kotlin",
        "amount": 30,
        "isUserRight": False
    },
    {
        "question": "Which is the largest ocean on Earth?",
        "answer": "Pacific Ocean",
        "amount": 40,
        "isUserRight": False
    },
    {
        "question": "Which device is used to measure atmospheric pressure?",
        "answer": "Barometer",
        "amount": 50,
        "isUserRight": False
    }
]

winingAmount = 0
i = 0

while i < len(questionList):
    print("\nQuestion no", i + 1, ":", questionList[i]["question"])
    getInput = input("Give your answer: ")

    if getInput.lower() == questionList[i]["answer"].lower():
        winingAmount += questionList[i]["amount"]
        questionList[i]["isUserRight"] = True
        print("Correct! You won", questionList[i]["amount"], "$")
    else:
        print("Wrong! Correct answer was:", questionList[i]["answer"])

    i += 1

print("\n--------------- Result ----------------\n")
print("🎉 Total Winning Amount:", winingAmount, "$ 🎉")

print("Wrong Questions with Correct Answers:\n")
for i in questionList:
    if not i["isUserRight"]:
        print("-", i["question"], "→", i["answer"])




# 7. Program to print the first 10 Fibonacci numbers

# The Fibonacci series is a list of numbers where each new number is made by adding the previous two numbers.
# The series always starts with 0 and 1.

# Step 1: Initialize the first two numbers of the Fibonacci sequence
n0 = 0
n1 = 1

# Step 2: Set how many Fibonacci numbers to print
count = 10

# Step 3: Use a loop to generate and print the series
for i in range(count):
    if i == 0:
        # Print the first Fibonacci number (0)
        print(n0, end=" ")
    elif i == 1:
        # Print the second Fibonacci number (1)
        print(n1, end=" ")
    else:
        # Calculate the next Fibonacci number
        result = n0 + n1

        # Print the result
        print(result, end=" ")

        # Update previous two numbers for the next iteration
        n0 = n1
        n1 = result




# 8. Write a Python program that takes a number n from the user and prints the Fibonacci number at that index along with the entire series up to that index.

# Program to find the nth Fibonacci number and print the full series

# Step 1: Initialize first two Fibonacci numbers
n0 = 0
n1 = 1

# Step 2: Take input from the user for which Fibonacci index they want
number = int(input("Enter a number to get Fibonacci value by index: "))

# Step 3: Create an empty list to store Fibonacci series
fabNumbers = []

# Step 4: Generate Fibonacci numbers up to the given index
for i in range(number):
    if i == 0:
        # First Fibonacci number is always 0
        fabNumbers.append(n0)
    elif i == 1:
        # Second Fibonacci number is always 1
        fabNumbers.append(n1)
    else:
        # Calculate the next Fibonacci number
        result = n0 + n1
        fabNumbers.append(result)

        # Update the previous two numbers for next loop
        n0 = n1
        n1 = result

# Step 5: Print the nth Fibonacci number
print("Fibonacci number at index", number, "is:", fabNumbers[number - 1])

# Step 6: Print the complete Fibonacci series up to that index
print("Full Fibonacci series up to index", number, "is:", fabNumbers)



# 9 Lets Start OS Moduke

import os
import shutil

if not os.path.exists("learn"):
    os.makedirs("learn") 

print(os.getcwd())
os.chdir("F:/Moeez/Cloud Data Engineering/python/learn") # change directory
print(os.getcwd())
i = 1
while i <= 100:
    # os.makedirs(f"learn/folder{i}")
    # os.rename(f"learn/folder{i}", f"learn/myfolder{i}")
    shutil.rmtree(f"myfolder{i}") # for delete directory
    i+=1


# WAP to check word lenght and its is greater than 3 then append random words in start and end else return word in reversed order

import random
import string
def encode_word(word):
    if len(word) >= 3:
        start = ''.join(random.choices(string.ascii_letters, k=3))
        end = ''.join(random.choices(string.ascii_letters, k=3))
        return f"{start}{word[1:]}{word[0]}{end}"
    else:
        return word[::-1]

print(encode_word(input("Give a word: ")))
print(encode_word(input("Give a word: ")))



# 10. Python File I/O: Read Student Marks from File, Assign Grades, and Generate Result Summary

# Before Code Improvement
studentFile = open("student.txt", 'r')
studentData = studentFile.read()
studentList = studentData.split("\n")
studentMap = []
for i in studentList:
    subList = i.split(',')
    for j in range(len(subList)):
        if(j == 0):
            studentMap.append({"name":subList[0], "marks":subList[1]})

for i in studentMap:
    if int(i['marks']) > 80:
        i['grade'] = 'A'
    elif int(i['marks']) >= 60 and int(i['marks']) < 79:
        i['grade'] = 'B'
    else:
        i['grade'] = 'Failed'


with open('result.txt','w') as f:
    for i in studentMap:
        f.write(f"{i['name']} - {i['grade']}{f' Grade' if i['grade'] != 'Failed' else ''}\n")



# After Code Improvement   
# Read file
with open("student.txt", 'r') as studentFile:
    studentList = studentFile.read().splitlines()

studentMap = []
for line in studentList:
    name, marks = line.split(',')
    studentMap.append({"name": name, "marks": marks})

# # Assign grades
for s in studentMap:
    if int(s['marks']) >= 80:
        s['grade'] = 'A'
    elif 60 <= int(s['marks']) < 80:
        s['grade'] = 'B'
    else:
        s['grade'] = 'Failed'

# # Write result file
with open("result.txt", "w") as f:
    for s in studentMap:
        grade_text = f"{s['grade']} Grade" if s['grade'] != 'Failed' else "Failed"
        f.write(f"{s['name']} - {grade_text}\n")

# # Print summary
total = len(studentMap)
a_count = sum(1 for s in studentMap if s['grade'] == 'A')
b_count = sum(1 for s in studentMap if s['grade'] == 'B')
fail_count = sum(1 for s in studentMap if s['grade'] == 'Failed')

print(f"Total Students: {total}")
print(f"A Grade: {a_count}")
print(f"B Grade: {b_count}")
print(f"Failed: {fail_count}")









