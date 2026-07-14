# ==========================================================
# Error Handling in Python
# ==========================================================

# Error handling prevents the program from crashing.
# It allows us to handle unexpected errors and display
# meaningful messages to the user.


# ==========================================================
# Example 1 - Index Error
# ==========================================================

lst = [1, 2, 3, 4, 5]

# print(lst[5])
# Raises IndexError because index 5 does not exist.



# ==========================================================
# Example 2 - ZeroDivisionError
# ==========================================================

# print(20 / 0)
# Raises ZeroDivisionError.



# ==========================================================
# Using try and except
# ==========================================================

# Python uses "try" and "except" to handle exceptions.

userInput = int(input("Enter Number: "))

try:
    print(20 / userInput)
except:
    print("Enter a non-zero number.")



# ==========================================================
# Handling a Specific Exception
# ==========================================================

value = "forty-two"

try:
    number = int(value)
    print(f"Converted: {number}")

except ValueError:
    # This block runs only for ValueError.
    print(f"Could not convert '{value}' to an integer.")



# ==========================================================
# Handling All Exceptions
# ==========================================================

# Exception is the parent class of most built-in exceptions.

try:
    print(20 / userInput)

except Exception as e:
    print(f"Error Occurred: {e}")



# ==========================================================
# Multiple Except Blocks
# ==========================================================

# Different exceptions can be handled separately.

try:
    file = open("./iofiles/myiofile.txt", "r")

except FileNotFoundError as f:
    print(f"Error Occurred: {f}")

except Exception as e:
    print(f"Error: {e}")



# ==========================================================
# Traceback Module
# ==========================================================

# The traceback module provides detailed error information,
# including the file name and line number.

import traceback

try:
    print(100 / 0)

except Exception as e:
    print(traceback.format_exception(e))



# ==========================================================
# else and finally
# ==========================================================

# else:
# Executes only if no exception occurs.

# finally:
# Always executes whether an exception occurs or not.
# It is commonly used for cleanup tasks like:
# - Closing files
# - Closing database connections
# - Releasing resources


# Example 1

try:
    file = open("./iofiles/myiofile.txt", "r")

except FileNotFoundError as f:
    print(f"Error Occurred: {f}")

else:
    print(f"File loaded successfully: {len(file.read())} characters.")

finally:
    print("Attempted")



# Example 2

try:
    file = open("./iofiles/file.txt", "r")

except FileNotFoundError as f:
    print(f"Error Occurred: {f}")

else:
    print(f"File loaded successfully: {len(file.read())} characters.")

finally:
    print("Attempted")