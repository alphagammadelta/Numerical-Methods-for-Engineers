'''Approximating double integrals using trapezoidal rule'''
def f(x, y):
    # Define your function here
    return x**2 + y**2

def double_integral_approximation(a, b, c, d, m, n):
    h1 = (b - a) / m
    h2 = (d - c) / n
    integral_sum = 0.0

    for i in range(1, m):
        x_i = a + i * h1
        for j in range(1, n):
            y_j = c + j * h2
            f_ij = f(x_i, y_j)
            integral_sum += f_ij

    integral_sum += 0.5 * (f(a, c) + f(b, c) + f(a, d) + f(b, d))

    integral_approximation = h1 * h2 * integral_sum
    return integral_approximation

# Example usage
a = 0
b = 1
c = 0
d = 1
m = 100  # Number of divisions in x-direction
n = 100  # Number of divisions in y-direction

approximation = double_integral_approximation(a, b, c, d, m, n)
print("Approximation of double integral:", approximation)
