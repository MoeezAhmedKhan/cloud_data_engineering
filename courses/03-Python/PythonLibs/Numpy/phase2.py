  # Numpy Array Operations
  
import numpy as np

# Indexing and Slicing
npArr = np.array([1,2,3,4,5,6,7,8,9,10])
print(f"Basic Slicing {npArr[2:6]}")
print(f"With Step {npArr[:8:2]}")
print(f"With Negative Indexing {npArr[::-1][:2]}")

np2dArr = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])
print(f"Specific Element \n{np2dArr[0, 2]}") # First argument is for row and Second is for column
print(f"Entire Row \n{np2dArr[1]}")
print(f"Entire Column \n{np2dArr[:,2]}")


# Sorting

unsortedArr = np.array([4,7,5,9,3,0,2,4,5,9,1,6])
sorted = np.sort(unsortedArr)
print(f"Sorted Array \n{sorted}")

unsorted2dArr = np.array([
    [3, 1],
    [1, 2],
    [2, 3]
])
sorted2dArr = np.sort(unsorted2dArr, axis=0) # axis=0 -> sort down the columns (vertically)
print(f"Sorted 2D Array By Column \n{sorted2dArr}")

sorted2dArr = np.sort(unsorted2dArr, axis=1) # axis=1 -> sort across each row (horizontally) e.g (elements in every row will be sorted left to right) 
print(f"Sorted 2D Array By Row \n{sorted2dArr}")


# Filter

numbers = np.array([1,2,3,4,5,6,7,8,9,10])
evenNumbers = numbers[numbers % 2 == 0] # filter expression is here in the []
print(f"Even Numbers {evenNumbers}")

# Filter with mask

mask = numbers > 5 # Filter expression is also called mask
print(f"Numbers greater than five {numbers[mask]}")

# NumPy (NP) Where
where_result = np.where(numbers > 5)
print(f"Wehere results {numbers[where_result]}")

conditionalArr = np.where(numbers > 5, "True", "False") # Where condition satisfying so there return True else False
print(conditionalArr)


# Now Adding and Removing Data

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([2,3,4,5,6])

print(f"Addition in array {arr1 + arr2}")
print(f"Merge in array {np.concatenate((arr1,arr2))}")


# Array Compatibility

a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.array([9,10,11,12])
print(f"Checking Array Compatibily, Shape is Same in both array or not \n{a.shape == b.shape == c.shape}")


# Adding a new row in existing array

orignalArr = np.array([[1,2],[3,4],[5,6]])
new_Arr = np.array([11,22]) 
print(f"Adding a row in existing array \n{np.vstack((orignalArr,new_Arr))}") # Adds new_Arr as a new row at the end

# Adding a new column in existing array

orignalAr = np.array([[1,2],[3,4]])
new_Ar = np.array([[11,22], [33,44]])
print(f"Adding a column in existing array \n{np.hstack((orignalAr,new_Ar))}") # Adds new_Ar as a new column at the end of element


# Deleting element

arr = np.array([12,2,3,4,55,66])
deleted = np.delete(arr, 2) # Its take array and second argument used for slicing index
print(f"Array after deletion {deleted}")

# Adding in each element
arr = np.array([22,33,44,55,66])
added = np.add(arr,89) # The second argument (89) is added to each element of the existing array
print(f"Added in each element of array {added}")


print("----------------Phase Two End Now Lets Start Practice Questions-----------------")