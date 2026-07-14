# ==========================================================
# File Handling, CSV & JSON
# ==========================================================


# ==========================================================
# File Modes
# ==========================================================

# Mode    Meaning             Creates File?      Overwrites Data?
# ---------------------------------------------------------------
# "r"     Read                No                 No
# "w"     Write               Yes                Yes
# "a"     Append              Yes                No
# "x"     Create              Yes                Error if file exists
# "r+"    Read and Write      No                 No


# ==========================================================
# 1. Reading a File
# ==========================================================

file = open("./iofiles/file.txt", "r")

# Read complete file
readed = file.read()
print(type(readed))
print(readed)

# Read first 3 characters
selectedChar = file.read(3)
print(selectedChar)

# Read first line
lineRead1 = file.readline()
print(lineRead1)

# Read second line
lineRead2 = file.readline()
print(lineRead2)

file.close()



# ==========================================================
# 2. Write Mode ("w")
# ==========================================================

# "w" removes old data before writing new data.

wr = open("./iofiles/writer.txt", "w")

wr.write("This is the file for learning Python.")

wr.write("This text will overwrite previous data.")

wr.close()



# ==========================================================
# 3. Append Mode ("a")
# ==========================================================

# "a" adds new data at the end of the file.

app = open("./iofiles/writer.txt", "a")

app.write("This is the appended text.")
app.write("\nThis is the second appended line.")
app.write("\nThis is the third appended line.")

app.close()



# Note:
# "w" and "a" create the file automatically if it does not exist.



# ==========================================================
# 4. Create Mode ("x")
# ==========================================================

# "x" creates a new file.
# It gives an error if the file already exists.

newfile = open("./iofiles/myfile.txt", "x")

newfile.write("Hello! This is x mode.")

newfile.close()



# ==========================================================
# 5. Read and Write Mode ("r+")
# ==========================================================

# "r+" allows both reading and writing.
# The file must already exist.

ffile = open("./iofiles/file.txt", "r+")

ffile.write("This is r+ mode.")
ffile.write("\nI am practicing file handling.")

ffile.writelines([
    "\nThis is writelines() function.",
    "\nIt writes multiple lines.",
    "\nAt one time."
])

print(ffile.read())

ffile.close()



# Important:
#
# After write(), the file pointer moves to the end of the file.
#
# read() starts reading from the current pointer position.
#
# Since the pointer is already at the end,
# read() returns an empty string.
#
# Move the pointer to the beginning before reading.
#
# Example:
#
# ffile.seek(0)
# print(ffile.read())



# ==========================================================
# 6. Using "with" Keyword
# ==========================================================

# "with" automatically closes the file.

with open("./iofiles/file.txt", "r") as file:

    fileRead = file.read()          # Read complete file

    content = file.readline()       # Read first line

    myContent = file.readlines()    # Read all lines

print(myContent)

for i in myContent[:2]:
    print(i)



# ==========================================================
# 7. Write Multiple Lines
# ==========================================================

with open("./iofiles/mycontent.txt", "w") as file:

    con = [
        "City : Karachi\n",
        "Status : Active\n",
        "ID : 23098\n"
    ]

    file.writelines(con)



# ==========================================================
# 8. Append Data Using "with"
# ==========================================================

with open("./iofiles/mycontent.txt", "a") as file:

    file.write("\nName : Ali")



# ==========================================================
# 9. Delete a File
# ==========================================================

import os

# os.remove("./iofiles/myphonedirectory.txt")




# ==========================================================
# PRACTICE QUESTIONS
# ==========================================================


# ----------------------------------------------------------
# Question 1
# ----------------------------------------------------------
#
# File contains:
#
# Ali
# Ahmed
# Usman
# Ali
# Hamza
# Ali
#
# Tasks:
# 1. Count total lines.
# 2. Count how many times "Ali" appears.
#
# Write your solution below:

with open("./iofiles/practice.txt", 'r') as pracFile:
    totalLine = 0
    nameCount = 0
    fileLines = pracFile.readlines()
    for i in range(len(fileLines)):
        totalLine += 1
        if(str(fileLines[i]).strip() == "Ali"):
            nameCount += 1
print(f"Name count: {nameCount} \nTotal lines: {totalLine}")            
            


# ----------------------------------------------------------
# Question 2
# ----------------------------------------------------------
#
# File contains:
#
# Python is easy
# Learning Python
# Flutter and Python
# Java
#
# Ask the user for a word.
# Print every line number where that word exists.
# If not found, print "Word not found".
#
# Write your solution below:

with open("./iofiles/practice.txt", 'r') as pracFile:
    fileLines = pracFile.readlines()
    getInput = True
    while getInput:
        foundList = []
        getInput = input("Input your word | For terminal enter exit: ")
        if(getInput.lower() == "exit"):
            getInput = False
            break
        for i in range(len(fileLines)):
            if(getInput in fileLines[i]):
                foundList.append(i+1)
        
        if(len(foundList) != 0):
            for i in foundList:
                print("Word Found At Line: ",i)
        else:
            print("Word Not Found")
                
        



