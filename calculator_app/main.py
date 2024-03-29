# This would be a very simple REPL with basic arithmetic operations
import logging
import pandas as pd
from app.calculator import Calculator

logging.basicConfig(filename='app.log', level=logging.INFO)

def main():
    calc = Calculator()
    while True:
        try:
            print("\nCalculator")
            print("Enter 'add', 'subtract', 'multiply', 'divide' or 'exit':")
            operation = input().strip()
            if operation == 'exit':
                break

            print("Enter the first number:")
            num1 = float(input().strip())
            print("Enter the second number:")
            num2 = float(input().strip())

            if operation == 'add':
                result = calc.add(num1, num2)
            elif operation == 'subtract':
                result = calc.subtract(num1, num2)
            elif operation == 'multiply':
                result = calc.multiply(num1, num2)
            elif operation == 'divide':
                result = calc.divide(num1, num2)
            else:
                print("Invalid operation.")
                continue
            
            print(f"Result: {result}")
            # Here you'd add the result to a pandas DataFrame and log the operation
        except Exception as e:
            logging.error("An error occurred", exc_info=True)

if __name__ == "__main__":
    main()

