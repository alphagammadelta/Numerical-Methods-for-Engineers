import numpy as np

def f(t, y):
    # System of two differential equations
    # y[0] represents the first variable (x)
    # y[1] represents the second variable (y)
    # dy[0]/dt = x + 2 * y
    # dy[1]/dt = x - y
    dydt_0 = y[0] + 2 * y[1]
    dydt_1 = y[0] - y[1]

    return np.array([dydt_0, dydt_1])

def runge_kutta_2nd_order(t0, tf, y0, h):
    t = t0
    y = y0

    while t < tf:
        if t + h > tf:
            h = tf - t

        k1 = h * f(t, y)
        k2 = h * f(t + h/2, y + k1/2)

        y = y + k2
        t = t + h

    return y

t0 = 0.0
tf = 1.0
y0 = np.array([1.0, 2.0])  # Initial values of variables
h = 0.1  # Step size

result = runge_kutta_2nd_order(t0, tf, y0, h)
print("Final values:", result)