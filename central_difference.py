'''Central Difference'''
import numpy as np

def central_difference(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

def richardson_extrapolation(cd1, cd2, r):
    return (2**r * cd2 - cd1) / (2**r - 1)

# Example usage
def f(x):
    return np.sin(x)

x = np.pi / 4  # Point at which to compute the derivative
h = 0.01  # Step size

cd1 = central_difference(f, x, h)
cd2 = central_difference(f, x, h/2)

derivative = richardson_extrapolation(cd1, cd2, 1)
print("Numerical derivative:", derivative)
