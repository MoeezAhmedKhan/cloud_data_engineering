# Reverse Slicing Concept - string[start:end:step]

# start → where to start slicing (index number)

# end → where to stop (but the end index is not included)

# step → how many steps to move at a time

# if step is positive, slicing goes left → right (forward)

# if step is negative, slicing goes right → left (backward / reverse)

text = "Programming"
# rev = text[::-1]
# print(rev[:5])
print(text[::-1][:5]) # shortcut in one line

text = "HelloWorld"
# rev = text[::-1]
# print(rev[3:7])
print(text[::-1][3:7])  # shortcut in one line

s = "abcdefg"
# print(s[::-2])
print(s[::-2])

quote = "SlicingIsPowerful"
# rev = quote[::-1]
# print(rev[3:8][::-1])
print(quote[::-1][3:8][::-1]) # shortcut in one line

