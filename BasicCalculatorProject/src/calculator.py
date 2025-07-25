def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculator():
    print("Basic Python Calculator")
    print("-------------------------")
    print("Operations: + - * /")

    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operation (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        if op == "+":
            print(f"Result: {add(num1, num2)}")
        elif op == "-":
            print(f"Result: {subtract(num1, num2)}")
        elif op == "*":
            print(f"Result: {multiply(num1, num2)}")
        elif op == "/":
            print(f"Result: {divide(num1, num2)}")
        else:
            print("Invalid operator")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
