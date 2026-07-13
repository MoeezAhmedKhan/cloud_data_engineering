# List Comprehension Practice Examples
# Example syntax [new_item for item in iterable if condition]

# 1. Take words from list which have more than 5 letters
words = ["apple", "banana", "grape", "kiwi", "mango", "pear"]

# Loop through each word, check if its length is greater than 5
arr = [i for i in words if len(i) > 5]
print("Words with length > 5:", arr)


# 2. Take numbers divisible by both 3 and 5
nums = [3, 5, 9, 12, 18, 20, 25, 30]

# Check if a number is divisible by 3 AND 5 at the same time
arr = [n for n in nums if n % 3 == 0 and n % 5 == 0]
print("Numbers divisible by both 3 and 5:", arr)


# 3. Take names that start with an uppercase letter
names = ["ali", "Moeez", "Sara", "hamza", "John"]

# Check the first character of each name → isupper() returns True if it's capital
arr = [i for i in names if i[0].isupper()]
print("Names starting with uppercase:", arr)


# 4. Capitalize the first letter of every word in a sentence
sentence = "Python is very powerful and fun to learn"

# Split the sentence into words, then capitalize each word
arr = [i.capitalize() for i in sentence.split(" ")]
print("Capitalized words:", arr)


# 5. Convert temperatures from Celsius to Fahrenheit
temps_c = [0, 10, 20, 30, 40]

# Formula: F = (C * 9/5) + 32
arr = [(i * 9/5) + 32 for i in temps_c]
print("Temperatures in Fahrenheit:", arr)
