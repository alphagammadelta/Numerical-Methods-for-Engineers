'''Simphson 1/3 Rule and refinement using Romberg Integration'''
def simpsons_rule(f, a, b, n):
    h = (b - a) / n
    result = f(a) + f(b)
    
    for i in range(1, n):
        x = a + i * h
        if i % 2 == 0:
            result += 2 * f(x)
        else:
            result += 4 * f(x)
    
    result *= h / 3
    
    return result

def romberg_integration(f, a, b, max_iterations):
    r = [[0] * (max_iterations+1) for _ in range(max_iterations+1)]
    
    for i in range(1, max_iterations+1):
        r[i][1] = simpsons_rule(f, a, b, 2**(i-1))
        
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
