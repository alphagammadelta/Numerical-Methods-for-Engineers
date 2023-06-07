'''Thomas Algorithm'''
import numpy as np

def thomas_algorithm(a, b, c, d):
    n = len(d)
    c_dash = np.zeros(n-1)
    d_dash = np.zeros(n)

    c_dash[0] = c[0] / b[0]
    d_dash[0] = d[0] / b[0]

    for i in range(1, n-1):
        m = 1.0 / (b[i] - a[i-1] * c_dash[i-1])
        c_dash[i] = c[i] * m
        d_dash[i] = (d[i] - a[i-1] * d_dash[i-1]) * m

    d_dash[n-1] = (d[n-1] - a[n-2] * d_dash[n-2]) / (b[n-1] - a[n-2] * c_dash[n-2])

    x = np.zeros(n)
    x[n-1] = d_dash[n-1]

    for i in range(n-2, -1, -1):
        x[i] = d_dash[i] - c_dash[i] * x[i+1]

    return x

# Example usage
a = np.array([1, 1, 1])  # lower diagonal
b = np.array([4, 5, 6])  # main diagonal
c = np.array([1, 1, 1])  # upper diagonal
d = np.array([7, 8, 9])  # right-hand side

solution = thomas_algorithm(a, b, c, d)
print("Solution:", solution)
