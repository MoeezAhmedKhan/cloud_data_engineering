# ==============================
# Loops in Python
# ==============================

# ----------------------------------
# for loop
# ----------------------------------

for i in range(5):
    print(i)


# ----------------------------------
# for loop with string
# ----------------------------------

name = "Python"

for ch in name:
    print(ch)


# ----------------------------------
# for loop with list
# ----------------------------------

numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)


# ----------------------------------
# for loop with tuple
# ----------------------------------

tup = (1, 2, 3, 4)

for item in tup:
    print(item)


# ----------------------------------
# for loop with set
# ----------------------------------

mySet = {10, 20, 30}

for item in mySet:
    print(item)


# ----------------------------------
# for loop with dictionary
# ----------------------------------

student = {
    "name": "Ali",
    "age": 20,
    "city": "Karachi"
}

for key in student:
    print(key)

for value in student.values():
    print(value)

for item in student.items():
    print(item)


# ----------------------------------
# range()
# ----------------------------------

for i in range(5):
    print(i)

for i in range(2, 8):
    print(i)

for i in range(1, 11, 2):
    print(i)


# ----------------------------------
# while loop
# ----------------------------------

i = 1

while i <= 5:
    print(i)
    i += 1


# ----------------------------------
# Infinite loop (Avoid)
# ----------------------------------

# while True:
#     print("Infinite Loop")


# ----------------------------------
# break
# ----------------------------------

for i in range(10):

    if i == 5:
        break

    print(i)


# ----------------------------------
# continue
# ----------------------------------

for i in range(10):

    if i == 5:
        continue

    print(i)


# ----------------------------------
# pass
# ----------------------------------

for i in range(5):
    pass


# ----------------------------------
# else with for
# ----------------------------------

for i in range(5):
    print(i)
else:
    print("Loop Completed")


# ----------------------------------
# else with while
# ----------------------------------

i = 1

while i <= 5:
    print(i)
    i += 1
else:
    print("Loop Completed")


# ----------------------------------
# Nested loop
# ----------------------------------

for i in range(3):

    for j in range(2):
        print(i, j)


# ----------------------------------
# enumerate()
# Used to get index and value together in a loop
# ----------------------------------

fruits = ["Apple", "Banana", "Orange"]

for index, value in enumerate(fruits):
    print(index, value)


# ----------------------------------
# Loop through dictionary
# ----------------------------------

student = {
    "name": "Ali",
    "age": 20,
    "city": "Karachi"
}

for key, value in student.items():
    print(key, value)