## What is NumPy?

"""
NumPy is a Python library used for working with arrays.

It has functions for working in domain of linear algebra, fourier transform, and matrices.

NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
"""

## Why Use NumPy?

"""
In Python we have lists that serve the purpose of arrays, but they are slow to process.

NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

The array object in NumPy is called `ndarray`, it provides a lot of supporting functions that make working with `ndarray` very easy.
"""

## Import NumPy

# Once NumPy is installed, import it in your applications by adding the `import` keyword:
import numpy as np

## NumPy as np

"""
NumPy is usually imported under the np alias.
Create an alias with the as keyword while importing:
"""
import numpy as np

## Checking NumPy Version

# The version string is stored under __version__ attribute.
import numpy as np

print(np.__version__)

## Create a NumPy ndarray Object

"""
NumPy is used to work with arrays.
The array object in NumPy is called `ndarray`.
We can create a NumPy `ndarray` object by using the `array()` function.
"""
import numpy as np

arr = np.array([101, 201, 301, 401, 501])

print(arr)

print(type(arr))

## Dimensions in Array

"""
A dimension in arrays is one level of array depth (nested arrays).
"""

### 0-Dimension

"""
0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.
"""
import numpy as np

classNum = int(input("How many students are in the CSC 102 class?"))

class_arr = np.array(classNum)

if (class_arr == 1):
    print("There is only ", class_arr, "student in CSC 102 class" )
else:
    print("There are", class_arr, "students in CSC 102 class" )

### 1-D Arrays

"""
An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.
These are the most common and basic arrays.
"""
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

### 2-D Arrays

"""
An array that has 1-D arrays as its elements is called a 2-D array.
These are often used to represent matrix or 2nd order tensors.
"""
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print(arr)

### 3-D arrays

"""
An array that has 2-D arrays (matrices) as its elements is called 3-D array.
These are often used to represent a 3rd order tensor.
"""
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(arr)

## Check Number of Dimensions?

"""
NumPy Arrays provides the `ndim` attribute that returns an integer that tells us how many dimensions the array have
"""
import numpy as np

a = np.array(42)
b = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([1, 2, 3, 4, 5])


print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

## Higher Dimensional Arrays

"""
An array can have any number of dimensions.
When the array is created, you can define the number of dimensions by using the ndmin argument.
In this array the innermost dimension (5th dim) has 4 elements, the 4th dim has 1 element that is the vector, the 3rd dim has 1 element that is the matrix with the vector, the 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.
"""
import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=8)

print(arr)
print('number of dimensions :', arr.ndim)

## Access Array Elements

"""
Accessing array elements is quite similar to accessing elements in a regular Python list.
"""
import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[1])

## Access 2-D Arrays

"""
To access elements from 2-D arrays, we can use comma separated integers representing the dimension and the index of the element.
"""
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])

## Access 3-D Arrays

"""
To access elements from 3-D arrays, we can use comma separated integers representing the dimensions and the index of the element.
"""
import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

## Negative Indexing

"""
Negative indexing means starting from the end of the array.
"""
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('Last element from 2nd dim: ', arr[1, -1])

## Slicing arrays

"""
Slicing in python means taking elements from one given index to another given index.
We pass slice instead of index like this: `[start:end]`.
We can also define the step, like this: `[start:end:step]`.
If we don't pass start its considered 0
If we don't pass end its considered length of array in that dimension
If we don't pass step its considered 1
"""

# Slice elements from index 1 to index 5 from the following array:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[1:5])

# Slice elements from index 4 to the end of the array:
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[4:])

# Slice elements from the beginning to index 4 (not included):
import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])

print(arr[:4])

## Checking the Data Type of an Array

"""
NumPy arrays have the data type attribute that returns the data type of the array:
"""
import numpy as np

int_arr = np.array([1, 2, 3, 4])

str_arr = np.array(['apple', 'banana', 'cherry'])

print(int_arr.dtype)

print(str_arr.dtype)

## Iterating Arrays

"""
Iterating means going through elements one by one.
"""
# Iterate on each scalar element of the 2-D array:

import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

for x in arr:
    for y in x:
        print(y, x)

# Iterate on the elements of the following 3-D array:

import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    print(x[0][1])
    print(x[1][0])

## Joining NumPy Arrays

"""
We can concatenate two or more arrays into a single array using `np.concatenate()`.
"""
# Join two arrays

import numpy as np

arr1 = np.array([1, 2, 3])

arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))

print(arr)

## Splitting NumPy Arrays

"""
We can split an array into multiple sub-arrays using `np.array_split()`.
"""
# Splitting is reverse operation of Joining.

# Joining merges multiple arrays into one and Splitting breaks one array into multiple.

# We use `array_split()` for splitting arrays, we pass it the array we want to split and the number of splits.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr)

# Access splitted arrays

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print(newarr[0])
print(newarr[1])
print(newarr[2])

## Splitting 2-D Arrays

"""
We can split 2-D arrays into multiple 2-D arrays.
"""
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])

newarr = np.array_split(arr, 3)

print(newarr)
