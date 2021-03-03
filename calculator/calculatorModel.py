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
    
if __name__ == '__main__':
    x = int(input("Enter a number: "))
    y = int(input("Enter another number: "))
    calc = Calculator()
    calc.load(x)
    calc.add(y)
    print(x, "+", y, "=", calc.value())

    #unit tests
    assert x + y == calc.value()