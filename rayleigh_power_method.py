'''
Python code for finding largest Eigenvalue and Eigenvector by Rayleigh Power method where the code displays the value at each iteration
'''
import numpy as np

def rayleigh_power(A, epsilon, max_iterations):
    n = A.shape[0]
    
    # Initialize a random initial eigenvector
    x = np.random.rand(n)
    x = x / np.linalg.norm(x)
    
    eigenvalue = 0.0
    iteration = 0
    
    while iteration < max_iterations:
        # Compute the next iteration
        y = np.dot(A, x)
        
        # Compute the eigenvalue using Rayleigh quotient
        eigenvalue_new = np.dot(x, y) / np.dot(x, x)
        
        # Normalize the eigenvector
        x = y / np.linalg.norm(y)
        
        # Display eigenvalue at each iteration
        print("Iteration {}: Eigenvalue = {}".format(iteration, eigenvalue_new))
        
        # Check for convergence
        if np.abs(eigenvalue_new - eigenvalue) < epsilon:
            break
        
        eigenvalue = eigenvalue_new
        iteration += 1
    
    eigenvector = x
    
    return eigenvalue, eigenvector


# Example usage
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

epsilon = 1e-6
max_iterations = 100

eigenvalue, eigenvector = rayleigh_power(A, epsilon, max_iterations)

print("\nLargest Eigenvalue:", eigenvalue)
print("Corresponding Eigenvector:", eigenvector)
