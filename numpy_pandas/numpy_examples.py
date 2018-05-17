import numpy as np 

# matrix attributes
array = np.array([[1,2,3],[4,5,6]])
print (array)
# print dimension
print('num of dim: ', array.ndim)
# print shape
print ('shape: ', array.shape)
# print size
print ('size: ', array.size)

# type of an array is dtype
a = np.array([2,3,4], dtype=np.int64)
print (a.dtype) 

# generate an array with all zeros
a = np.zeros((3,4))
print (a)

# generate an empty matrix
a = np.empty((3,4))
print (a)

# generate a ranged matrix with interval
a = np.arange(10, 20, 2)
print (a) 

# change matrix dimensions
a = np.arange(12).reshape((3,4))
print (a)

# generate a line space 
a = np.linspace(1,10,20) # automatically match the interval, 20 is the number of lines
print (a)

"""""""""""""""""""""""""""""""""""""""
Video 5
"""""""""""""""""""""""""""""""""""""""
a = np.array([10,20,30,40])
b = np.arange(4)
c = a - b
print (a, b)
print (c)
d = b**2
print (d)
c = 10*np.tan(a)
print (c)
# what are thoes values < 3
print (b < 3) 
print (b==3)

# matrix computation
a = np.array([[1,1],
            [0,1]])
b = np.arange(4).reshape((2,2))
print (a)
print (b)
# multiply one by one
c = a*b 
# matrix multiplication
c_dot = np.dot(a, b)
c_dot_2 = a.dot(b)
print (c)
print (c_dot)
print (c_dot_2)

# overall operation
a = np.random.random((2,4))
print (a)
print (np.sum(a))
print (np.min(a))
print (np.max(a))

# only for a row
# axis = 0 is for row
# axis = 1 is for column
print (np.sum(a, axis=0))
print (np.sum(a, axis=1))
print (np.min(a, axis=0))


"""""""""""""""""""""""""""""""""""""""
Video 6
"""""""""""""""""""""""""""""""""""""""
A = np.arange(14, 2, -1).reshape(3,4)
print (A)
# index of the minimum value
print (np.argmin(A))
# index of the maximum value
print (np.argmax(A))
# accumulate sum 
print (np.cumsum(A))
# accumulate diff
print (np.diff(A))
# index of nonzero elements
print (np.nonzero(A))
# sort
print (np.sort(A))
# matrix transpose
print (A.T)
print ((A.T).dot(A))
# all elements > 9 will be reset as 9 and elements < 5 will be reset as 5
print (np.clip(A, 5, 9))
# operation on column
print (np.mean(A, axis=0)) 
# operate on row 
print (np.mean(A, axis=1))

"""""""""""""""""""""""""""""""""""""""
Video 7
"""""""""""""""""""""""""""""""""""""""
A = np.arange(3,15).reshape((3,4))
print (A)
# two indexing methods
print (A[1][1])
print (A[1,1])
# the whole row
print (A[2:])
# the whole column
print (A[:,1])
