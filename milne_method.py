import numpy as np

def f(t, y):
    # Define your differential equation here
    # y is the dependent variable
    # t is the independent variable

    # Example: dy/dt = t^2 + y
    dydt = t**2 + y

    return dydt

def milne_method(t0, tf, y0, h):
    t = t0
    y = y0

    while t < tf:
        if t + h > tf:
            h = tf - t

        y_pred = y + (4 * h / 3) * f(t, y)
        t_pred = t + h

        y_corr = y + (h / 3) * (f(t_pred, y_pred) + 2 * f(t, y))
        t_corr = t + h

        y = y_corr
        t = t_corr

    return y

# Example usage
t0 = 0.0
tf = 1.0
y0 = 0.0  # Initial value of y
h = 0.1  # Step size

result = milne_method(t0, tf, y0, h)
print("Final value of y:", result)
