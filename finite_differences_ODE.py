import numpy as np
import matplotlib.pyplot as plt

def f(t, y):
    # Define your differential equation here
    # y is the dependent variable
    # t is the independent variable

    # Example: dy/dt = -2ty
    dydt = -2 * t * y

    return dydt

def solve_ivp_fd(t0, tf, y0, h):
    num_steps = int((tf - t0) / h)  # Number of steps

    t = np.linspace(t0, tf, num_steps + 1)  # Time points
    y = np.zeros(num_steps + 1)  # Solution array
    y[0] = y0  # Initial condition

    for i in range(num_steps):
        y[i + 1] = y[i] + h * f(t[i], y[i])

    return t, y

# Example usage
t0 = 0.0
tf = 1.0
y0 = 1.0  # Initial value of y
h = 0.1  # Step size

t, y = solve_ivp_fd(t0, tf, y0, h)
print("The solution is: ",y)

# Plotting the solution

plt.plot(t, y, 'b.-')
plt.xlabel('t')
plt.ylabel('y')
plt.title('Finite Difference Method Solution')
plt.grid(True)
plt.show()
