import numpy as np 
my_list=[1,2,3,4]
np_array=np.array(my_list)
print(np_array)
print(my_list)

"""
numpy operations: dimensions and shape
#dimensions - number of axes in matrix (number of rows and columns)


#function used to find dimension in ndim
shape - number of rows and columns
"""
np_array=np.array([[1,2],[3,4]])
dimensions = np_array.ndim
print(dimensions)

shape = np_array.shape
print(shape)

#accessing elements from np array
element = np_array[1,1]
print(element)

#create an array of range of values
arr=np.arange(0,15,2) #start_value, end_value(excluding), skip
print(arr)

#reshape - changing the dimensions of matrix
reshaped_array=np_array.reshape(1,4)
print(reshaped_array)

reshaped_array2=np_array.reshape(4,1)
print(reshaped_array2)

sorted_array = np.sort([3,4,5,1])
print(sorted_array)
