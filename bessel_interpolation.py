'''Bessel Interpolation'''
import numpy as np
from scipy.special import jn, jn_zeros

def bessel_interpolation(x, y, x_interp, order):
    n = len(x)
    m = len(x_interp)
    f_interp = np.zeros(m)

    for k in range(m):
        f_interp[k] = 0.0
        for i in range(n):
            bessel_arg = np.pi * order * (x_interp[k] - x[i]) / (x[n-1] - x[0])
            bessel_val = jn(order, bessel_arg)
            f_interp[k] += y[i] * bessel_val

    return f_interp

# Example usage
x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])  # given x data points
y = np.array([1.0, 3.0, 5.0, 4.0, 2.0])  # given y data points
x_interp = np.array([0.25, 1.23, 2.14, 3.57])  # x points for interpolation
order = 2  # Bessel function order

y_interp = bessel_interpolation(x, y, x_interp, order)
print("Interpolated y values:", y_interp)
