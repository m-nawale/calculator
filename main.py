# main entry point for the calculator application

from calculator import Calculator

def main():
    C=Calculator()
    print("Addition: ", C.add(15, 10))
    print("Subtraction: ", C.subtract(15, 10))
    print("Multiplication: ", C.multiply(15, 10))

if __name__ == "__main__":
    main()