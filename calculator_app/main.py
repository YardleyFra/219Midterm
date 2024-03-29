import logging
from calculator.arithmetic import add, subtract, multiply, divide
from calculator.trigonometry import sine, cosine, tangent

log_file = 'calculator_app/logs/'
logging.basicConfig(filename='calculator.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    'sin': sine,
    'cos': cosine,
    'tan': tangent
}

def main():
    # Prompt user for their name
    user_name = input("Enter your name: ")
    logging.info(f"{user_name} started the calculator application")
    
    while True:
        operation = input("\nEnter the operation symbol or 'quit' to exit: ")
        
        if operation.lower() == 'quit':
            logging.info(f"{user_name} exited the calculator application")
            print("Exiting the calculator. Goodbye!")
            break
        
        if operation not in operations:
            print("Invalid operation symbol. Please try again.")
            continue
        
        try:
            values = input("Enter the values separated by spaces: ").split()
            values = [float(val) for val in values]
            result = operations[operation](*values)
            print(f"The result is {result}")
            logging.info(f"Operation: {operation}, Values: {values}, Result: {result}. User: {user_name}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            logging.error(f"Error during operation: {e}. User: {user_name}")
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
