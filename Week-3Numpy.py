# Numpy
# Core Library for scientific computing in python
# Data Science, machine learning, Deep learning 
# scikit-learn, matplotlib, pandas..
# High Performance multidimensional array -> FAST!
# Mathematical operations with arrays
# A lot of code written in C

# Numpy UseCases 
# Array/Matrix operations - Linear Algebra
# Dot Product
# Matrix multiplications
# Linear System
# inverse, determinant 
# Eigenvectors
# Random numbers
# Working with image represented as array 

import numpy as np

a = np.array([1,2,3])
print(a)
print(a.shape)
print(a.dtype)
print(a.ndim)
print(a.size)
print(a.itemsize)
print(a[0])

a[0] = 10
print(a)

b = a * np.array([2,0,2])
print(b)

l = [1,2,3]
a = np.array([1,2,3])

l = l + [4]
print(l)

a = a + np.array([4])
print(a)

l = l * 2
print(l)
a = a * 2
print(a)

# Dot product 
l1 = [1,2,3]
l2 = [4,5,6]

dot = 0
for i in range(len(l1)):
	dot += l1[i] * l2[i]
print(dot)	

# Speed test 
import numpy as np
from timeit import default_timer as timer

a = np.random.randn(1000)
b = np.random.randn(1000)

A = list(a)
B = list(b)

T = 1000

def dot1():
    dot = 0
    for i in range(len(A)):
        dot += A[i] * B[i]
    return dot	

def dot2():
    return np.dot(a, b)

# Timing dot1 (Python list-based dot product)
start = timer()
for t in range(T):
    dot1()
end = timer()
t1 = end - start

# Timing dot2 (NumPy vectorized dot product)
start = timer()
for t in range(T):
    dot2()
end = timer()
t2 = end - start

print('List dot product time:', t1)
print('NumPy dot product time:', t2)
print('Speed ratio (list/NumPy):', t1 / t2)


Multidimensional array and (nd) arrays
import numpy as np 

a = np.array([1,2])
print(a)
print(a.shape)

a = np.array([[1,2], [3,4]])
print(a)
print(a.shape)
print(a.T)

a = np.array([[1,2], [3,4]])
print(np.linalg.inv(a))
print(np.linalg.det(a))
print(np.diag(a))

indexing / slicing / Boolean indexing
import numpy as np 

a = np.array([[1, 2], [3, 4]])
print(a)

b = a[0, 1]
print(b)

# Slicing
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a)

b = a[-1, -1]
print(b)

# Boolean indexing
import numpy as np
a = np.array([[1,2], [3,4], [5,6]])
print(a)

bool_idx = a > 2
print(bool_idx)
print(a[bool_idx])


a = np.array([[1,2], [3,4], [5,6]])
print(a)

print(a[a > 2])

b = np.where(a>2, a, -1)
print(b)

a = np.array([10,19,30,41,50,61])
print(a)
b = [1,3,5]
print(a[b])

a = np.array([10,19,30,41,50,61])
print(a)
even = np.argwhere(a%2==0).flatten()
print(a[even])

# Reshapping Array 
import numpy as np

# Creating a 1D array with values from 1 to 6
a = np.arange(1, 7)
print("Original array:", a)

# Reshape to 2 rows and 3 columns
reshaped_a = a.reshape(2, 3)
print("Reshaped array:\n", reshaped_a)


a = np.arange(1, 7)
print(a)
print(a.shape)
b = a[:, np.newaxis]
print(b)

# Concatenation 
import numpy as np
a = np.array([[1,2], [3,4]])
print(a)
b = np.array([[5,6]])
c = np.concatenate((a,b), axis=None)
print(c)

import numpy as np
a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
# hstack, vstack
c = np.vstack((a,b))
#c = np.hstack((a,b))
print(c)


# Broadcasting 
import numpy as np

x = np.array([[1,2,3], [4,5,6], [1,2,3], [4,5,6]])
a = np.array([1,0,1])
y = x + a
print(y)

Functions and Axis
import numpy as np

a = np.array([[7,8,9,10,11,12,13], [17,18,19,20,21,22,23]])
print(a)
print(a.sum(axis=None))
print(a.sum(axis=0))
print(a.mean(axis=1))
print(a.var(axis=None))
print(a.std(axis=None))
print(a.min(axis=1))
print(a.max(axis=1))

# Datatypes
import numpy as np
x = np.array([1,2])
print(x)
print(x.dtype)

Copying
import numpy as np

a = np.array([1,2,3])
b = a.copy()
b[0] = 42
print(b)
print(a)

# Generating arrays
import numpy as np

a = np.zeros((2,3))
print(a)

a = np.ones((2,3))
print(a)

a = np.full((2,3), 5.0)
print(a)

a = np.eye(3)
print(a)

a = np.arange(20)
print(a)

a = np.linspace(0,10,5)
print(a)


# Random Numbers
import numpy as np

a = np.random.random((3,2)) #0-1
print(a)

a = np.random.randn(1000) #normal /Gaussian
print(a.mean(), a.var())

a = np.random.randint(10,size=(3,3))
print(a)

a = np.random.choice(5, size=10)
print(a)

import numpy as np

a = np.random.choice([-8, -7, -6], size=10)
print(a)

# Linear Algebra 
import numpy as np

a = np.array([[1,2], [3,4]])
eigenvalues, eigenvectors = np.linalg.eig(a)

print(eigenvalues)
print(eigenvectors) # Column vectors!

# e_vec * e_val = A * e_vec
b = eigenvectors[:,0] * eigenvalues[0]
print(b)
c = a @ eigenvectors[:,0]
print(b)

# print(b==c)

print(np.allclose(b,c))


# Solving Linear System 
# The admission fee at a small fair is $1.50 for children and $4.00 for adults. On a certain day, 2200 people enter the fair an $5050 is
# collected. How many children and holw many adults attended ?

import numpy as np
A = np.array([[1,1],[1.5,4.0]])
b = np.array([2200,5050])

# x = np.linalg.inv(A).dot(b)
# print(x)

# Best way to solve this

x = np.linalg.solve(A, b) # This
print(x)

# loading CSV file 
# np.loadtxt, np.genfromtxt
data = np.loadtxt('spambase.csv', delimiter=",",dtype=np.float32)
print(data)















