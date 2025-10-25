# 1. Print numbers 1 to 10 using for loop
for i in range(1, 11):
    print(i)

print("-------------")

# 2. Print numbers 20 to 1 using while loop
i = 20
while i >= 1:
    print(i)
    i -= 1

print("-------------")

# 3. Print even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

print("-------------")

# 4. Print numbers 1 to n (user input)
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i)

print("-------------")

# 5. Print odd numbers from 1 to n
n = int(input("Enter a number: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i)

print("-------------")

# 6. Print "Happy Birthday!" five times
for i in range(5):
    print("Happy Birthday!")

print("-------------")

# 7. Print first n squares (1² to n²)
n = int(input("Enter a number: "))
print(f"The first {n} terms of the series are:")
for i in range(1, n + 1):
    print(i ** 2, end=" ")
print()

print("-------------")

# 8. Multiplication table of a number
n = int(input("Enter a number: "))
print(f"Multiplication table of {n}:")
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

print("-------------")

# 9. Arithmetic progression (3, +4) first 8 terms
start = 3
diff = 4
for i in range(8):
    print(start + i * diff, end=" ")
print()

print("-------------")

# 10. Geometric sequence (2, ×3) first 6 terms
start = 2
ratio = 3
for i in range(6):
    print(start * (ratio ** i), end=" ")
print()

print("-------------")

# 11. Sum of numbers 1 to n
n = int(input("Enter a positive integer: "))
total = 0
for i in range(1, n + 1):
    total += i
print("Sum from 1 to", n, "is:", total)

print("-------------")

# 12. Sum of reciprocals from 1 to n
n = int(input("Enter a positive integer: "))
total = 0
for i in range(1, n + 1):
    total += 1 / i
print(f"Sum of reciprocals from 1 to {n} is: {round(total, 2)}")

print("-------------")

# 13. Running total of 5 numbers
total = 0
for i in range(5):
    num = int(input("Enter a number: "))
    total += num
print("Final running total is:", total)

print("-------------")

# 14. Factorial of a number
n = int(input("Enter a number: "))
if n < 0:
    print("Factorial does not exist for negative numbers.")
elif n == 0:
    print("The factorial of 0 is 1.")
else:
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    print(f"The factorial of {n} is {fact}.")

print("-------------")

# 15. Power of a number without using **
base = float(input("Enter base number: "))
exponent = int(input("Enter exponent: "))
result = 1
if exponent > 0:
    for i in range(exponent):
        result *= base
elif exponent < 0:
    for i in range(-exponent):
        result /= base
# exponent = 0 → result remains 1
print(f"{base} raised to the power of {exponent} is: {result}")
