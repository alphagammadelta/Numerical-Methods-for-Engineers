'''Backward Difference'''
import numpy as np

def backward_difference(f, x, h):
    return (f(x) - f(x - h)) / h

def richardson_extrapolation(bd1, bd2, r):
    return (2**r * bd2 - bd1) / (2**r - 1)

# Example usage
def f(x):
    return np.sin(x)

x = np.pi / 4  # Point at which to compute the derivative
h = 0.01  # Step size

bd1 = backward_difference(f, x, h)
bd2 = backward_difference(f, x, h/2)

derivative = richardson_extrapolation(bd1, bd2, 1)
print("Numerical derivative:", derivative)
