'''Newton Raphson Method'''
import numpy as np

def newton_raphson_method(f, g, df_dx, df_dy, dg_dx, dg_dy, x0, y0, tol=1e-6, max_iter=100):
    x = x0
    y = y0
    iterations = 0

    while True:
        f_val = f(x, y)
        g_val = g(x, y)

        # Calculate the Jacobian matrix
        J = np.array([[df_dx(x, y), df_dy(x, y)],
                      [dg_dx(x, y), dg_dy(x, y)]])

        # Calculate the increment
        delta = np.linalg.solve(J, np.array([-f_val, -g_val]))

        x += delta[0]
        y += delta[1]

        iterations += 1

        # Display the values at each iteration
        print(f"Iteration {iterations}: x = {x}, y = {y}")

        if np.linalg.norm(delta) < tol or iterations >= max_iter:
            break

    return x, y

# Example usage
def f(x, y):
    return x**3 + y**2 - 1

def g(x, y):
    return x + y - 1

def df_dx(x, y):
    return 3 * (x**2)

def df_dy(x, y):
    return 2 * y

def dg_dx(x, y):
    return 1

def dg_dy(x, y):
    return 1

initial_guess_x = 0.5
initial_guess_y = 0.5

solution = newton_raphson_method(f, g, df_dx, df_dy, dg_dx, dg_dy, initial_guess_x, initial_guess_y)
