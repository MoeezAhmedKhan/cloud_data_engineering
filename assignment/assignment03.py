# 1. Print alternate elements of a user-given list
lst = input("Enter elements separated by space: ").split()
print("Alternate elements are:", lst[::2])

print("-------------")

# 2. Reverse a list without using reverse()
lst = input("Enter elements separated by space: ").split()
rev = []
for i in range(len(lst) - 1, -1, -1):
    rev.append(lst[i])
print("Reversed list:", rev)

print("-------------")

# 3. Find largest number in a list without using max()
lst = list(map(int, input("Enter numbers separated by space: ").split()))
largest = lst[0]
for num in lst:
    if num > largest:
        largest = num
print("Largest number is:", largest)

print("-------------")

# 4. Rotate list elements (last element moves to first)
lst = input("Enter elements separated by space: ").split()
rotated = [lst[-1]] + lst[:-1]
print("Rotated list:", rotated)

print("-------------")

# 5. Delete a given word from a string
text = input("Enter a string: ")
word = input("Enter word to delete: ")
new_text = text.replace(word, "")
print("Updated string:", new_text.strip())

print("-------------")

# 6. Convert mm/dd/yyyy to Month day, year format
months = ["January", "February", "March", "April", "May", "June",
          "July", "August", "September", "October", "November", "December"]
date_str = input("Enter date (mm/dd/yyyy): ")
m, d, y = date_str.split("/")
m = int(m)
print(f"Formatted date: {months[m-1]} {int(d)}, {y}")

print("-------------")

# 7. Capitalize first letter of each word in a string
sentence = input("Enter a sentence: ")
words = sentence.split()
new_sentence = ""
for w in words:
    new_sentence += w.capitalize() + " "
print("Capitalized sentence:", new_sentence.strip())

print("-------------")

# 8. Find sum of each row in a matrix
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))
matrix = []
for i in range(m):
    row = list(map(int, input(f"Enter row {i+1} elements: ").split()))
    matrix.append(row)

for i in range(m):
    print(f"Sum of row {i+1} =", sum(matrix[i]))

print("-------------")

# 9. Add two matrices of size m x n
m = int(input("Enter number of rows: "))
n = int(input("Enter number of columns: "))

print("Enter elements for first matrix:")
mat1 = [list(map(int, input().split())) for _ in range(m)]

print("Enter elements for second matrix:")
mat2 = [list(map(int, input().split())) for _ in range(m)]

result = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(mat1[i][j] + mat2[i][j])
    result.append(row)

print("Sum of matrices:")
for row in result:
    print(row)

print("-------------")

# 10. Multiply two matrices
r1 = int(input("Enter rows of first matrix: "))
c1 = int(input("Enter columns of first matrix: "))
r2 = int(input("Enter rows of second matrix: "))
c2 = int(input("Enter columns of second matrix: "))

if c1 != r2:
    print("Matrix multiplication not possible!")
else:
    print("Enter first matrix:")
    mat1 = [list(map(int, input().split())) for _ in range(r1)]
    print("Enter second matrix:")
    mat2 = [list(map(int, input().split())) for _ in range(r2)]

    result = [[0 for _ in range(c2)] for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += mat1[i][k] * mat2[k][j]

    print("Resultant matrix after multiplication:")
    for row in result:
        print(row)
