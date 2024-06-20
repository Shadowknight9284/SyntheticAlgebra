import math
import random
import sympy as sp


class MathFunction:
    def __init__(self, expression):
        self.expression = expression
        
    def __str__(self):
        return self.expression
    
    def evaluate(self, **kwargs):
        try:
            allowed_names = {"__builtins__": None}
            allowed_names.update(kwargs)
            return eval(self.expression, {"__builtins__": None, "math": math}, allowed_names)
        except Exception as e:
            raise ValueError(f"Error evaluating expression: {e}")
        
    def addFunction(self, function):
        self.expression += ' + ' + function.expression
        
    def simplify(self):
        pass 
    # TODO: Implement simplification of the expression
        
        
class LinearFunction(MathFunction):
    def __init__(self, **kwargs):
        coef = kwargs.get('coef', 1)
        bias = f"{kwargs.get('bias', 0)}"
        if len(coef) > 0:
            bias += ' + ' + ' + '.join([f"{coef[i]}*x_{i}" for i in range(len(coef))])
        super().__init__(bias)

class PolynomialFunction(MathFunction):
    def __init__(self, **kwargs):
        bias = f"{kwargs.get('bias', 0)}"
        coef = kwargs.get('coef', 1)
        
       
    