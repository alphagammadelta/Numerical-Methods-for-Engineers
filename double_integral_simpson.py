'''Approximating double integrals using simpson 1/3rd rule'''
def f(x, y):
    # Define your function here
    return x**2 + y**2

def double_integral_approximation(a, b, c, d, m, n):
    h1 = (b - a) / m
    h2 = (d - c) / n
    integral_sum = 0.0

    for i in range(m + 1):
        x_i = a + i * h1
        for j in range(n + 1):
            y_j = c + j * h2
            f_ij = f(x_i, y_j)
            weight = 1.0
            if i == 0 or i == m:
                weight *= 1.0 / 3.0
            elif i % 2 == 0:
                weight *= 2.0 / 3.0
            else:
                weight *= 4.0 / 3.0

            if j == 0 or j == n:
                weight *= 1.0 / 3.0
            elif j % 2 == 0:
                weight *= 2.0 / 3.0
            else:
                weight *= 4.0 / 3.0

            integral_sum += weight * f_ij

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
