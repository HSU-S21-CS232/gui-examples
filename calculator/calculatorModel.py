class Calculator:

    def __init__(self):
        self._accumulator = 0.0
    
    def add(self, number):
        self._accumulator += number
    
    def subtract(self, number):
        self._accumulator -= number

    def multiply(self, number):
        self._accumulator *= number

    def divide(self, number):
        self._accumulator /= number
    
    def clear(self):
        self._accumulator = 0.0

    def load(self, number):
        self._accumulator = number

    def value(self):
        return self._accumulator