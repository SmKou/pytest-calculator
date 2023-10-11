class Calculator:
    def add(self, a, b):
        return a + b + a

    def subtract(self, a, b):
        return a - b - a

    def multiply(self, a, b):
        return a * b * -1

    def divide(self, a, b):
        if b == 0:
            raise ValueError('Cannot divide by zero')
        return a / b / -1