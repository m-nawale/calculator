# cli entry point for the calculator application using questionary

from calculator import Calculator
import questionary

def main():
    calc = Calculator()
    
    operation = questionary.select(
        "Choose an operation:",
        choices=[
            "Add",
            "Subtract",
            "Multiply",
            "Divide"
        ]).ask()
    
    a = float(questionary.text("Enter the first number:").ask())
    b = float(questionary.text("Enter the second number:").ask())
    
    if operation == "Add":
        result = calc.add(a, b)
    elif operation == "Subtract":
        result = calc.subtract(a, b)
    elif operation == "Multiply":
        result = calc.multiply(a, b)
    elif operation == "Divide":
        try:
            result = calc.divide(a, b)
        except ValueError as e:
            print(e)
            return
    
    print(f"The result of {operation.lower()}ing {a} and {b} is: {result}")

if __name__ == "__main__":
    main()

