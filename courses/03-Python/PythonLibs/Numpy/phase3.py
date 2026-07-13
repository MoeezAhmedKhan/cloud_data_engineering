import numpy as np
import matplotlib.pyplot as plt

# We can save numpy arrays We have builtin method to save numpy arrays

# Now Make Array
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.random.rand(3,3)
arr3 = np.zeros((4,4))

np.save('array1.npy',arr1)
np.save('array2.npy',arr2)
np.save('array3.npy',arr3)

# We can load numpy array and can get data
loadedArray1 = np.load('array1.npy')
loadedArray2 = np.load('array2.npy')
loadedArray3 = np.load('array3.npy')

print(f"Loader Array 1 \n{loadedArray1}")
print(f"Loader Array 2 \n{loadedArray2}")
print(f"Loader Array 3 \n{loadedArray3}")

# An image is just a grid of pixels, where each pixel stores 3 numbers (Red, Green, Blue), and all those pixels together can be stored as a NumPy array.

try:
    logo = np.load('numpy-logo.npy') # Load pixels from image and save into logo variable
    plt.figure(figsize=(12,5))
    plt.subplot(1,2,1)
    plt.imshow(logo) # Draw image
    plt.title("Numpy Image")
    plt.grid(False)

    darklogo = 1 - logo
    plt.subplot(1,2,2)
    plt.imshow(darklogo)
    plt.title("Numpy Dark Image")
    plt.grid(False)

    plt.show() # Display image on screen
except FileNotFoundError:
    print("Logo not found!")