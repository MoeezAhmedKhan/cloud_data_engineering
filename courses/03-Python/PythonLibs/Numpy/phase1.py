# NumPy stands for Numerical Python.
# It is a Python library used to work with numbers, lists, and large amounts of data more easily and faster.

# pip install numpy (Run it firstly)

# Numpy array and Basics

import numpy as np

# One Dimentional Array:
oneDArr = np.array([1,2,3,4,5])
print(oneDArr)

twoDArr = np.array([[1,2,3],[4,5,6]])
print(twoDArr)

# Python List vs Numpy Array

lst = [1,2,3,4,5]
print(lst * 2)

npArr = np.array([1,2,3,4,5]) # element wise multiplication
print(npArr * 2)

# Checking time

import time
startTime = time.time()
pyList = [i for i in range(10000000)]
print(f"Python List Generation Time Taked : {time.time() - startTime}")

# VS

startTime = time.time()
np_Arr = np.arange(10000000)
print(f"NumPy List Generation Time Taked : {time.time() - startTime}")


# Creating array from scratch

zero = np.zeros((3,4)) # start count for row | end count for column and it gives a matric
print(f"Zero array \n{zero}") 

one = np.ones((2,4))
print(f"One array \n{one}") 


full = np.full([2,6], 6) # second argument define which element will be occur in the matric
print(f"Full array \n{full}")

random = np.random.random([3,3])
print(f"Random array \n{random}")

sequence = np.arange(10,20,2) # 3rd argument define the step which will be occur in the array it return 1D array 
print(f"Sequence array \n{sequence}")


# What is Vector / Matric / Tensor

# One Dimentional Array called vector
vector = np.array([1,2,3]) # Vector

# Two Dimentional Array called Matric
matric = np.array([[1,2,3],[4,5,6]]) # Matric

# N Dimentional Array called Tensor
tensor = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) # Tensor


# Now Move OnTo Array Properties

npArr = np.array([[1,2,3],
                  [4,5,6]])

print(f"Rows and Columns : {npArr.shape}")
print(f"Data Type of each element : {npArr.dtype}")
print(f"Dimention (Dept of array) : {npArr.ndim}")
print(f"Count of total elements : {npArr.size}")


# Now Move OnTo Array Reshaping

arrNp = np.arange(12)
print(f"One Dimentional Array \n{arrNp}")
reShaped = arrNp.reshape((3,4))
print(f"Reshaped One Dimentional to 2 Dimentional \n{reShaped}")

# Flattened array

flattened = reShaped.flatten()
print(f"Flattened array \n{flattened}") # reverse into orignal form amd its return a new copy of array

# Ravel array

ravel = reShaped.ravel()
print(f"Ravel array \n{ravel}") # reverse into orignal form amd its return orignal array

# Transpose array

transpose = reShaped.T # Elements of the rows become the elements of the columns, and vice versa
print(f"Transposed array \n{transpose}")


print("----------------Phase One End-------------------")