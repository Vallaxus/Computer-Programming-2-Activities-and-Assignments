def add(a, b): return a + b


def subtract(a, b=0): return a - b


def multiply(a, b=1): return a * b


def divide(a, b): return f"{a}/{b} = {a / b}" if b != 0 else "Error: Division by zero."


def main():
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    choice = input("Enter choice (1/2/3/4): ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(a=num1, b=num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(divide(num1, num2))
    else:
        print("Invalid choice.")


main()
