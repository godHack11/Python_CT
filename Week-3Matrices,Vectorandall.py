# Vectors 
# Vectors are ordered array of numbers that represents a point or direction in space. In data science, vectors are used to represent
# data points, features or coefficients in machine learning models.

# Creating a vector 
# Creating a Horizontal Vector and Vertial Vector 

import numpy as np
list1 = [1, 2, 3]

list2 = [[10],
        [20],
        [30]]

vector1 = np.array(list1)

vector2 = np.array(list2)

print("Horizontal Vector")
print(vector1)

print("Vertical Vector")
print(vector2)

# Basic Arithmetic operation: 
# In this example we will see do arithmetic operations which are element-wise between two vectors of equal length to result in a new
# vector with the same length

# importing numpy
import numpy as np

# creating a 1-D list (Horizontal)
list1 = [5, 6, 9]

# creating a 1-D list (Horizontal)
list2 = [1, 2, 3]

# creating first vector
vector1 = np.array(list1)

# printing vector1
print("First Vector          : " + str(vector1))

# creating second vector
vector2 = np.array(list2)

# printing vector2
print("Second Vector         : " + str(vector2))

# adding both the vector
# a + b = (a1 + b1, a2 + b2, a3 + b3)
addition = vector1 + vector2

# printing addition vector
print("Vector Addition       : " + str(addition))

# subtracting both the vector
# a - b = (a1 - b1, a2 - b2, a3 - b3)
subtraction = vector1 - vector2

# printing addition vector
print("Vector Subtraction   : " + str(subtraction))

# multiplying  both the vector
# a * b = (a1 * b1, a2 * b2, a3 * b3)
multiplication = vector1 * vector2

# printing multiplication vector
print("Vector Multiplication : " + str(multiplication))

# dividing  both the vector
# a / b = (a1 / b1, a2 / b2, a3 / b3)
division = vector1 / vector2

# printing division vector
print("Vector Division       : " + str(division))

# Vector Dot Product 
# In mathematics, the dot product or scalar product is an algebraic operation that takes two equal-length sequences of numbers and 
# returns a single number. 
# For this we will use dot method.

import numpy as np
# creating a 1-D list (Horizontal)
list1 = [5, 6, 9]

# creating a 1-D list (Horizontal)
list2 = [1, 2, 3]

# creating first vector 
vector1 = np.array(list1)

# printing vector1
print("First Vector  : " + str(vector1))

# creating second vector
vector2 = np.array(list2)

# printing vector2
print("Second Vector : " + str(vector2))

# getting dot product of both the vectors
# a . b = (a1 * b1 + a2 * b2 + a3 * b3)
# a . b = (a1b1 + a2b2 + a3b3)
dot_product = vector1.dot(vector2)

# printing dot product
print("Dot Product   : " + str(dot_product))


# Vector-Scalar Multiplication 
# Multiplying a vector by a scalar is called scalar multiplication. To perform scalar multiplication, we need to multiply the scalar by 
# each component of the vector.

import numpy as np
# creating a 1-D list (Horizontal)
list1 = [1, 2, 3]

# creating first vector 
vector = np.array(list1)

# printing vector1
print("Vector  : " + str(vector))

# scalar value 
scalar = 2

# printing scalar value
print("Scalar  : " + str(scalar))
 
# getting scalar multiplication value
# s * v = (s * v1, s * v2, s * v3)
scalar_mul = vector * scalar

# printing dot product
print("Scalar Multiplication : " + str(scalar_mul))


# Matrices
# Matrix is a two-dimensional array of numbers. They are used to represent datasets, transformations or linear systems where rows 
# typically represent observations and columns represent features.

# Matrix operations
# 1. Matrix Addition & Subtraction
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

add = A + B
sub = A - B

print("Addition:\n", add)
print("Subtraction:\n", sub)

# 2. Matrix Multiplication
# a. Element-wise Multiplication
elementwise = A * B
print("Element-wise multiplication:\n", elementwise)

# b. Matrix Product (Dot Product)
product = np.dot(A, B)
# OR
product = A @ B  # Preferred in modern code
print("Matrix multiplication:\n", product)

# 3. Transpose of a Matrix
transpose = A.T
print("Transpose:\n", transpose)

# 4. Matrix Inverse (only for square & non-singular matrices)
inverse = np.linalg.inv(A)
print("Inverse:\n", inverse)

# 5. Matrix Determinant
det = np.linalg.det(A)
print("Determinant:", det)

# 6. Matrix Rank
rank = np.linalg.matrix_rank(A)
print("Rank:", rank)

# 7. Eigenvalues and Eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
print("Eigenvalues:\n", eigenvalues)
print("Eigenvectors:\n", eigenvectors)

