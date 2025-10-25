# 1. Count number of vowels in a string
s = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("Number of vowels:", count)

print("-------------")

# 2. Count uppercase, lowercase, digits, and spaces
s = input("Enter a string: ")
upper = lower = digit = space = 0
for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    elif ch.isspace():
        space += 1
print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)
print("Spaces:", space)

print("-------------")

# 3. Swap first and last characters of a string
s = input("Enter a string: ")
if len(s) <= 1:
    print("New string:", s)
else:
    new_s = s[-1] + s[1:-1] + s[0]
    print("New string:", new_s)

print("-------------")

# 4. Reverse the string manually
s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
print("Reversed string:", rev)

print("-------------")

# 5. Left shift a string by one position
s = input("Enter a string: ")
if len(s) > 1:
    new_s = s[1:] + s[0]
else:
    new_s = s
print("Shifted string:", new_s)

print("-------------")

# 6. Print initials of full name without using split()
name = input("Enter your full name (First Middle Last): ")
initials = name[0].upper() + ". "
for i in range(1, len(name)):
    if name[i - 1] == " " and name[i] != " ":
        initials += name[i].upper() + ". "
print("Initials:", initials.strip())

print("-------------")

# 7. Check if a string is palindrome
s = input("Enter a string: ")
rev = ""
for ch in s:
    rev = ch + rev
if s == rev:
    print("Palindrome")
else:
    print("Not a palindrome")

print("-------------")

# 8. Display cyclic left shift pattern (SHIFT → HIFTS → IFTSH → FTSHI → TSHIF → SHIFT)
s = "SHIFT"
for i in range(len(s) + 1):
    print(s)
    s = s[1:] + s[0]

print("-------------")

# 9. Validate password based on given rules
password = input("Enter your password: ")
has_upper = has_lower = has_digit = False

if len(password) >= 8:
    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True

    if has_upper and has_lower and has_digit:
        print("Password is valid.")
    else:
        print("Password must include at least one uppercase, one lowercase, and one digit.")
else:
    print("Password must be at least 8 characters long.")
