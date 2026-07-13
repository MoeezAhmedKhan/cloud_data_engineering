# Practice Questions

import numpy as np

# Q1 – Create and reshape an array
# Task: Create a 1D array of numbers from 1 to 20 and reshape it into a 4x5 matrix.
orignalArr = np.arange(1, 21)
reShapedArr = orignalArr.reshape(4,5)
print(f"Rehaped Array \n{reShapedArr}")

# Q2 – Access a specific element
# Task: Access the element 42 from the given 2D array using indexing.
arr = np.array([
    [10, 20, 30],
    [40, 41, 42],
    [50, 51, 52]
])
print(f"Access Specific Index {arr[1,2]}")

# Q3 – Filter odd numbers using mask and np.where
# Task: Create an array 1–20 and print only odd numbers.
myArr = np.arange(1, 21)
masked = myArr[myArr % 2 != 0]
print(f"Get Odd Numbers With Masked {masked}")
where = np.where(myArr % 2 != 0)
print(f"Get Odd Numbers With Where {myArr[where]}")

# Q4 – Element-wise arithmetic operations
# Task: Perform addition, multiplication, and division element-wise.
a = np.array([5, 10, 15, 20])
b = np.array([2, 4, 6, 8])
print(f"Addition {np.add(a,b)}")
print(f"Multiplcation {np.multiply(a,b)}")
print(f"Dividition {np.divide(a,b)}")

# Q5 – Stack arrays
# Task: Stack two 2x2 arrays vertically and horizontally.
x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
print(f"Added a new array (y) in the row of existing array (x) \n{np.vstack((x,y))}")
print(f"Added a new array (y) in the column of existing array (x) \n{np.hstack((x,y))}")

# Q6 – Sorting by axis
# Task: Sort each row and each column of a 3x3 matrix.
arr = np.array([[9, 2, 7],
                [4, 6, 1],
                [3, 8, 5]])
print(f"Sorting each column \n{np.sort(arr, axis=0)}")
print(f"Sorting each row \n{np.sort(arr, axis=1)}")

# Q7 – Delete and insert elements
# Task: Delete 3rd element and insert 99 at index 2.
arr = np.array([10, 20, 30, 40, 50])
deleted = np.delete(arr,2)
newArr = np.insert(deleted, 2, 99)
print(f"Inserted a new element {newArr}")

# Q8 – Reshape, transpose, flatten
# Task: Reshape 1D → 2D → transpose → flatten back to 1D.
mArr = np.arange(1,13)
reShapedmArr = mArr.reshape(3,4)
transpose = reShapedmArr.T # Transpose = swap rows/cols
flatten_back = transpose.flatten() # Back to 1D
print(f"Orignal Array \n{mArr}")
print(f"Reshaped Array \n{reShapedmArr}")
print(f"Transposed Array \n{transpose}")
print(f"Flatten Back \n{flatten_back}")

# Q9 – Filter with condition
# Task: Create random array (0–100), show elements > 50.
randomArr = np.random.randint(0, 101,size=15)
filteredRandomArr = randomArr[randomArr > 50]
print(f"Orignal Array {randomArr}")
print(f"Filtered Array {filteredRandomArr}")

# Q10 – 3D Tensor Info
# Task: Create 3D array (2,3,4) and show info (shape, ndim, size, first block)
array = np.arange(24)+1
reshapedArray = array.reshape((2,3,4))
print(f"Reshaped Array \n{reshapedArray}")
print(f"Its Shape {reshapedArray.shape}")
print(f"No of Dimention {reshapedArray.ndim}")
print(f"Total Elements {reshapedArray.size}")
print(f"The First Matric \n{reshapedArray[0]}")


print("----------------Practice Questions End Now Start Practice 2-----------------")