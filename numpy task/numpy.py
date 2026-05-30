import numpy as np

a = np.array([
    [11,22,33],
    [44,55,66],
    [77,88,99]
])
""" 1. Extract:- first column- last row- [
   [22 33]
   [55 66]
  """
a[:,0]
a[2,:]

a = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])
""" 2. Extract:- first row- second column- element 5 """
a[0,:]
a[:,1:2]
a[1,1]


""" 3. Create an array from 1 to 12 and reshape it into:- (3,4)- (2,6)- (2,3,2"""

b=np.arange(1,13)
b.reshape(3,4)
b.reshape(2,6)
b.reshape(2,3,2)

a = np.array([1,2,3])
b = np.array([4,5,6])

""" 4.Perform:- addition- subtraction- multiplication- division- power of 3- square- mean"""

print("adition:",a+b)
print("subtraction:",a-b)
print("multiplication:",a*b)    
print("division:",a/b)
print("power of 3:",a**3)
print("square:",a**2)
print("mean:",a.mean())

"""" 5. Create a 1D array containing numbers from 1 to 10 using random module.
Create a 2D array of shape (3,3) containing numbers from 1 to 9 using random module"""

a=np.random.randint(1,11,10)
b=np.random.randint(1,10,9).reshape(3,3)

""" 6. Generate a random array of shape (2,5)"""
a=np.random.rand(2,5)

""" 7. Difference between Python list and NumPy array
list can contain elements of different data types, while NumPy arrays are homogeneous and can only contain elements of the same data type."""

""" 8. Convert the following integer array into float datatype:"""
a = np.array([1,2,3,4])
a.astype(float)

""" 9. What is the difference between:- dtype- astype()
dtype() tell the data type of the elements in the array, while astype() is a method used to convert the data type of the elements in the array to a specified type."""

""" 10. Create a 2D array and print:- shape- size- ndim- dtype- Change its datatype"""
a=np.array([[1,2,3],[4,5,6]])
a.shape
a.size
a.ndim
a.dtype
a.astype(float)

""" 11. Can a 1D array be sliced like:
a[:,1]
Why or why not"""
"""No, a 1D array cannot be sliced like a[:,1] because it does not have multiple dimensions. The slicing syntax a[:,1] is used for 2D arrays to access the second column, but in a 1D array, there is only one dimension, so you would use a[1] to access the second element instead."""