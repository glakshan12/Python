import numpy as np
"""arr=np.array([1,2,3])#1d
print(arr)
#2d
arr2d=np.array([[1,2,3],[4,5,6]])
print(arr2d)
#3d
arr3d=np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
                ])
print(arr3d)
print(arr.ndim)
print(arr3d.ndim)
print(arr.shape)
print(arr2d.size)
print(arr.dtype)
print(arr.itemsize)
print(arr.nbytes) """

#indexing and slicing
arr1=np.array([10,20,30,40,50])
print(arr1[0])#normal indexing
print(arr1[0:3])#slicing
arr2=np.array([[10,20,30],[40,50,60]])
print(arr2[0,1])#2d indexing
print(arr2[[1,0],[1,1]])# fancy indexing 2d
print(arr2[0])
print(arr2[1])
print(arr2[0:2])#row range slicing
print(arr2[:,1])#coloumn wise slicing
print(arr2[:,0])#coloumn wise slicing
print(arr2[0:2,0:2])#two rows slicing

#boolean indexing
print(arr2[arr2>30])
arr = np.array([10,20,30,40,50])
print(arr[[0,1,4]])#this is fancy indexing but cant do it correctly
#2d fancy indexing 
arr2d=np.array([
    [1,2,3],
    [4,5,6]
])
print(arr2d[[0,1],[1,2]])
 
