# Dictionary - Dictionary are used to store valye in a form of key value pair.
# They are unordered, mutable, and dont allow duplicate keys

info = {
    "key" : "value",
    "key" : "new value", # Duplicate key, this will overwrite the first one
    "name":"ali",
    "age":20,
    "topics" : ("dictionary", "set"),
    "subjects" : ["Python", "Flutter"],
    "is_adult" : True,
    ("Job", "Company") : ("Data Engineery", "Google") # We can only use tuple as key because tuple is immutable thats why.
}
print(info)
print(info["name"])
print(info[("Job", "Company")][0])

info["name"] = "Bilal" # assign a value into existing key
info["fatherName"] = "Ahmed" # add a new key into existing dictionary

print(info)

nullDictionary = {} # we can create null/empty dictionary


# Nested Dictionary

student = {
    "name":"Salman",
    "rollNo":3345,
    "marks":{
        "phy":66,
        "math":78,
        "eng":89,
        "chem":76
    }
}

print(student)
print(student['marks']['phy'])
print(len(student))

# Dictionary Methods:

print(student.keys()) # return all keys
print(student.values()) # return all values
print(student.items()) # return each pair in a list

print(student.get("name")) # return a value according to key but if key is not exist in the dictionary there will be no error and return only None
print(student["name"]) # return a value according to key but if key is not exist in the dictionary there will an error

moreInfo = {"year":"first year","subject":"Engineering"}
student.update(moreInfo) # insert a new dictionary into existing dictionary
print(student)


# Set: set is a collection of unique and unordered value and each element in a set is an immutable so we cant use list or dictionary in set.

# Set with only integers
collection1 = {1, 2, 3, 4} # Sets are unordered. Integer sets may appear ordered due to consistent hashing,
print(collection1)  # Output: {1, 2, 3, 4} (Consistent order)

# Set with mixed types
collection2 = {"world", 1, 2, 3, 4, "hello", "world"}
print(collection2)  # Output: Unordered (order may vary)

# Set with strings only
collection3 = {"apple", "banana", "cherry"}
print(collection3)  # Output: Unordered (order may vary)
print(type(collection3))
print(len(collection3))

newCollection = {} # empty set

# Set is Mutable but elements of set is immutable

# Method of sets

collection3.add("Orange") # add new items into existing set
print(collection3)

newCollection2 = {"Peach", "Lemon", "Pineapple"}
collection3.update(newCollection2) # update set with new items
print(collection3)

collection3.remove("Lemon") # remove item from the set
print(collection3)

numberCollection = {1,2,3,4,5,6,7,8,9}
print(numberCollection)
print(numberCollection.pop()) # Pop/Remove item into the set and return the popped value
print(numberCollection.pop()) # Pop/Remove item into the set and return the popped value

# Union and Intersection methods

# Union combine both set unique values and return new set
set1 = {1,2,3}
set2 = {4,5,6}
print(set1.union(set2)) 

# Intersection combine common value and return new set
set3 = {1,2,3}
set4 = {2,5,3}
print(set3.intersection(set4)) 

# Lets Practice

# Q-1. Store following words meanings in python dictionary
# table : "a peace of furniture", "list of fact and figures"
# cat : "a small animal"

# Q-2. You are given a list of subjects for students and assume one classroom is required for one student. How many classroom needed by all students?
# "python", "java", "c", "c++", "javascript", "c++", "python", "c", "dart", "php"

subjects = {"python", "java", "c", "c++", "javascript", "c++", "python", "c", "dart", "php"}
print(subjects)
print(len(subjects))

# WAP to take 3 subjects marks as input from user and store subject name one by one into empty dictionary. Use subject name as key and marks a value

marksCollection = {}
phyMarks = input("Enter phy marks")
marksCollection.update({"phy":phyMarks})

mathMarks = input("Enter math marks")
marksCollection.update({"math":mathMarks})

chemMarks = input("Enter chem marks")
marksCollection.update({"chem":chemMarks})
print(marksCollection)

# WAP to figure out the value 9 and 9.0 as seperate value in a set

mySet = {9, str("9.0")}
print(mySet)