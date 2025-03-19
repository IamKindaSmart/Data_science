import numpy as np

#array slicing
#array[start:end:skip]
linear_array=np.array([1,2,3,4,5,6,7,8,9])
print(linear_array[0:4])
print(linear_array[:7])
print(linear_array[::2])
print(linear_array[::-1])

mutli_array=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(mutli_array[1,1])
print(mutli_array[0:1,0:1])
print(mutli_array[0:2,0:2])

#exercise - create a matrix of 7*7 and take out the middle 3*3 cross-section out of the 7*7 matrix
matrix=np.arange(1,50).reshape(7,7)
print(matrix)
cross_section=matrix[2:5,2:5]
print(cross_section)

#conditional selection of elements from array
#select even numbers

even = linear_array[linear_array%2==0]
print(even)

#compare with value
print(linear_array[linear_array==6])

#selection with index
print(linear_array[[2,4,6]])

#exercise - select the value less than 5 from an array of 1-10
less_than_5 = linear_array[linear_array<5]
print(less_than_5)

#operations on each element using loops
for i in range(0, len(linear_array)):
    linear_array[i] += 1
print(linear_array)

#witout using loops
k = np.array([1,2,3,4,5,6,7])
k += 1
print(k)