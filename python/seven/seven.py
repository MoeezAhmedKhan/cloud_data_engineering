# File I/O in Python
# Python can be used to perform operations on a file. (read and write data)

# Open, read & close File
# We have to oepn a file before reading or writing

# f = open("filename","mod")

file = open("file.txt") # second parameter is option which is mode and bydefault mode is read 
# read = file.read()
# read = file.read(4) # Its mean i want to read only 4 starting characters
readLine1 = file.readline() # read line by line
print(readLine1)
readLine2 = file.readline()
print(readLine2)
# print(type(read))
file.close() # we must close file after performing task

# 'r': Open for reading (default mode).

# 'w': Open for writing, truncating the file first (overwrites if the file exists).

# 'x': Create a new file and open it for writing. Fails if the file already exists.

# 'a': Open for writing, appending to the end of the file if it exists.

# 'b': Binary mode (used for binary files).

# 't': Text mode (default mode, used for text files).

# '+': Open a disk file for updating (allows both reading and writing).

f = open("sample.txt","w") #"w" mode means we are writing to the file.If the file does not exist in the directory, it will be created automatically. If the file already exists, its previous content will be overwritten..
f.write("Hello, World This is python.\nAnd I am wiriting the text into file.\nThis text override all previous text in this file.")
f.close()

f = open("sample.txt","a")
f.write("\nI am appending this text in file if exist else first create this after that this text will append")
f.close()

f = open("demo.txt", "r+") # If file exist it will open for reading and writing both and override from starts. 
f.write("Abcd")
print(f.read())
f.close()

f = open("forw.txt", "w+") # Open the file in w+ mode. The existing content (if any) in example.txt will be deleted because of the truncation in w+.
print(f.read())
f.write("Again write hello world because text is truncated when program runs")
f.close()

f = open("forw.txt", "a+") # Open the file in a+ mode. The existing content (if any) in example.txt will be append from new content.
print(f.read())
f.write("\nThis text is appending into existing content")
f.close()

# Summarize we have covered
# r   - Read only, pointer at start, no truncate, error if file doesn’t exist.
# w   - Write only, pointer at start, truncates file, creates file if it doesn’t exist.
# a   - Append only, pointer at end, no truncate, creates file if it doesn’t exist.
# r+  - Read and write, pointer at start, no truncate, error if file doesn’t exist.
# w+  - Read and write, pointer at start, truncates file, creates file if it doesn’t exist.
# a+  - Read and append, pointer at end, no truncate, creates file if it doesn’t exist.


# # With New Syntax

with open("new_sample_file.txt","r") as f: # when we use with syntax so this will auto close your file we dont need to exlicit close
        data = f.read()
        print(data)

with open("new_sample_file.txt","w") as f:
        f.write("I am override the prev text into new text.")


print("---------------------------------------------------------------------------")

# Now Deleting a file
# using os module
# Module (like a code library) is a file written by another programmer that generally has a function we can use.

import os

os.remove("for_remove.txt") # file will be delete thorugh os.remove


