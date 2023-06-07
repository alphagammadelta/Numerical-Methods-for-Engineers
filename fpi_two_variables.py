'''fpi two variables'''
import numpy as np

def fixed_point_iteration(f, g, x0, y0, tol=1e-6, max_iter=100):
    x = x0
    y = y0
    iterations = 0

    while True:
        x_new = f(x, y)
        y_new = g(x, y)

        iterations += 1

        # Display the value at each iteration
        print(f"Iteration {iterations}: x = {x_new}, y = {y_new}")

        if abs(x_new - x) < tol and abs(y_new - y) < tol or iterations >= max_iter:
            break

        x = x_new
        y = y_new

    return x_new, y_new

# Example usage
def f(x, y):
    return np.sin(x + y)

def g(x, y):
    return np.cos(x - y)

initial_guess_x = 1.0
initial_guess_y = 1.0

fixed_point = fixed_point_iteration(f, g, initial_guess_x, initial_guess_y)
