# Q1. Create a new file "practice.txt" and Add the following data in it.
# Hi everyone
# We are learning file I/O
# using Java
# i lIKE Programming in Java

with open("practice.txt", "w") as f:
    f.write("Hi everyone")
    f.write("\nWe are learning file I/O")
    f.write("\nusing Java")
    f.write("\ni lIKE Programming in Java")


# Q2. WAP that replace all occurrence of Java with Python in above file.

with open("practice.txt", "r") as f:
    data = f.read()
    newData = data.replace("Java", "Python")

with open("practice.txt", "w") as f:
    f.write(newData)


# Q3. Search if the word learning exist in the above file or not

with open("practice.txt", "r") as f:
    data = f.read()
    if "learning" in data:
        print("exist")
    else:
        print("not exist")

# Q4. Write a program to find all the lines in a file where the word "learning" occurs. Print the line numbers where it is found. If the word is not found in any line, do not print anything.

with open("practice.txt", "r") as f:
    data = True
    idx = 1
    while(data):
        r = f.readline()
        if("learning" in r):
            print("learning found on line no", idx)
            data = False
        idx+=1


# Q5. Q: Write a program to read numbers from a file, print all even numbers, and display their count.
with open("last_question_practice.txt", "r") as f:
    data = f.read()
    count = 0
    splitiedList = data.split(",")
    for i in splitiedList:
        if(int(i) % 2 == 0):
            print(i)
            count+=1
    print("And there are",count,"even numbers")