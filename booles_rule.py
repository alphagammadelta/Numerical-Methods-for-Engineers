'''Boole's Rule and refinement using Romberg Integration'''
def booles_rule(f, a, b, n):
    h = (b - a) / n
    result = 7 * (f(a) + f(b))
    
    for i in range(1, n, 4):
        x0 = a + i * h
        x1 = a + (i+1) * h
        x2 = a + (i+2) * h
        x3 = a + (i+3) * h
        result += 32 * f(x0) + 12 * f(x1) + 32 * f(x2) + 14 * f(x3)
    
    result *= 2 * h / 45
    
    return result

def romberg_integration(f, a, b, max_iterations):
    r = [[0] * (max_iterations+1) for _ in range(max_iterations+1)]
    
    for i in range(1, max_iterations+1):
        r[i][1] = booles_rule(f, a, b, 4**(i-1))
        
        for j in range(2, i+1):
            r[i][j] = (4**(j-1) * r[i][j-1] - r[i-1][j-1]) / (4**(j-1) - 1)
            
        if abs(r[i][i] - r[i-1][i-1]) < 1e-6:
            break
    
    return r[i][i]

# Example usage
import math

def my_function(x):
    return math.sin(x)

a = 0.0
b = math.pi / 2
max_iterations = 10

integral_approximation = romberg_integration(my_function, a, b, max_iterations)
print("Approximation:", integral_approximation)
