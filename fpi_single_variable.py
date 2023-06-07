'''fpi single variable'''
import numpy as np

def fixed_point_iteration(g, x0, tol=1e-6, max_iter=100):
    x = x0
    iterations = 0

    while True:
        x_new = g(x)

        iterations += 1

        # Display the value at each iteration
        print(f"Iteration {iterations}: x = {x_new}")

        if abs(x_new - x) < tol or iterations >= max_iter:
            break

        x = x_new

    return x_new

# Example usage
def g(x):
    return np.cos(x)

initial_guess = 0.5
fixed_point = fixed_point_iteration(g, initial_guess)
