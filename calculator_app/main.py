import logging
import pandas as pd
import os
from calculator.arithmetic import add, subtract, multiply, divide
from calculator.trigonometry import sine, cosine, tangent


log_directory = 'calculator_app/logs'
os.makedirs(log_directory, exist_ok=True)


log_file = os.path.join(log_directory, 'calculator.log')
logging.basicConfig(calFile=log_file, level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


calculation_history = pd.DataFrame(columns=['Operation', 'Values', 'Result'])


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    'sin': sine,
    'cos': cosine,
    'tan': tangent
}

def load_history(calFile):
    global calculation_history
    try:
        calculation_history = pd.read_csv(calFile)
        print("Calculation history loaded successfully.")
    except FileNotFoundError:
        print("Calculation history file not found.")
    except Exception as e:
        print("Error occurred while loading calculation history:", e)

def save_history(calFile):
    global calculation_history
    try:
        if not os.path.exists(calFile):
            with open(calFile, 'w'):  # Create the file if it doesn't exist
                pass
        calculation_history.to_csv(calFile, index=False)
        print("Calculation history saved successfully.")
    except Exception as e:
        print("Error occurred while saving calculation history:", e)

def clear_history():
    global calculation_history
    calculation_history = pd.DataFrame(columns=['Operation', 'Values', 'Result'])
    print("Calculation history cleared.")

def delete_record(index):
    global calculation_history
    try:
        calculation_history.drop(index, inplace=True)
        print("Record deleted successfully.")
    except KeyError:
        print("Invalid record index.")
    except Exception as e:
        print("Error occurred while deleting record:", e)

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

        if operation.lower() == 'load':
            calFile = input("Enter the calFile to load: ")
            load_history(calFile)
            continue

        if operation.lower() == 'save':
            calFile = input("Enter the calFile to save: ")
            save_history(calFile)
            continue

        if operation.lower() == 'clear':
            clear_history()
            continue

        if operation.lower().startswith('delete'):
            index = int(operation.split()[-1])
            delete_record(index)
            continue

        if operation not in operations:
            print("Invalid operation symbol. Please try again.")
            continue

        try:
            values = input("Enter the values separated by spaces: ").split()
            values = [float(val) for val in values]
            result = operations[operation](*values)
            print(f"The result is {result}")
            # Append calculation to history
            calculation_history = calculation_history.append({'Operation': operation, 'Values': values, 'Result': result}, ignore_index=True)
            logging.info(f"Operation: {operation}, Values: {values}, Result: {result}. User: {user_name}")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except Exception as e:
            logging.error(f"Error during operation: {e}. User: {user_name}")
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
