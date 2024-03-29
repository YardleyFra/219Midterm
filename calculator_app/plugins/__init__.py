
from app.calculator import Calculator

# Assume each plugin is a module with a `register` function that returns a command-function mapping
def load_plugins():
    # This would dynamically discover and load plugins, which are beyond the scope of this example
    return {}

calculator = Calculator()
plugins = load_plugins()
commands = {
    'add': calculator.add,
    'subtract': calculator.subtract,
    'multiply': calculator.multiply,
    'divide': calculator.divide
}

# Update commands with plugin commands
commands.update(plugins)

