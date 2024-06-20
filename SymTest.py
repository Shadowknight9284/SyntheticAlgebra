import sympy as sp
import numpy as np
import math
import random
from sympy import symbols
import matplotlib.pyplot as plt

def generate_function(class_type):
    x = symbols('x')
    
    if class_type == 'polynomial':
        degree = random.randint(1, 5)
        coefficients = [random.randint(-10, 10) for _ in range(degree + 1)]
        polynomial = sum(coefficients[i] * x**i for i in range(degree + 1))
        return polynomial
    
    elif class_type == 'linear':
        slope = random.randint(-10, 10)
        intercept = random.randint(-10, 10)
        linear = slope * x + intercept
        return linear
    
    elif class_type == 'trigonometric':
        amplitude = random.randint(1, 10)
        frequency = random.randint(1, 10)
        phase_shift = random.uniform(0, 2 * math.pi)
        trigonometric = amplitude * sp.sin(frequency * x + phase_shift)
        return trigonometric
    
    elif class_type == 'exponential':
        base = random.randint(2, 10)
        exponent = random.randint(1, 5)
        exponential = base**x
        return exponential
    
    elif class_type == 'logarithmic':
        logarithmic = sp.log(x)
        return logarithmic
    
    elif class_type == 'rational polynomial':
        numerator = generate_function('polynomial')
        denominator = generate_function('polynomial')
        rational = numerator / denominator
        return rational
    
    elif class_type == 'composite':
        inner_function = generate_function(random.choice(['polynomial', 'linear', 'trigonometric', 'exponential', 'logarithmic', 'rational polynomial']))
        outer_function = generate_function(random.choice(['polynomial', 'linear', 'trigonometric', 'exponential', 'logarithmic', 'rational polynomial']))
        composite = outer_function.subs(x, inner_function)
        return composite
    
    else:
        raise ValueError("Invalid class type")



def quotientBound(f,g):
    h = f/g
    h_prime = h.diff()
    h_double_prime = h_prime.diff()
    x = symbols('x')
    critical_points = sp.solve(h_prime)
    ccu = []
    ccd = []
    for i in critical_points:
        if h_double_prime.subs(x,i) > 0:
            ccu.append([i,h.subs(x,i)])
        elif h_double_prime.subs(x,i) < 0:
            ccd.append([i,h.subs(x,i)])
    if ccu == []:
        ccu.append(-math.inf)
    if ccd == []:
        ccd.append(math.inf)
    return ccu,ccd



