'''Forward Difference'''
import numpy as np

def forward_difference(f, x, h):
    return (f(x + h) - f(x)) / h

def richardson_extrapolation(fd1, fd2, r):
    return (2**r * fd2 - fd1) / (2**r - 1)

# Example usage
def f(x):
    return np.sin(x)

x = np.pi / 4  # Point at which to compute the derivative
h = 0.1  # Step size

fd1 = forward_difference(f, x, h)
fd2 = forward_difference(f, x, h/2)

derivative = richardson_extrapolation(fd1, fd2, 1)
print("Numerical derivative:", derivative)
