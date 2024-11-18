
# Why Python for Arithmetic?
# Simplicity: Minimal boilerplate for mathematical operations.
# Libraries: Powerful libraries like NumPy, SymPy, and SciPy enable high-performance and symbolic arithmetic.
# Built-in Precision: Handles large numbers and precision arithmetic natively.

class Arithmetic:
    # constructor called
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b
    
    def divison(self):
        return self.a / self.b

arithmetic = Arithmetic(10, 20)
print("Addition:", arithmetic.add())       # 30
print("Multiplication:", arithmetic.multiply())  # 200
print("Division:", arithmetic.divison())
