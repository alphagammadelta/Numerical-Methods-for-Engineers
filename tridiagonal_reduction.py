'''Tridiagonal Reduction Method'''
import numpy as np

def given_reduction(A):
    n = A.shape[0]
    iterations = 0

    for k in range(n - 2):
        x = A[k+1:, k]
        v = x.copy()
        v[0] += np.sign(x[0]) * np.linalg.norm(x)

        
        H = np.eye(n)
        H[k+1:, k+1:] -= 2.0 * np.outer(v, v) / np.dot(v, v)

        
        A = H @ A @ H

        iterations += 1

        # Display the matrix at each iteration
        print(f"Iteration {iterations}:")
        print(A)
        print()

    return A

# Example usage
A = np.array([[1, 2, 3, 4],
              [2, 5, 6, 7],
              [3, 6, 8, 9],
              [4, 7, 9, 10]])

tridiagonal_matrix = given_reduction(A)
