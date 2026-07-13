# File Handling, CSV & JSON

# Opening and Reading Files

# Mode	Meaning	Creates file?	Overwrites?
# "r"	Read	No — error if missing	No
# "w"	Write	Yes                    	Yes — wipes existing content
# "a"	Append	Yes	                    No — adds to end
# "x"	Create	Yes — error if exists	No
# "r+"	Read and write	No	            No

# 1
# file = open("./datafiles/file.txt", "r")

# print(file.read())

# 2
# wr = open("./datafiles/writer.txt", 'w')
# wr.write("This is the file for learning python ")

# wr.write("This is the file for learning python ") # 'w override the file'
# wr.close()

#3
# app = open("./datafiles/writer.txt", 'a')
# app.write("This is the appended text")
# app.write("\nThis is the second line for appended text")
# app.write("\nThis is the third line for appended text")
# app.close()


#4
# newfile = open("./datafiles/myfile.txt", "x")
# newfile.write("Hello This is x mode")

#5
# ffile = open("./datafiles/file.txt", "r+")
# print(ffile.read())
# ffile.write("\nThis is r+ mode")
# ffile.write("\nI am in practice mode")
# ffile.writelines([
#     "This is the wrilines function",
#     "For create multiple line in a file"
#     "At a time"
# ])

# ffile.close()


# with keyward

# with open("./datafiles/file.txt", "r") as file:
#     # fileRead = file.read() # Read whole file at a time
#     # content = file.readline() # Read first line
#     myContent = file.readlines() # Read line by line

# print(myContent)
# for i in myContent[:2]:
#     print(i)

with open("./datafiles/mycontent.txt", 'w') as file:
    con = [
        "City: Karachi \n",
        "Status : Active \n",
        "Id: 23098 \n"
    ]
    file.writelines(con)

with open("./datafiles/mycontent.txt", 'a') as file:
    file.write("Name: Ali")


# Now working with CSV



