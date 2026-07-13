# Lambda Function VS Normal Function

# Normal func
def sum(x,y):
    print(x+y)

sum(10,5)

# lambda like an annonymous function
sum = lambda x,y:x+y
print(sum(20,20))

# Maximum of two numbers : Check which number is bigger
max = lambda x,y : x if x > y else y
print("Max",max(10, 14))

# Reversed string with lambda
rev = lambda x: x[::-1]
print("Reversed string:",rev("Python"))


# Working with pre defined function:

# Map : The map() function applies the same action or operation to every item in a list (or any collection) — without using a loop.
# example : map(function, iterable)

# Question 1
def sum(x):
    return x * x

sum_result = list(map(sum, [1,2,3,4,5]))
print(sum_result)

# With lambda
sum_result_With_lambda = list(map(lambda x:x+x, [2,4,6,8,10]))
print(sum_result_With_lambda)


# Question 2
names = ["Ali Khan", "Sara Ahmed", "Bilal Qureshi", "Hina Fatima", "Ahmed Raza"]
# Without lambda
def modify(n):
    splited = n.split(' ')
    return f'{splited[0][0]}.{splited[1][0]}'
        
newNames = list(map(modify,names))
print(newNames)

# With lambda
newNames = list(map(lambda n:n.split(' ')[0][0] + "."+ n.split(' ')[1][0],names))
print(newNames)


# Question 3
names = ["  ali khan ", "sara   ahmed", "  bilal qureshi", "hina FATIMA  ", "  ahmed  raza "]
# with lambda 
cleaned = list(map(lambda x:x.strip().title(),names))
print(cleaned)


# filter : The filter() function is used to pick only those items from a list (or any collection) that match a condition. 
# example : filter(function,iterable)

# Question 1: Keep Only Names with Vowels at the Start

names = ["Ali", "Sara", "Bilal", "Omar", "Hina", "Umer", "Raza", "Asad"]
filteredName = list(filter(lambda n : n[0].upper() in "AEIOU",names))
print(filteredName)

# Question 2: Filter Words with Length > 5 and Containing a Digit

words = ["apple12", "cat", "sunrise", "data9", "moon", "python3", "sky"]
filteredWords = list(filter(lambda x: len(x) >= 5 and any(c.isdigit() for c in x),words))
print(filteredWords)
# Here i have used any function which is similar to these functions and it return true/false on certain condition

# Question 3: Filter Students Who Passed Based On if Marks >= 60 and Attendance ≥ 80 

students = [
    {"name": "Ali", "marks": 78, "attendance": 90},
    {"name": "Sara", "marks": 60, "attendance": 75},
    {"name": "Bilal", "marks": 55, "attendance": 95},
    {"name": "Hina", "marks": 82, "attendance": 60},
    {"name": "Raza", "marks": 68, "attendance": 85}
]

filteredStudents = list(filter(lambda s: s['marks'] >= 60 and s['attendance'] >= 80,students))
print(filteredStudents)


# Reduce - combines all elements of a list step by step into one single result

# Question 1: Find Product of Only Even Numbers

from functools import reduce

numbers = [2, 5, 8, 3, 10, 15, 6]
evenNumber = [i for i in numbers if i % 2 == 0] # list comprehension
product = reduce(lambda x,y:x*y,evenNumber)
print(product)

# Question 2: Combine Words into a Sentence (Capitalizing Each Word)

words = ["hello", "my", "name", "is", "moeez"]
sentence = reduce(lambda w,y:f"{w} {y}".title(),words) 
print(sentence)

# Question 3: Find the Student with the Highest Marks

students = [
    {"name": "Ali", "marks": 78},
    {"name": "Sara", "marks": 92},
    {"name": "Bilal", "marks": 65},
    {"name": "Hina", "marks": 88}
]
highestMark = reduce(lambda s,x:s if s['marks'] > x['marks'] else x,students)
print(highestMark)



