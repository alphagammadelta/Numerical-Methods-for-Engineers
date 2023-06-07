'''Trapezoidal Rule and refinement using Romberg Integration'''
def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    
    for i in range(1, n):
        x = a + i * h
        result += f(x)
    
    result *= h
    
    return result

def romberg_integration(f, a, b, max_iterations):
    r = [[0] * (max_iterations+1) for _ in range(max_iterations+1)]
    
    for i in range(1, max_iterations+1):
        r[i][1] = trapezoidal_rule(f, a, b, 2**(i-1))
        
        for j in range(2, i+1):
            r[i][j] = (4**(j-1) * r[i][j-1] - r[i-1][j-1]) / (4**(j-1) - 1)
            
        if abs(r[i][i] - r[i-1][i-1]) < 1e-6:
            break
    
    return r[i][i]


import math

def my_function(x):
    return math.sin(x)

a = 0.0
b = math.pi / 2
max_iterations = 10

integral_approximation = romberg_integration(my_function, a, b, max_iterations)
print("Approximation:", integral_approximation)
