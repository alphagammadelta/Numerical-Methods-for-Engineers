'''Sterling Interpolation'''
import numpy as np

def sterling_interpolation(x, y, x_interp):
    n = len(x)
    m = len(x_interp)
    coeffs = np.zeros(n)
    f_interp = np.zeros(m)

    for i in range(n):
        coeffs[i] = y[i]
        for j in range(n):
            if i != j:
                coeffs[i] /= (x[i] - x[j])

    for k in range(m):
        f_interp[k] = 0.0
        for i in range(n):
            prod = 1.0
            for j in range(n):
                if i != j:
                    prod *= (x_interp[k] - x[j])
            f_interp[k] += coeffs[i] * prod

    return f_interp

# Example usage
x = np.array([0.0, 1.0, 2.0, 3.0, 4.0])  # given x data points
y = np.array([1.0, 3.0, 5.0, 4.0, 2.0])  # given y data points
x_interp = np.array([0.25, 1.23, 2.14, 3.57])  # x points for interpolation

y_interp = sterling_interpolation(x, y, x_interp)
print("Interpolated y values:", y_interp)
