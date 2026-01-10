def operations_menu():
    print("Available operations: ")
    print(" + sum")
    print(" - subtraction")
    print(" * multiplication")
    print(" / division")
    print(" = calculate operation")
    print(" C Restart calculation")
    print(" q quit")

def calculate(result, operation, number):
    if operation == '+':
        return result + number
    elif operation == '-':
        return result - number
    elif operation == '*':
        return result * number
    elif operation == '/':
        if number == 0:
            print("Error, dividing by zero is undefined")
            return result
        return result / number
    else:
        print("Invalid operation")
        return result

def run_calculator():
    print("Command line calculator")
    result = 0.0
    first_number = True

    print(result)

    while True:
        if first_number:
            try:
                result = float(input("Insert the first number\n"))
                first_number = False
            except ValueError:
                print("Invalid Number")
                continue
        else:
            operations_menu()
            operation = input("Select an operation from the menu\n").strip()

            if operation == '=':
                print(f"\nResult: {result}\n")
                continue
            elif operation == 'C':
                result = 0.0
                first_number = True
                print("\nResult Restarted\n")
                print(result)
                continue
            elif operation == 'q':
                print("\nClosing Calculator")
                break
            elif operation not in ['+','-','*','/']:
                print("\nInvalid Operation\n")
                continue

            try:
                number = float(input("Insert the next number\n"))
            except ValueError:
                print("Invalid Number")
                continue

            result = calculate(result, operation, number)
            print(f"\nResult = {result}\n")

# Ejecutar calculadora
run_calculator()
