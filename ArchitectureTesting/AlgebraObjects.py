import random
class Linear:
    def __init__(self):
        self.order = 0
        self.coef = []
        self.bias = 0
    
    def generate(self, coef, bias):
        self.order = len(coef)
        self.coef = coef
        self.bias = bias
        
    def random(self, order):
        self.order = order
        self.coef = [random.gauss(0, 1) for _ in range(self.order)]
        self.bias = random.gauss(0, 1)
        
    def __str__(self):
        s = ""
        for i in range(self.order-1, -1, -1):
            s += str(self.coef[i]) + "*x_" + str(i) + " + "
        s += str(self.bias)
        return s
    
    
class Polynomial:
    def __init__(self):
        self.order = 0
        self.coef = []
    
    def generate(self, coef, bias):
        self.order = len(coef)
        self.coef = coef
        
    def random(self, order):
        self.order = order
        self.coef = [random.gauss(0, 1) for _ in range(self.order+1)]
        
    def __str__(self):
        s = ""
        for i in range(self.order, 0, -1):
            s += str(self.coef[i]) + "*x^" + str(i) + " + "
        s += str(self.coef[0])
        return s

class Rational:
    def __init__(self):
        self.numerator = 0
        self.denominator = 1
        
    def generate(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
        
    def random(self):
        self.numerator = Linear()
        self.numerator.random(1)
        self.denominator = Linear()
        self.denominator.random(1)
        
    def __str__(self):
        s = str(self.numerator) + "/" + str(self.denominator)
        return s

class Exponential:
    def __init__(self):
        self.base = 0
        self.power = 1
        self.coefficient = 1
        
    def generate(self, base, power, coefficient):
        self.base = base
        self.power = power
        self.coefficient = coefficient
        
    def random(self):
        self.base = random.random()*5
        self.power = random.gauss(0, 1)
        self.coefficient = random.gauss(0, 1)
        
    def __str__(self):
        s = str(self.coefficient) + "*" + str(self.base) + "^" + str(self.power) + "x"
        return s
    
class Logarithm:
    def __init__(self):
        self.base = 0
        self.coefficient = 1
        
    def generate(self, base, coefficient):
        self.base = base
        self.coefficient = coefficient
        
    def random(self):
        self.base = random.random()*5
        self.coefficient = random.gauss(0, 1)
        
    def __str__(self):
        s = str(self.coefficient) + "*log" + str(self.base) + "x"
        return s
    
    