import numpy as np

# Question 1
A = np.arange(1, 10, 2)
B = np.arange(2, 11, 2)
dot = np.dot(A, B)
print(f"Dot of A and B is: {dot}")

# Question 2
C = np.outer(A, B)
print(f"Sum of all elements in C is: {np.sum(C)}")
print(f"Trace of C is: {np.trace(C)}")

# Question 3
M = np.array([[17, 24, 1, 8, 15], [23, 5, 7, 14, 16], [4, 6, 13, 20, 22], [10, 12, 19, 21, 3], [11, 18, 25, 2, 9]], dtype=np.double)
print(f"Product of all elements in M is: {np.prod(M)}")

# Question 4
inverse = np.linalg.inv(M)
print(f"Inverse of M is:\n {inverse}")
print(f"Transpose of M is:\n {M.T}")
D1 = np.matmul(inverse, M.T)
D2 = inverse * M.T
print(f"|D1|*|D2| is : {np.linalg.det(D1) * np.linalg.det(D2)}")