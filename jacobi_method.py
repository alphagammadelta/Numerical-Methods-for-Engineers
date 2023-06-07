''''python code to find the eigenvalues and eigenvectors by using Jacobi's method which displays the values at each iteration'''
import numpy as np

def jacobi_eigenvalue(A, tol=1e-4, max_iter=100):
    n = A.shape[0]
    V = np.eye(n)
    iterations = 0

    while True:
        # Find the maximum off-diagonal element
        maxval = 0.0
        p = 0
        q = 0

        for i in range(n):
            for j in range(i+1, n):
                if abs(A[i, j]) > maxval:
                    maxval = abs(A[i, j])
                    p = i
                    q = j

        if maxval < tol or iterations >= max_iter:
            break

        # Compute the rotation angle
        if A[p, p] == A[q, q]:
            theta = np.pi / 4
        else:
            theta = 0.5 * np.arctan(2 * A[p, q] / (A[p, p] - A[q, q]))

        # Compute the rotation matrix
        c = np.cos(theta)
        s = np.sin(theta)
        R = np.eye(n)
        R[p, p] = c
        R[p, q] = -s
        R[q, p] = s
        R[q, q] = c

        # Update A and V
        A = R.T.dot(A).dot(R)
        V = V.dot(R)

        iterations += 1

        # Display eigenvalues and eigenvectors at each iteration
        eigenvalues = np.diag(A)
        eigenvectors = V.T
        print(f"Iteration {iterations}:")
        for i in range(n):
            print(f"Eigenvalue {i+1}: {eigenvalues[i]}")
            print(f"Eigenvector {i+1}: {eigenvectors[i]}")
        print()

    return eigenvalues, eigenvectors

# Example usage
A = np.array([[5, 2, 1],
              [2, 3, 1],
              [1, 1, 2]])

eigenvalues, eigenvectors = jacobi_eigenvalue(A)
