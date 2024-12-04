class Calculator:
    def __init__(self, a, b, operation):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == 'addition':
            return self.a + self.b
        elif self.operation == 'subtraction':
            return self.a - self.b
        elif self.operation == 'multiplication':
            return self.a * self.b
        elif self.operation == 'division':
            if self.b != 0:
                return self.a / self.b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"

# Example usage
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operation = input("Enter operation (Addition, Subtraction, Multiplication, Division): ")
calc = Calculator(a, b, operation)
print(f"Result: {calc.calculate()}")