# Matrix Transpose
# The transpose of a matrix is a new matrix whose rows are the columns of the original. 
# Using Numpy
import numpy as np

A = np.array([[1, 2], [3, 4]])

A_transpose = A.T  # .T is the transpose attribute
print("Original Matrix:\n", A)
print("Transposed Matrix:\n", A_transpose)

# Without NumPy (Using Lists)
A = [[1, 2], [3, 4]]

# Using list comprehension
A_transpose = [[A[j][i] for j in range(len(A))] for i in range(len(A[0]))]

print("Original Matrix:", A)
print("Transposed Matrix:", A_transpose)

# Identity Matrix
# An identity matrix is a square matrix in which all the elements of the main diagonal are 1 and all other elements are 0.
# Creating an Identity Matrix Using NumPy
import numpy as np

I = np.identity(3)  # 3x3 identity matrix
print("Identity Matrix:\n", I)

# Without NumPy (Using Lists)
size = 3
identity_matrix = [[1 if i == j else 0 for j in range(size)] for i in range(size)]

print("Identity Matrix:")
for row in identity_matrix:
    print(row)

# Zero Matrix
# A Zero Matrix (also called a Null Matrix) is a matrix in which all elements are 0.
import numpy as np

Z = np.zeros((3, 3))  # 3x3 zero matrix
print("Zero Matrix:\n", Z)

# Sparse Matrix 
# A Sparse Matrix is a matrix that contains mostly zero values. It’s useful to store such matrices in optimized formats that save 
# memory and computation time.
import numpy as np
from scipy.sparse import csr_matrix

dense_matrix = np.array([
    [0, 0, 3],
    [0, 0, 0],
    [0, 4, 0]
])

sparse_matrix = csr_matrix(dense_matrix)

print("Sparse Matrix:\n", sparse_matrix)
print("Non-zero values:", sparse_matrix.data)

# Inverse of Matrix
# The inverse of a square matrix A is another matrix A^{-1} such that:
# A \cdot A^{-1} = I
# Where I is the identity matrix.

import numpy as np

A = np.array([[4, 7], [2, 6]])

# Compute inverse
A_inv = np.linalg.inv(A)

print("Original Matrix:\n", A)
print("Inverse Matrix:\n", A_inv)

# Matrix Decomposition 
# Matrix decomposition is a process where we break down a complex matrix into simpler into more manageable parts. 
# These parts include LU decomposition, QR decomposition or Singular Value Decomposition

# LU Decomposition is a matrix factorization technique where a matrix A is decomposed into:
# A = LU
# Where:
# L is a Lower triangular matrix
# U is an Upper triangular matrix
# Useful for:
# Solving linear systems
# Inverse computation
# Determinants
import numpy as np
from scipy.linalg import lu

A = np.array([[4, 3], [6, 3]])

P, L, U = lu(A)

print("Original Matrix A:\n", A)
print("Permutation Matrix P:\n", P)
print("Lower Triangular Matrix L:\n", L)
print("Upper Triangular Matrix U:\n", U)
print("Reconstruction (L @ U):\n", L @ U)

# Singular Value Decomposition (SVD) in Python
# Singular Value Decomposition (SVD) is a powerful matrix factorization technique used in:
# Dimensionality reduction (PCA)
# Image compression
# Recommender systems
# Latent semantic analysis (text mining)

# Determinants
# Determinant of a square matrix is a single number that tells us if the matrix can be turned around or not. It is is important when we 
# need to find the best possible answer or when we are solving systems of linear equations in math.

# Eigenvalues and Eigenvectors
# Eigenvalues and eigenvectors are used in various data science algorithms such as PCA for dimensionality reduction and feature 
# extraction.

# Vector Spaces and Subspaces
# A vector space is a set of vectors that can be scaled and added together and subspaces are subsets of a vector space used for 
# understanding data structures and transformations in machine learning.

# Systems of Linear Equations
# Systems of linear equations can be represented as matrices. Solving systems of linear equations is essential in regression analysis, 
# optimization and neural networks.

# Orthogonality
# Two vectors are considered orthogonal when their dot product evaluation results in a zero value. Data science makes use of 
# orthogonality for selecting features while conducting dimensionality reduction and establishing whether models operate independently 
# or not.

# Principal Component Analysis (PCA)
# PCA is a dimensionality reduction technique that transforms data into a smaller set of variables and capture the most significant 
# variance. It's used for feature extraction and noise reduction.

# Optimization in Linear Algebra
# Optimization means to find the best possible solution to a problem. Linear algebra applies this concept to solve problems involving 
# least squares regression as well as machine learning models and linear regression models.







