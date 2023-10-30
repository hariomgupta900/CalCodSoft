# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y == 0:
        return "Division by zero is not allowed"
    return x / y

# Prompt the user to input two numbers
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number:"))

    # Prompt the user to select an operation
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter operation (1/2/3/4): ")

    if choice not in ['1', '2', '3', '4']:
        print("Invalid input")
    else:
        if choice == '1':
            result = add(num1, num2)
            operation = "+"
        elif choice == '2':
            result = subtract(num1, num2)
            operation = "-"
        elif choice == '3':
            result = multiply(num1, num2)
            operation = "*"
        else:
            result = divide(num1, num2)
            operation = "/"

        print(f"{num1} {operation} {num2} = {result}")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
