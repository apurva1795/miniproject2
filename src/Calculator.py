def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a  *  b

def division(a, b):
    return a / b

def square(a, b):
    return a * a

def squareRoot(a, b):
    return a ** 0.5

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = addition(a, b)
        return self.result

    def square(self, a, b):
        self.result = square(a, b)
        return self.result

    def squareRoot(self, a, b):
        self.result = squareRoot(a, b)
        return self.result