# ----------------------------------------------------------
# Question 3
# ----------------------------------------------------------
#
# File contains:
#
# 12,45,23,78,90,11,8,100
#
# Tasks:
# 1. Print all even numbers.
# 2. Print all odd numbers.
# 3. Print the sum of all even numbers.
#
# Write your solution below:

with open("./iofiles/practice.txt", 'r') as pracFile:
    practiceFile = pracFile.readline().split(",")
    sumOfEven = 0
    for i in practiceFile:
        if(int(i) % 2 == 0):
            sumOfEven+=int(i)
            print(i, "is Even")
        else:
            print(i, "is Odd")
    print("Sum of even is ", sumOfEven)
    



# ----------------------------------------------------------
# Question 4
# ----------------------------------------------------------
#
# Read a text file and find:
#
# 1. Total lines
# 2. Total words
# 3. Total characters
#
# Write your solution below:

with open("./iofiles/practice.txt", 'r') as pracF:
    myFile = pracF.readlines()
    totalLine = 0
    toTalWord = 0
    totalChar = 0
    for i in myFile:
        totalLine += 1
        toTalWord += len(i.split(" "))
        for j in range(len(i)):
            if(i[j]):
                totalChar += 1
        
    print(f"Total Lines: {totalLine}")
    print(f"Total Lines: {toTalWord}")
    print(f"Total Char: {totalChar}")



# ----------------------------------------------------------
# Question 5
# ----------------------------------------------------------
#
# File contains:
#
# Ali,87
# Ahmed,45
# Usman,91
# Hamza,39
# Sara,72
#
# Print:
#
# Passed Students
#
# Failed Students
#
# Passing marks = 50
#
# Write your solution below:

with open("./iofiles/practice.txt", 'r') as pf:
    dictnory = {}
    listOfStudent = [] 
    
    # Data cleaning because the file has raw data
    for x in pf.readlines():
        pFile = x.split(",")
        for i in range(len(pFile)):
            if(i == 0):
                dictnory["name"] = pFile[0].strip()
            else:
                dictnory["marks"] = pFile[1].strip()
            
        listOfStudent.append(dictnory)
        dictnory = {}
        
    for i in listOfStudent:
        if(int(i["marks"]) >= 50):
            print(f"{i["name"]} is passed marks {i["marks"]}")
        else:
            print(f"{i["name"]} is failed marks {i["marks"]}")




# ----------------------------------------------------------
# Question 6
# ----------------------------------------------------------
#
# File contains:
#
# Ali,11111111111
# Ahmed,22222222222
# Usman,33333333333
# Hamza,44444444444
# Ali,66666666666
#
# Ask the user for a name.
# Print the phone number if found.
# Otherwise print "Contact not found".
#
# Write your solution below:

with open("./iofiles/practice.txt", 'r') as myf:
    directory = {}
    listOfDirectory = []
    foundNumber = [] # may have multiple same names in phone directry.
    
    # Data cleaning because the file has raw data
    for x in myf.readlines():
        value = x.split(",")
        for i in range(len(value)):
            if(i == 0):
                directory["name"] = value[i].strip()
            else:
                directory["phone"] = value[i].strip()
            
        listOfDirectory.append(directory)
        directory = {}
       
    strInput = input("Search Name in Directory: ")
    for i in listOfDirectory:
        if(strInput == i["name"]):
            foundNumber.append(i["phone"])
    
    if len(foundNumber) != 0:
        print("Number Found: ", foundNumber)
    else:
        print("Contact Not Found")
            
            
        





# ==========================================================
# CSV Files
# A CSV (comma-separated values) file stores tabular data as plain text. 
# Each line is a row. Each value within a row is separated by a comma. The first row is usually a header.
# ==========================================================


import csv

with open("./iofiles/employees.csv", "r") as csvFile:
    readedFile = csv.DictReader(csvFile)
    for i in readedFile:
        print(i['id'], "-", i["name"])
        
# Write:

records = [
    {"id": 1, "name": "Alice", "department": "Engineering", "status": "active"},
    {"id": 2, "name": "Bob",   "department": "Finance",     "status": "active"},
]

with open("./iofiles/output.csv", "w", newline="") as f:
    fieldnames = ["id", "name", "department", "status"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(records)
    


# ==========================================================
# Working with JSON
# JSON (JavaScript Object Notation) is the data format of APIs and configuration files. 
# It looks almost identical to a Python dictionary — key-value pairs, arrays, nested objects.
# ==========================================================

import json

# json.loads() parses a JSON string into a Python object:

response = '{"status": "ok", "records": 4200, "errors": null}'
data = json.loads(response)

print(data)

# json.dumps() converts a Python object into a JSON string:

result = {
    "pipeline": "daily_load",
    "rows_loaded": 9500,
    "success": True
}

json_string = json.dumps(result)
print(json_string)
print(type(json_string))