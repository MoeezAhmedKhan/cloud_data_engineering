# Loops in python - repeat a block of code multiple times
# There are two types of loops in python
# 1. While Loop
# 2. For Loop

# While Loop - A while loop is used to execute a block of code repeatedly as long as a given condition is true.

# while(True):
#     print("This is an infinite loop") #infinite loop

count = 1 # iterator
while(count <= 5): # condition
    print("Count is :",count) # iteration
    count+=1 
print("Last value of count: ",count)

# Make loop in reverse order

x = 5
while(x >= 1):
    print("New Count is :",x)
    x-=1 

# Lets practice:

# Q1. Print numbers 1 to 100

a = 1
while(a <= 100):
    print("Count is :",a)
    a+=1

# Q2. Print numbers 100 to 1

b = 100
while(b >= 1):
    print("Count is :",b)
    b-=1

# Q3. You have any number like 2 print the table of 2

tbleNo = 2
count = 1
while(count <= 10):
    print(tbleNo,"x",count,"=",count*tbleNo)
    count+=1

# Q4. Print the following list using loop. list is [1,4,6,9,2,12,16,20,24,28]

idx = 0
numbs = [1,4,6,9,2,12,16,20,24,28]
while(idx < len(numbs)):
    print(numbs[idx])
    idx+=1

# Q4. Searched a number in this list using loop. list is [1,4,6,9,2,12,16,20,24,28]

i = 0
lstt = [1,4,6,9,2,12,16,20,24,28]
searchNumber = 24
while(i < len(lstt)):
    if(lstt[i] == searchNumber): # This is the example of linear search its mean search element in the list one by one
        print("Searched successfully:",lstt[i],"and found at index:",i)
    i+=1


# Break : used to terminate the loop 
# Continue : terminate execution in the current iteration & continue execution from next iteration

z = 0
while(z < 5):
    if(z == 3):
        break
    print(z)
    z+=1
print("Loop ended through break statement")

x = 0
while(x < 5):
    if(x == 2):
        x+=1
        continue # skip current iteration
    print(x)
    x+=1
print("Loop ended")


# For loop is used to perform a sequenial traversal. For traversing list, string, tuple etc.

fruits = ["Apple", "Mango", "Banana", "Orange"]

for val in fruits:
    print(val)

tple = (1,2,4,6,33,8,45)
for val in tple:
    print(val)

strng = "HelloCoders"
for val in strng:
    print(val, end=" ") # The end parameter prevents the output from moving to the next line.
else: # This block executes after the loop completes without a break.
    print("\nTask ended")

# LiKe
x = 0
while(x < 5):
    if(x == 3):
        break
    print(x)
    x+=1
else: # In this case else with not run because loop terminated through break.
    print("Loop ended through break statement")

#Lets Practice:

# Q1. Print the following list using loop. list is [1,4,6,9,2,12,16,20,24,28]

numbers = [1,4,6,9,2,12,16,20,24,28]

for i in numbers:
    print(i)

# Q2. Searched a number in this tuple using loop. tple is (1,4,6,9,2,12,16,20,24,28)

tple = (1,4,6,9,2,12,16,20,24,28)
searchNumber = 12
for i in tple:
    if(i == searchNumber):
        print("Searched successfully using for loop:",i)


# Range - range return a sequene of numbers, starting from 0 amd stop before a specified number.

print(range(5))

for v in range(5): # start from 0 which is optional and 5 is end value
    print(v)

print("------------------------")

for v in range(2, 10): # range(start, stop)
    print(v)

print("------------------------")

for v in range(5, 50, 5): # Last one is step size which is also a option parameter but i want the step size will be 5
    print(v)

# Lets Practice

# Q1. Print number 1 to 100 through range

for i in range(1, 101):
    print(i)

# Q2. Print number 100 to 1

print("---------------- reverse -------------")
for i in range(100, 0, -1):
    print(i)


# Q3. Print a multiplication table of a number n through range

tbleNo = 4
for i in range(1, 11):
    print(tbleNo,"x",i,"=",tbleNo*i)

# pass is a null statement that does nothing. It is used as placeholder for future code.
 
for i in range(1, 100):
    pass  # This is a null statement and does not execute anything.

if(8 >= 5):
    pass  # This is also a null statement used as a placeholder.


# Lets do practice again.

# Q. Find the some of n natural number using while loop

num = 0
n = 1
while(n <= 100):
    num+=n
    n+=1
print("Sum of 1 to 100 is:",num)

# Q. WAP to find the factorial of first n number using for loop

fact = 5
temp = 1
while(fact >= 1):
    temp*=fact
    fact-=1

print("Factorial of 5 is",temp)




