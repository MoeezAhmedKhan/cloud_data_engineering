# List - list is a builtin data type that store collection of different values from different datatypes.
# string is immutable but list is mutable

student = ["Ali", 22, "10th", "Karachi", 90.25]
print(student)
print(type(student))
print(student[0])
print(len(student))

student[0] = "Bilal" #This is the example of list mutable
print(student)

# Slicing of List
numbers = [23, 33, 55, 78, 56, 90, 32]
print(numbers[2:])
print(student[-1]) #Also the list can support negative indexing. and its return the last value from list

# List of method
numbers.append(11)
print(numbers)

numbers.sort()
print(numbers)

a = ['a', 'b', 'c']
a.sort(reverse=True)
print(a)

b = [2, 1, 4]
b.reverse()
print(b)

b.insert(0, 100)
print(b)

b.remove(2)
print(b)

b.pop(0)
print(b)

print(b.count(4))

#Tuple - Tuple is immutable builtin datatype for create sequence of value.

tup = ('Apple', 'Banana', 'Mango')
print(tup)
print(type(tup))

tup2 = (2,) #If we have only a number in a tuple so we use ',' after number else tuple will be consiton as integer
print(tup2)
print(type(tup2))
#You can also apply slicing in tuple.

# Tuple methods

print(tup.index('Mango')) #index will return the index of searched value.
print(tup.count('Mango'))

# WAP to ask the user input 3 times and store the movie name in a list

movieList = []

# userInput1 = input("Enter first movie name: ")
# userInput2 = input("Enter second movie name: ")
# userInput3 = input("Enter third movie name: ")
# movieList.append(userInput1)
# movieList.append(userInput2)
# movieList.append(userInput3)
# print("Movies are:",movieList)

#Short way:
movieList.append(input("Enter first movie name: "))
movieList.append(input("Enter second movie name: "))
movieList.append(input("Enter third movie name: "))
print("Movies are:",movieList)

#WAP to check if a list contain palindrom elements. (User copy method)

# A palindrome is a term that defines a sequence where the start and end elements are the same when read in reverse order. 
# For example: [10, 20, 20, 10]

palindromList = ["Apple", "Banana", "Banana", "Apple"]
copyOfPalindromList = palindromList.copy()
copyOfPalindromList.reverse()

if(palindromList == copyOfPalindromList):
    print("This is palindrome", palindromList)
else:
    print("This is not a palindrome", palindromList)

#WAP to count the number of student have A grade from the tuple

grades = ('A','B','A','C','D','A','A')
print(grades.count('A'))

#WAP to sort from A-Z same tuple but with the list formate.
grades = ['A','B','A','C','D','A','A']
grades.sort()
print(grades)