# String is a squence of characters
str1 = "This is a string.\nAnd we are learning python"
str2 = 'This is a string.'
str3 = """"This is also a string"""

# Escapsequence
# \n
# \t

#Concatination
mystr1 = "Maaz"
mystr2 = "Khan"
print(mystr1+mystr2)

#Length os string
print(len(mystr1))

#Indexing starts with 0
str = "Python"
print(str[0])

#Slicing - accessing part of a string - ending index is not included
newString = "This is python file for learning about string"
print(newString[8:19])
print(newString[20:len(newString)])
print(newString[:19]) #[0:19]
print(newString[0:])  #[0:len(newString)]

#Slicing with negative index

#  A  p  p  l  e
# -5 -4 -3 -2 -1

str = "Apple"
print(str[-1])

str2 = "This is an example of negative string"
print(str2[-6:-1])

str3 = "This is an example of negative string"
print(str2[-26:])


#string funtions

str = "i am a python programmer"
print(str.endswith("er"))
print(str.capitalize())
print(str.replace("python", "flutter"))
print(str.find("y")) # return index of y
print(str.count("p")) # how many time included this character/word in string

# WAP to take a user input and print its length
a = input("Enter your name: ")
print(len(a))

# WAP to check occurrence of $ in string

b = "This is an example to check occurrence of $ print the count of $"
print(b.count("$"))


# Conditional Statements
# if - elif - else

signal = "red"
if(signal == "green"):
    print("Go")
elif(signal == "red"):
    print("Stop")
elif(signal == "Yellow"):
    print("Look")
else:
    print("Signal is broken")

num = 18
if(num > 10):
    print("Number is greater than 10")
if(num > 15):
    print("Number is greater than 15")

# WAP to check the student grade according to their percentage

# Nesting if
age = 18
gender = "Female"
if(age >= 18):
    if(gender == "Male"):
        print("Access")
    else:
        print("Access denied")
        
else:
    print("You are not eligible")

# WAP to check the number is even or odd

i = int(input("Enter a number: "))
if(i % 2 == 0):
    print(i,"is even")
else:
    print(i,"is odd")

# WAP to check the number is multple of 7 or not. (Multiple means the number appear in the table of seven Or divide by 7 without any remainder)
# If a number is a multiple of 7, it means that the number is divisible by 7 without leaving any remainder.

a = 14
if(a % 7 == 0):
    print(a,"is Multple of 7")
else:
    print(a,"is not Multple of 7")

# WAP to take 3 input from user and check which number is greater

numb1 = int(input("Enter number one: ")) 
numb2 = int(input("Enter number two: ")) 
numb3 = int(input("Enter number three: ")) 

if(numb1 >= numb2 and numb1 >= numb3):
    print(numb1,"is first largest number")
elif(numb2 >= numb3):
    print(numb2,"is second largest number")
else:
    print(numb3,"is third largest number")
